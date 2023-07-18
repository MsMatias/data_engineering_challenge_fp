import airflow
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from core.utils import generate_report

DAG_ID = "report"

with DAG(
    dag_id=DAG_ID,
    start_date=datetime(2023, 7, 17),
    schedule="0 * * * *",
    catchup=False,
) as dag:
    get_report = PythonOperator(
                    task_id='get_report', 
                    python_callable=generate_report,
                    op_kwargs={
                        "report_name": "report"
                    }
                )
