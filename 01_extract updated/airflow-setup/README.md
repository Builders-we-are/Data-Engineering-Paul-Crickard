follow the instruction from the official airflow page to create my docker 

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

# steps

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.0.1/docker-compose.yaml'

mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

before you run docker make sure your memory is more than 4G else you will get an error

docker compose up airflow-init


docker compose up



I found a resource that might help you if this is the first time you're using docker

https://www.youtube.com/watch?v=aTaytcxy2Ck
