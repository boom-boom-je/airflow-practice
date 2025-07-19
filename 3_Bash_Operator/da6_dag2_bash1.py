from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bash_file_workflow",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    create_file = BashOperator(
        task_id="create_temp_file",
        bash_command='echo "temporary data" > /tmp/temp_file.txt',
    )

    show_file = BashOperator(
        task_id="show_file_contents",
        bash_command='cat /tmp/temp_file.txt',
    )

    delete_file = BashOperator(
        task_id="delete_temp_file",
        bash_command='rm /tmp/temp_file.txt',
    )

    create_file >> show_file >> delete_file