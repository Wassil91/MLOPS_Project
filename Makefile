install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C /home/azureuser/airflow/dags/*.py

format:
	black -l 100 /home/azureuser/airflow/dags/*.py

deploy:
	# Ajoutez ici les commandes de déploiement

.PHONY: install lint format deploy
