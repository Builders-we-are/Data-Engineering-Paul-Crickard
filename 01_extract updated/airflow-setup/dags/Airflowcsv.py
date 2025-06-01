import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd


def csvToJson():
    df = pd.read_csv("data.csv")
    for i, r in df.iterrows():
        print(r["name"])
    df.to_json("fromAirflow.json", orient="records")


default_args = {
    "owner": "paulcrickard",
    "start_date": dt.datetime(2025, 6, 29),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    "MyCSVDAG",
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),  #'0 * * * * *',
) as dag:
    print_starting = BashOperator(
        task_id="starting", bash_command='echo "I am reading the csv now......."'
    )
    csvJson = PythonOperator(task_id="convertCSVtoJSON", python_callable=csvToJson)

    print_starting >> csvJson
