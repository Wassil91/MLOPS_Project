from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import psycopg2
import mlflow
import pandas as pd

def transform_data():
    # Connectez-vous à la base de données PostgreSQL pour récupérer les données à transformer
    postgres_host = os.environ.get('AZURE_DB_HOST')  
    postgres_port = os.environ.get('AZURE_DB_PORT')  
    postgres_user = os.environ.get('AZURE_DB_USER')  
    postgres_password = os.environ.get('AZURE_PG_PASSWORD')  
    postgres_database = os.environ.get('AZURE_DB_NAME')
    
    conn = psycopg2.connect(
        host=postgres_host,
        port=postgres_port,
        user=postgres_user,
        password=postgres_password,
        database=postgres_database
    )
    cursor = conn.cursor()
    
    # Exemple de récupération des données pour la transformation
    cursor.execute("""
        SELECT n_dpe, surface
        FROM dpe_logement 
        WHERE processed = true
    """)
    data = cursor.fetchall()
    
    # Transformer les données selon vos besoins
    transformed_data = [(row[0], some_transformation_function(row[1])) for row in data]
    transformed_df = pd.DataFrame(transformed_data, columns=['n_dpe', 'transformed_column'])
    
    # Enregistrer les données transformées dans MLflow
    mlflow.log_table(df=transformed_df, table_name='dpe_training')
    
    conn.commit()
    cursor.close()
    conn.close()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag_transform_data = DAG(
    'transform_data',
    default_args=default_args,
    description='DAG pour transformer les données dans la base de données PostgreSQL',
    schedule_interval='@daily',
)

transform_data_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform_data,
    dag=dag_transform_data,
)

