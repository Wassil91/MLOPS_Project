from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import psycopg2
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

def model_training():
    # Connectez-vous à la base de données PostgreSQL pour récupérer les données d'entraînement
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
    
    # Exemple de récupération des données pour l'entraînement du modèle
    cursor.execute("""
        SELECT n_dpe, surface, promotion
        FROM dpe_logement 
        WHERE processed = true
    """)
    data = cursor.fetchall()
    
    # Divisez les données en variables prédictives (X) et variable cible (y)
    X = [row[:-1] for row in data]
    y = [row[-1] for row in data]
    
    # Divisez les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialisez et entraînez le modèle de forêt aléatoire
    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Logguer les paramètres du modèle
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)
        
        # Évaluer le modèle
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)
        
        # Logguer la métrique d'exactitude
        mlflow.log_metric("accuracy", accuracy)
        
        # Enregistrer le modèle dans MLflow
        mlflow.sklearn.log_model(model, "model")

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

dag_model_training = DAG(
    'model_training',
    default_args=default_args,
    description='DAG pour l\'entraînement du modèle de promotion des logements neufs',
    schedule_interval='@weekly',  # Par exemple, une fois par semaine
)

model_training_task = PythonOperator(
    task_id='model_training_task',
    python_callable=model_training,
    dag=dag_model_training,
)

