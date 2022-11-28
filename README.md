<h3 align="center">
    <img alt="Logo" title="#logo" width="250px" src="/assets/16004295603423_P11.png">
    <br>
</h3>


# OpenClassrooms Projet P13

- [Objectif](#obj)
- [Compétences](#competences)
- [Technologies](#techs)
- [Requirements](#reqs)
- [Architecture](#architecture)
- [Configuration locale](#localconfig)
- [Déploiement](#deployment)
- [Présentation](#presentation)

<a id="obj"></a>
## Objectif

Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis.
L'objectif de ce projet est de faire évoluer le site web éxistant (repository GitHub : [OC Lettings](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR)) sur les points suivants :
- Réduction de diverses dettes techniques sur le projet 
- Refonte de l'architecture modulaire 
- Ajout d'un pipeline CI/CD utilisant CircleCI et Heroku 
- Surveillance de l’application et suivi des erreurs via Sentry.

<a id="competences"></a>
## Compétences acquises
- Gérer la production de code en utilisant la méthodologie CI/CD avec CircleCI
- Appliquer une architecture modulaire dans une application Python
- Mettre en place un système de contrôle des codes en utilisant Sentry
- Déployer une application en utilisant Heroku
- Refactoriser une application pour réduire la dette technique

<a id="techs"></a>
## Technologies Utilisées
- [Python3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Gunicorn](https://gunicorn.org/)
- [Sqlite](https://www.sqlite.org/)
- [HTML](https://developer.mozilla.org/fr/docs/Web/HTML)
- [Docker](https://www.docker.com/)
- [CircleCI](https://circleci.com/)
- [Heroku](https://www.heroku.com/)
- [Sentry](https://sentry.io/)
- [Pytest-django](https://pytest-django.readthedocs.io/)
- [Flake8](https://flake8.pycqa.org/)

<a id="reqs"></a>
## Requirements
- django
- gunicorn
- sentry-sdk
- pytest-django
- flake8
- python-dotenv
- whitenoise

<a id="architecture"></a>
## Architecture et répertoires
```
Project
├── oc_lettings_site
│   ├── lettings : application pour les locations
│   ├── profiles : application pour les profiles utilisateurs
│   ├── web_site : application pour le site web
│   ├── settings.py : fichier de réglages django
│   ├── urls.py : fichier principal des endpoints
│   ├── ..
|── staticfiles : fichier statiques pour l'environnement de production
|── manage.py : fichier principal de gestion django
|── oc-lettings-site.sqlite3 : base de données sqlite
|── requirements.txt
|── setup.cfg : fichier de configuration pour flake8 et pytest
|
|── .circleci
│   ├── config.yml : fichier de configuration du pipeline ci/cd
|── .dockerignore
|── Dockerfile : fichier de création de notre image Docker
|── Procfile : ficher de déploiement heroku
```

<a id="localconfig"></a>
## Configuration locale

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

<a id="deployment"></a>
## Déploiement

**Prérequis :**

- Un compte Github
- Un compte CircleCi
- Un compte DockerHub
- Un compte Heroku
- Un compte Sentry

### Description du fonctionnement du Pipeline CircleCi

#### Lors d'un commit sur une branche autre que master, exécution du job suivant :
- `build-and-test` qui est composé des actions (run) suivantes :
  - Run Tests : exécution de tests unitaires via la commande pytest
  - Run Linting PEP8 : exécution du linting via la commande flake8
    
#### Lors d'un commit sur la branche master, exécution des jobs suivants :
   
- `build-and-test` décrit ci-dessus
- `build-docker-push` qui est composé des actions (run) suivantes :
  - Build Docker image : création d'une image docker à partir du code source via Git
  - Push Docker Image : upload de l'image créée vers le Docker Hub en deux temps : d'abord avec le tag correspondant au "hash" de commit CircleCI puis avec le tag "latest"
- `deploy-heroku` composé de l'action (run) suivante :
  - Start container and push to Heroku : lancement du build de l'application sur Heroku via Git
  
#### Workflow :
Le job `build-and-test` est exécuté lors d'une modification apportée sur n'importe quelle branche du projet.

Les jobs `build-docker-push` et `deploy-heroku` ne sont exécutés quant à eux que lors d'une modification apportée sur la branche master.

Le job `build-docker-push` n'est exécuté que lorsque le job `build-and-test` est exécuté avec succès.

Le job `deploy-heroku` n'est exécuté que lorsque le job `build-docker-push` est exécuté avec succès.

### Variables d'environnement :

Création des variables d'environnement au niveau du projet :

| Nom des Variables   | Service  | Description                           |
|---------------------|----------|---------------------------------------|
| `DOCKER_REPOSITORY` | CircleCI | Nom de votre repository Docker        |
| `DOCKER_USERNAME`   | CircleCI | Nom d'utilisateur votre compte Docker |
| `DOCKER_TOKEN`      | CircleCI | Token de votre compte Docker          |
| `HEROKU_API_KEY`    | CircleCI | Clé API de votre compte Heroku        |
| `HEROKU_APP_NAME`   | CircleCI | Nom de l'application Heroku           |
| `SENTRY_DSN`        | Heroku | Token interne d'intégration Sentry    |
| `SECRET_KEY`        | Heroku   | Clé secrete Django                    |
| `ENV`               | Heroku   | Environnement ('production' ou 'dev') |


### Accès à l'application :
**Local :**  
Pour un déploiement en local via le code source ou l'image docker, veillez à renseigner les variables d'environnement suivantes :
```text
SECRET_KEY=valeur_de_la_clé_secrète_django
SENTRY_DSN=valeur_de_la_clé_sentry_dsn
ENV=production
```

**Docker :** 

Vous pouvez par exemple placer les deux lignes ci-dessus dans un fichier `env_file` à la racine de votre projet pour exécuter l'image docker de la manière suivante :
```bash
docker pull <docker_image:tag>
docker run --env-file=env_file -i -p 8000:8000 <docker_image>
```

`docker_image` : accédez à la dernière image créée en utilisant le tag "latest", ou bien choisissez une image antérieure en utilisant le "hash" du commit CircleCi correspondant. 

**Heroku :** 

https://oc-lettings-27.herokuapp.com/

<a id="presentation"></a>
### Présentation

[<img alt="presentation" width="480px" src="/assets/presentation.png">](https://docs.google.com/presentation/d/e/2PACX-1vSOiqDLikxrQPaAu0QaBImoTD0CMJaHlYf4POBRm_IzMTcDZTanlpkW0ZJF6OPBg-BBsqm9KdbmncmC/pub?start=false&loop=false&delayms=5000)
