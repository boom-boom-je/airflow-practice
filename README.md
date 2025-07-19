# Airflow Practice Repository

이 리포지토리는 **Apache Airflow**를 처음 학습하면서 실습한 내용을 정리한 공간입니다.  
단순한 DAG 실행부터 XCom, GCS 연동, 환경 제거까지 단계적으로 구성되어 있으며, 각 디렉토리에는 실습에 사용된 DAG 파일과 실행 결과 스크린샷이 포함되어 있습니다.

---

> ## 📁 디렉토리 구조 및 실습 내용

| 디렉토리 | 내용 |
|----------|------|
| `1_Airflow 환경 생성` | Docker 기반의 Airflow 환경 구성 및 Web UI 접속 확인 |
| `2_Python_Operator` | PythonOperator를 활용한 DAG 작성 및 task 실행 실습 |
| `3_Bash_Operator` | BashOperator를 활용하여 bash 명령어 실행 실습 |
| `4_Bash_Python_Mixed_Operator` | BashOperator와 PythonOperator를 함께 사용하는 DAG 구성 실습 |
| `5_XCom` | XCom을 활용한 태스크 간 데이터 전달 실습 |
| `6_GCS_Airflow` | Google Cloud Storage와 연동한 DAG 구성 실습 |
| `7_Airflow 삭제` | 사용한 Airflow 환경 삭제 및 정리 절차 |

> 각 폴더에는 관련 DAG 코드와 실행 결과 스크린샷이 포함되어 있습니다.

> ## 🛠️ 사용 환경

- **Python**
- **Airflow**
- 일부 실습에서는 **Google Cloud Storage (GCS)** 연동 필요

---
