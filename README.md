### TEAM Project

Wassil Fahem, David Dumanoir, Antoine Poivet, Yanis Hamdaoui

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
Une fois les conteneurs démarrés, accédez à l'interface web Airflow via votre navigateur Web à l'adresse http://localhost:8080 (à la place de localhost utilisez votre adresse IP de votre VM Azure). Accédez également à l'interface web de mlflow à l'adresse http://localhost:5001 (à la place de localhost utilisez votre adresse IP de votre VM Azure). Veillez également à mettre les bons ports. Vous pouvez utiliser les DAGs fournis pour exécuter les différentes étapes du pipeline MLops qui seront visibles sur l'interface de Airflow.

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

## Démonstration des étapes du projet 

### Source de données :

![SourcedataAPI_DPE](https://media.discordapp.net/attachments/1240357804846616749/1240376079995375797/image.png?ex=664655be&is=6645043e&hm=b11332daaa195993de6215637e01e1b19494a8d330134734bf081b7d7c21e968&=&format=webp&quality=lossless&width=1316&height=662)

### VM Azure :
![VM Azure](https://media.discordapp.net/attachments/1240357804846616749/1240366767784726629/image.png?ex=66464d12&is=6644fb92&hm=41d2b00800f180f41e2748602fdc4f8a59f1e093623ede24e021baaf02ecfa7d&=&format=webp&quality=lossless&width=1311&height=662)

### Paramètre réseau de la VM :
![ParamReseauVM](https://media.discordapp.net/attachments/1240357804846616749/1240366962924716142/image.png?ex=66464d40&is=6644fbc0&hm=eb4575d39321f24720e638e2157fa11af32e5468e33c8aa51ee7e572ebcd511c&=&format=webp&quality=lossless&width=1316&height=662)

### Stockage de la clé .pem :

![StockageKey](https://media.discordapp.net/attachments/1240357804846616749/1240369122035105842/image.png?ex=66464f43&is=6644fdc3&hm=3e3f4a67d5401c449f083d5ab5b11798d787cf1a06f2c12cce6814e4e03e7d68&=&format=webp&quality=lossless&width=1062&height=472)

### Création de la base de données Postgre sur Azure :

![bddPostgreAzure](https://media.discordapp.net/attachments/1240357804846616749/1240367818545954887/image.png?ex=66464e0c&is=6644fc8c&hm=36716f80e32e3c438867e762099e84484d51594e05e59b6e322603399e691f1e&=&format=webp&quality=lossless&width=1333&height=662)

### Connexion à la VM Azure :

![ConnexionVM](https://media.discordapp.net/attachments/1240357804846616749/1240368868896280687/image.png?ex=66464f07&is=6644fd87&hm=a6f84c0c4ae31cd6229399afb08af8c3ef83446e0c1783f60806b02773a7d747&=&format=webp&quality=lossless&width=843&height=662)

### Stockage projet dans la VM :

![StockageVMprojet](https://media.discordapp.net/attachments/1240357804846616749/1240369429779583046/image.png?ex=66464f8d&is=6644fe0d&hm=6bdfa5a3fec76bd3e69cd52929a9eed2af80e0c4dabaeadb6121111f110406e0&=&format=webp&quality=lossless&width=1440&height=76)

### Stockage variables d'environnement dans la VM :

![stockVarEnv](https://media.discordapp.net/attachments/1240357804846616749/1240372158463610880/image.png?ex=66465217&is=66450097&hm=573678c43ee5a8c2c9c3ca1dad5a60b464cffd391bf1bcd228d95e43ebbb3587&=&format=webp&quality=lossless&width=826&height=33)
![suite](https://media.discordapp.net/attachments/1240357804846616749/1240373059018559519/image.png?ex=664652ee&is=6645016e&hm=b00e245f1e6afea04b5905d609f742fc7d14e2fcbe36b40e0a8b6eeaa019c4b8&=&format=webp&quality=lossless&width=1440&height=188)


### Lancement du projet :

![lancementProjetVM](https://media.discordapp.net/attachments/1240357804846616749/1240371184890286100/image.png?ex=6646512f&is=6644ffaf&hm=884c3197475d872b4b03c8ab0cad18c24aecb79e7c106e92159fd61a451fb722&=&format=webp&quality=lossless&width=1411&height=662)

### Vérification lancement projet :

![verifilancementprojet](https://media.discordapp.net/attachments/1240357804846616749/1240371298870497280/image.png?ex=6646514a&is=6644ffca&hm=b146bd5c205e3d23fa1ae4eb813cfb180f165dcb9fd697e88fc33aa6c6bcb95c&=&format=webp&quality=lossless&width=687&height=346)

### Vérification interface web Mlflow :

![UAmlflow](https://media.discordapp.net/attachments/1240357804846616749/1240371433486418100/image.png?ex=6646516a&is=6644ffea&hm=f42a0e913767128d683c4ea07cfcc20e49963a12631917aa51c7724d9b6a5983&=&format=webp&quality=lossless&width=1306&height=662)

### Vérification interface web Airflow :

![UAAirflow](https://media.discordapp.net/attachments/1240357804846616749/1240395058562203668/image.png?ex=6646676b&is=664515eb&hm=d9d0165d57fc9cb317da4991ab8973c1bfbb9d97af975b1da07374c2f2e7696e&=&format=webp&quality=lossless&width=687&height=351)

### Liste des variables dans Airflow :

![VariablesAirflowUA](https://media.discordapp.net/attachments/1240357804846616749/1240371765293744413/image.png?ex=664651b9&is=66450039&hm=4f57aa6c2fe9daeec729afa65f4169efa97b7b2091d76e389bbeb5220d5b9fd3&=&format=webp&quality=lossless&width=1302&height=662)



## Problème et bugs

Nous avons rencontrés pas mal de problème et malheureusemennt notre projet n'est pas terminé à 100%. Ce qu'il manque :
 - Faire fonctionner les dags sur airfflow
 - Stocker les données récuperer de l'API dans les tables de la base postgres via le dag load_data
 - Affichage modèle dans Mlflow

## Licence

Pour réaliser ce projet il est nécessaire d'avoir des crédits sur Azure, nous en avons eu grâce à notre abonnement scolaire. Veillez à bien choisir les environnements de Développement sur Azure pour éviter de consommer trop de credits.
