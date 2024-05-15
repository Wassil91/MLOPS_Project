# Projet MLops - Airflow sur Azure
Ce projet vise à mettre en œuvre un pipeline MLops complet utilisant Apache Airflow pour l'orchestration, MLflow pour le suivi des modèles, et PostgreSQL pour la gestion des données via une VM Azure. Le pipeline est conçu pour prédire l'étiquette GES des logements neufs à partir du dataset de l'ADEME.

## Structure du projet
Le projet est organisé comme suit :

- dags/ : Contient les DAGs Airflow pour l'extraction, la transformation, l'entraînement et le déploiement des modèles.
- config/ : Contient les fichiers de configuration pour Airflow.
- logs/ : Répertoire pour les logs Airflow.
- plugins/ : Plugins Airflow personnalisés.
- requirements.txt : Fichier de dépendances Python.
- Makefile : Makefile pour l'installation et le formatage du code.
- docker-compose.yml : Configuration Docker Compose pour Airflow, MLflow et PostgreSQL.
- Dockerfile.airflow : Dockerfile pour l'image Airflow.
- Dockerfile.mlflow : Dockerfile pour l'image MLflow.

## Arborescence du projet sur la VM

- airflow
  - Dockerfile.airflow
  - Dockerfile.mlflow
  - Makefile
  - config
  - dags
    - __pycache__
    - load_data.py
    - model_trainning.py
    - transform_data.py
  - docker-compose.yml
  - logs
  - plugins
  - requirements.txt

## Installation et configuration
Clonez ce référentiel vers votre machine locale ou votre VM Azure.
Assurez-vous que Docker et Docker Compose sont installés.
Exécutez make install pour installer les dépendances.
Mettez en place les variables d'environnement requises dans config/airflow.env.
Exécutez docker-compose up -d pour démarrer les conteneurs.

## Utilisation
Une fois les conteneurs démarrés, accédez à l'interface Airflow via votre navigateur Web à l'adresse http://localhost:8080. Vous pouvez utiliser les DAGs fournis pour exécuter les différentes étapes du pipeline MLops.

## Organisation et création de la VM Azure
Pour créer et organiser une VM Azure pour ce projet, suivez les étapes suivantes :

### Création de la VM Azure :

Connectez-vous au portail Azure.
Cliquez sur "Créer une ressource" > "Machine virtuelle".
Suivez les étapes du processus de création de la machine virtuelle en spécifiant la configuration appropriée, y compris le type de machine, le système d'exploitation, le réseau, etc.
Assurez-vous de définir un nom de groupe de ressources significatif pour organiser vos ressources Azure.
Une fois la VM créée, notez son adresse IP publique pour y accéder.

### Configuration de la sécurité :

Utilisez les fonctionnalités de sécurité Azure pour restreindre l'accès à votre VM en fonction de vos besoins. Par exemple, vous pouvez configurer les règles du groupe de sécurité réseau pour autoriser l'accès SSH uniquement à partir d'adresses IP spécifiques.

### Connexion à la VM Azure :

Utilisez un client SSH tel que PuTTY (Windows) ou la commande ssh (Linux/macOS) pour vous connecter à la VM Azure en utilisant son adresse IP publique.
Une fois connecté, vous pouvez commencer à travailler sur votre projet MLops.

## Création du Serveur PostgreSQL sur Azure
La mise en place d'un serveur PostgreSQL sur Azure permet de stocker et de gérer les données de manière sécurisée et évolutive. Voici les étapes à suivre pour créer un serveur PostgreSQL sur Azure :

### Connexion au Portail Azure :

Connectez-vous au Portail Azure à l'aide de vos identifiants.

### Création d'une Ressource :

Cliquez sur le bouton "+ Créer une ressource" dans le menu de navigation.
Recherchez "PostgreSQL" dans la barre de recherche et sélectionnez "Azure Database for PostgreSQL" dans les résultats.

### Configuration du Serveur PostgreSQL :

Remplissez les détails requis tels que l'abonnement, le groupe de ressources, et le nom du serveur.
Choisissez la version de PostgreSQL et la région de déploiement selon vos besoins.

### Configuration de la Sécurité :

Configurez les paramètres de sécurité comme le nom d'utilisateur et le mot de passe pour l'accès au serveur.
Choisissez le type d'authentification approprié, tel que l'authentification basée sur Azure Active Directory ou l'authentification basée sur le serveur.

### Options de Configuration Additionnelles :

Configurez les options supplémentaires telles que la taille de la base de données, les sauvegardes automatiques, et les règles de pare-feu.

### Validation et Déploiement :

Passez en revue les détails de la configuration pour vous assurer qu'ils sont corrects.
Cliquez sur "Vérifier + Créer" pour valider la configuration.
Une fois la validation réussie, cliquez sur "Créer" pour déployer le serveur PostgreSQL sur Azure.

### Accès au Serveur PostgreSQL :

Une fois le déploiement terminé, accédez au serveur PostgreSQL via l'adresse et les informations d'identification fournies lors de la configuration.
Vous pouvez utiliser des outils tels que pgAdmin ou psql pour vous connecter à votre serveur et commencer à gérer vos bases de données.

## Problème et bugs


## Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails. Pour réaliser ce projet il est nécessaire d'avoir des crédits sur Azure, nous en avons eu grâce à notre abonnement scolaire.
