from airflow import DAG
from airflow.operators.python import PythonOperator
from google.cloud import storage
from datetime import datetime

def download_from_gcs():
    client = storage.Client()
    bucket = client.bucket("airflow-demo-bucket-1")
    blob = bucket.blob("sample_data.csv")
    blob.download_to_filename("/tmp/sample_data.csv")
    print("GCS에서 파일 다운로드 완료!")

with DAG(
    dag_id="gcs_download_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    download_task = PythonOperator(
        task_id="download_csv_from_gcs",
        python_callable=download_from_gcs,
    )