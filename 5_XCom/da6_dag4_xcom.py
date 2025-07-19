from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# 1단계: 이름 리스트 push
def push_names():
    return ["Alice", "Bob", "Charlie", "Diana"]

# 2단계: 이름 개수 출력
def count_names(ti):
    names = ti.xcom_pull(task_ids="push_names_task")
    print(f"이름 개수: {len(names)}")
    print(f"이름 목록: {names}")

# DAG 정의
with DAG(
    dag_id="xcom_list_example_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    push_names_task = PythonOperator(
        task_id="push_names_task",
        python_callable=push_names,
    )

    count_names_task = PythonOperator(
        task_id="count_names_task",
        python_callable=count_names,
    )

    push_names_task >> count_names_task