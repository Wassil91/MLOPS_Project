from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests
import json
import pandas as pd
import os
import psycopg2

from dotenv import load_dotenv

DATA_PATH = os.path.dirname(os.path.abspath(__file__))

def check_environment_setup():
    # Vérifier que tous les fichiers sont disponibles et les variables d'environnement bien déclarées
    required_files = ["load_data.py" ,  "model_trainning.py",  "transform_data.py"]  # Liste des fichiers requis
    missing_files = [file for file in required_files if not os.path.exists(os.path.join(DATA_PATH, file))]

    if missing_files:
        raise Exception(f"Les fichiers suivants sont manquants : {', '.join(missing_files)}")

    required_env_vars = ['AZURE_DB_HOST', 'AZURE_DB_PORT', 'AZURE_DB_USER', 'AZURE_PG_PASSWORD', 'AZURE_DB_NAME']
    missing_env_vars = [var for var in required_env_vars if var not in os.environ]

    if missing_env_vars:
        raise Exception(f"Les variables d'environnement suivantes ne sont pas déclarées : {', '.join(missing_env_vars)}")
    else:
        print("Vérification de l'environnement réussie.")


def ademe_api():
    # Obtenir les données de l'API Ademe pour les logements neufs
    url = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-v2-logements-neufs/lines"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception si la réponse n'est pas réussie (ex: code de statut HTTP 4xx ou 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Gérer l'erreur de requête (par exemple, imprimer un message d'erreur ou enregistrer dans les journaux)
        print(f"Erreur lors de la requête à l'API Ademe : {e}")
        return None  # Retourner None pour indiquer une réponse vide ou invalide


def process_results(**kwargs):
    # Traiter les résultats pour obtenir l'URL suivante ou les données à insérer dans la base de données
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='ademe_api')

    if data is not None:
        next_url = data.get('next')  # Utilisez get() pour obtenir la valeur de la clé 'next' ou None si la clé n'existe pas
        # Vous pouvez également traiter les données ici pour les préparer à être insérées dans la base de données
        return next_url
    else:
        # Gérer le cas où les données ne sont pas disponibles (par exemple, imprimer un message d'avertissement ou enregistrer dans les journaux)
        print("Aucune donnée disponible pour traiter.")
        return None

def save_postgresdb(**kwargs):
    # Charger les données dans la base de données PostgreSQL
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='ademe_api')
    records = data['records']

    # Prétraitement des données avant insertion dans la base de données
    df = pd.DataFrame(records)
    # Dump des échantillons au format json en gardant seulement la colonne 'n_dpe' comme demandé
    df_json = df['fields'].apply(json.dumps).tolist()

    # Connexion à la base de données PostgreSQL à partir des variables d'environnement Azure
    postgres_host = os.environ.get('AZURE_DB_HOST')
    postgres_port = os.environ.get('AZURE_DB_PORT')
    postgres_user = os.environ.get('AZURE_DB_USER')
    postgres_password = os.environ.get('AZURE_PG_PASSWORD')
    postgres_database = os.environ.get('AZURE_DB_NAME')

    try:
        conn = psycopg2.connect(
            host=postgres_host,
            port=postgres_port,
            user=postgres_user,
            password=postgres_password,
            database=postgres_database
        )
        cursor = conn.cursor()

        # Insertion des données dans la base de données PostgreSQL
        # Exemple de code pour l'insertion dans la base de données
        # Remplacez cela par votre propre code pour insérer les données
        for json_data in df_json:
            cursor.execute("INSERT INTO dpe_logement (data) VALUES (%s)", (json_data,))

        conn.commit()
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        # Gérer les erreurs de connexion ou d'insertion dans la base de données
        print(f"Erreur lors de l'insertion des données dans PostgreSQL : {e}")

def drop_duplicates():
    # Supprimer les doublons dans la base de données vis-à-vis de n_dpe
    # Connexion à la base de données PostgreSQL à partir des variables d'environnement Azure
    postgres_host = os.environ.get('AZURE_DB_HOST')
    postgres_port = os.environ.get('AZURE_DB_PORT')
    postgres_user = os.environ.get('AZURE_DB_USER')
    postgres_password = os.environ.get('AZURE_PG_PASSWORD')
    postgres_database = os.environ.get('AZURE_DB_NAME')

    try:
        conn = psycopg2.connect(
            host=postgres_host,
            port=postgres_port,
            user=postgres_user,
            password=postgres_password,
            database=postgres_database
        )
        cursor = conn.cursor()

        # Exécuter la requête SQL pour supprimer les doublons dans la table en utilisant n_dpe comme critère
        # Assurez-vous de remplacer "nom_table" par le nom réel de votre table
        cursor.execute("""
            DELETE FROM nom_table
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM dpe_tertiaire
                GROUP BY n_dpe
            )
        """)

        conn.commit()
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        # Gérer les erreurs de connexion ou d'exécution de la requête SQL
        print(f"Erreur lors de la suppression des doublons dans PostgreSQL : {e}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'load_data',
    default_args=default_args,
    description='DAG pour charger les données depuis l\'API Ademe pour les logements neufs',
    schedule_interval='@daily',
)

check_environment_setup_task = PythonOperator(
    task_id='check_environment_setup',
    python_callable=check_environment_setup,
    dag=dag,
)

ademe_api_task = PythonOperator(
    task_id='ademe_api',
    python_callable=ademe_api,
    dag=dag,
)

process_results_task = PythonOperator(
    task_id='process_results',
    python_callable=process_results,
    provide_context=True,
    dag=dag,
)

save_postgresdb_task = PythonOperator(
    task_id='save_postgresdb',
    python_callable=save_postgresdb,
    provide_context=True,
    dag=dag,
)

drop_duplicates_task = PythonOperator(
    task_id='drop_duplicates',
    python_callable=drop_duplicates,
    dag=dag,
)

check_environment_setup_task >> ademe_api_task >> process_results_task >> save_postgresdb_task >> drop_duplicates_task

