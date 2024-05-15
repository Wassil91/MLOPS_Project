# Projet MLops - Airflow
Ce projet vise à mettre en œuvre un pipeline MLops complet utilisant Apache Airflow pour l'orchestration, MLflow pour le suivi des modèles, et PostgreSQL pour la gestion des données. Le pipeline est conçu pour prédire l'étiquette GES des logements neufs à partir du dataset de l'ADEME.

# Structure du projet
Le projet est organisé comme suit :

dags/ : Contient les DAGs Airflow pour l'extraction, la transformation, l'entraînement et le déploiement des modèles.
config/ : Contient les fichiers de configuration pour Airflow.
logs/ : Répertoire pour les logs Airflow.
plugins/ : Plugins Airflow personnalisés.
requirements.txt : Fichier de dépendances Python.
Makefile : Makefile pour l'installation et le formatage du code.
docker-compose.yml : Configuration Docker Compose pour Airflow, MLflow et PostgreSQL.
Dockerfile.airflow : Dockerfile pour l'image Airflow.
Dockerfile.mlflow : Dockerfile pour l'image MLflow.

# Installation et configuration
Clonez ce référentiel vers votre machine locale ou votre VM Azure.
Assurez-vous que Docker et Docker Compose sont installés.
Exécutez make install pour installer les dépendances.
Mettez en place les variables d'environnement requises dans config/airflow.env.
Exécutez docker-compose up -d pour démarrer les conteneurs.

# Utilisation
Une fois les conteneurs démarrés, accédez à l'interface Airflow via votre navigateur Web à l'adresse http://localhost:8080. Vous pouvez utiliser les DAGs fournis pour exécuter les différentes étapes du pipeline MLops.

# Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez ouvrir une pull request avec vos modifications.

# Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
