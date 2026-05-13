from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="annex_pipeline",
    start_date=datetime(2026,5,12),
    schedule="@daily",
    catchup=False
) as dag:

    ingest = BashOperator(
        task_id="ingest_data",
        bash_command="python /opt/airflow/scripts/ingest.py"
    )

    clean = BashOperator(
        task_id="clean_data",
        bash_command="python /opt/airflow/scripts/clean.py"
    )

    features = BashOperator(
        task_id="feature_engineering",
        bash_command="python /opt/airflow/scripts/features.py"
    )

    quality = BashOperator(
        task_id="quality_checks",
        bash_command="python /opt/airflow/scripts/quality.py"
    )

    analysis = BashOperator(
        task_id="analysis",
        bash_command="python /opt/airflow/scripts/analysis.py"
    )

    ingest >> clean >> features >> quality >> analysis
