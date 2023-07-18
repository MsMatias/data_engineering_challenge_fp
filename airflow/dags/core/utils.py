import logging
import pathlib
from pandas import DataFrame

from airflow.hooks.postgres_hook import PostgresHook

logger = logging.getLogger(__name__)

def get_query(name: str) -> str:
    path = pathlib.Path(__file__).parent.parent.absolute()
    file = open(f"{path}/sql/{name}")
    return file.read()


def get_data() -> list:
    logger.info("Fetching data from the database...")

    hook = PostgresHook('dwh')
    conn = hook.get_conn()
    cursor = conn.cursor()

    cursor.execute(get_query("report.sql"))

    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row)) for row in cursor.fetchall()]

    conn.commit()
    conn.close()

    logger.info("Data fetched successfully.")
    return data


def generate_report(**context: object) -> None:
    logger.info("Generating report...")
    logger.info(context)

    data = get_data()
    df = DataFrame(data)
    df.to_csv("/opt/airflow/data/{}_{}.csv".format(context['report_name'], context['ts_nodash']), index=False)

    logger.info("Report generated successfully.")
