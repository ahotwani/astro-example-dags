from datetime import datetime
from airflow.models.dag import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator

with DAG(dag_id="triggering_dag", schedule=None, start_date=datetime(2023, 1, 1)):
    SimpleHttpOperator(
        task_id="trigger_external_dag",
        log_response=True,
        method="POST",
            # Change this to the DAG_ID of the DAG you are triggering
        endpoint=f"api/v1/dags/hello_world/dagRuns",
        http_conn_id="http_conn",
        data={
            "logical_date": "{{ logical_date }}"
        }
    )
