DROP TABLE IF EXISTS public.workorders;
CREATE TABLE IF NOT EXISTS public.workorders (
    time timestamp,
    product bigint,
    production real
);

DROP TABLE IF EXISTS public.metrics;
CREATE TABLE IF NOT EXISTS public.metrics (
    id bigint,
    val real,
    time timestamp
);

CREATE DATABASE airflow;