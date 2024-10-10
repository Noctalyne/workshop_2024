# **Bracelet Connecté pour la Prévention chez les Personnes Âgées et autres**

## **Description du projet**

Ce projet consiste à développer une application web en Django pour le suivi et la surveillance en temps réel des personnes âgées ou vulnérables via un bracelet connecté. Ce bracelet détecte les chutes, les comportements anormaux, et envoie des alertes aux proches ou aux services médicaux.

Le système inclut un suivi médical à travers une API, intégrant des données de santé en temps réel dans le dossier médical électronique du patient. Le bracelet, conçu en **silicone médical**, possède des fonctions d'alerte (**sonore**, **vibration**, **lumière SOS**) et une aide **vocale intégrée**.

## **Fonctionnalités principales**

1. **Détection de chutes** avec envoi automatique d'alertes.
2. **Géolocalisation** de la personne en cas d'incident.
3. **Suivi en temps réel** via une application web par les proches ou le médecin.
4. **Intégration avec services médicaux** pour partage des données avec le dossier médical.
5. **Alerte sonore, vibration et lumière SOS** sur le bracelet.
6. **Aide vocale** avec micro intégré.

## **Prérequis**

- Python 3.x
- Django 4.x
- Docker (facultatif pour la virtualisation)
- Une API de suivi médical (API gouvernementale ou privée)
- Un environnement Python pour le traitement des données (analyse et envoi)

## **Installation de l'environnement**

1. **Cloner le dépôt**  

```bash
   git clone https://gitlab.com/b38425543/workshop2024.git
   cd workshop2024
 ```

2. **Installer les dépendances**

**Utilisez un environnement virtuel Python :** 

```bash
    python -m venv env
    source env/bin/activate  # Linux/Mac
    env\Scripts\activate     # Windows
    pip install -r requirements.txt
```
   
3. **Configurer l'application**

Créez un fichier .env en vous basant sur le fichier env.example pour ajouter vos variables d'environnement (clés API, configuration base de données, etc.).

4. **Migrer la base de données**

```bash
    python manage.py migrate
```

5. **Charger les données de test**

```bash
    python manage.py loaddata fixtures.json
```

6. **Lancer le serveur de développement**

```bash
    python manage.py runserver
```

7. **Démarrer le bracelet**

- Pour simuler le fonctionnement du bracelet connecté, un script Python est fourni. Il envoie des données à l'API à partir de capteurs simulés.

```bash
    python bracelet_simulation.py
```

## **Installation via Docker**

Pour installer et lancer l'application avec Docker, exécutez la commande suivante :

```bash
    docker-compose up
```

## **Structure du projet**

```
    ├── bracelet_simulation.py   # Script de simulation des données du bracelet
    ├── core/                    # Contient la logique métier de l'application Django
    ├── api/                     # Gestion des requêtes API pour l'envoi des données médicales
    ├── static/                  # Fichiers statiques (images, logos)
    ├── templates/               # Fichiers HTML pour l'interface web
    └── README.md                # Ce fichier
```


## **Utilisation**

Une fois l'application lancée, accédez à l'interface web à l'adresse ```http://localhost:8000.``` Vous pouvez y créer un compte pour un proche ou un médecin, voir les données de santé en temps réel et configurer les notifications d'alerte.