from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

# Python 함수 정의
def write_to_file():
    with open("/tmp/hello.txt", "w") as f:
        f.write("Hello from PythonOperator!")

with DAG(
    dag_id="python_bash_mixed_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    # PythonOperator로 파일 생성
    create_file = PythonOperator(
        task_id="create_file",
        python_callable=write_to_file,
    )

    # BashOperator로 파일 내용 출력
    show_file = BashOperator(
        task_id="show_file",
        bash_command="cat /tmp/hello.txt",
    )

    # BashOperator로 파일 삭제
    delete_file = BashOperator(
        task_id="delete_file",
        bash_command="rm /tmp/hello.txt",
    )

    create_file >> show_file >> delete_file