## Résumé

Site web d'Orange County Lettings

## Développement local

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

---
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




---

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
---
### Accès à l'application :
**Local :**  
Pour un déploiement en local via le code source ou l'image docker, veillez à renseigner les variables d'environnement suivantes :
```text
SECRET_KEY=valeur_de_la_clé_secrète_django
SENTRY_DSN=valeur_de_la_clé_sentry_dsn
```

**Docker :** 

Vous pouvez par exemple placer les deux lignes ci-dessus dans un fichier `env_file` à la racine de votre projet pour exécuter l'image docker de la manière suivante :
```bash
docker pull <docker_image:tag>
docker run --env-file=env_file -i -p 8000:8000 <docker_image>
```

`docker_image` : accédez à la dernière image créée en utilisant le tag "latest", ou bien choisissez une image antérieure en utilisant le "hash" du commit CircleCi correspondant. 

**Heroky :** 

https://oc-lettings-27.herokuapp.com/
