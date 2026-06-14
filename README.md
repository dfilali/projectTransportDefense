# La Défense Mobility Platform

> Smart Mobility Analytics powered by AI, Open Data & Big Data Technologies

Une plateforme intelligente dédiée à l’optimisation de la mobilité urbaine à La Défense, premier quartier d’affaires d’Europe. Le projet exploite des données ouvertes, des API temps réel et des modèles d’intelligence artificielle afin de fournir des analyses avancées, des prédictions de trafic et des recommandations de déplacement.

---

## Contexte

La Défense accueille chaque jour plusieurs centaines de milliers de voyageurs utilisant différents moyens de transport :

- Métro  
- RER  
- Tramway  
- Bus  
- Mobilités douces  
- Véhicules particuliers  

Cette forte concentration génère régulièrement :

- des congestions de trafic  
- des retards de transport  
- une augmentation des émissions de CO₂  
- une dégradation de l’expérience utilisateur  

L’objectif de ce projet est de mettre la Data Science, l’Intelligence Artificielle et les Open Data au service d’une mobilité plus fluide, plus intelligente et plus durable.

---

## Fonctionnalités

### Dashboard interactif

Visualisation en temps réel :

- Conditions de circulation  
- État du trafic routier  
- Conditions météorologiques  
- Informations transports publics  
- Indicateurs environnementaux  

---

### Prédiction du trafic

Utilisation de modèles de Machine Learning permettant de :

- anticiper les périodes de congestion  
- identifier les zones à risque  
- prévoir les évolutions du trafic selon les conditions météo et horaires  

---

### Recommandation d’itinéraires

Proposition d’itinéraires intelligents en fonction :

- du trafic actuel  
- des perturbations des transports  
- des conditions météorologiques  
- de l’impact environnemental  

---

### Analyse environnementale

Évaluation des différents modes de transport selon :

- les émissions de CO₂  
- le temps de trajet  
- l’efficacité énergétique  

---

### Intégration multi-sources

Le projet centralise et exploite plusieurs sources de données :

- TomTom Traffic API  
- Visual Crossing Weather API  
- RATP Open Data  
- Données géographiques ouvertes  

---

## Architecture du projet

```text
                ┌───────────────────┐
                │   External APIs   │
                │  RATP / TomTom /  │
                │  Weather API      │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Data Extraction   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Data Processing   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Data Lake (MinIO) │
                └─────────┬─────────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
   ┌────────────────┐         ┌────────────────┐
   │ Machine        │         │ Analytics      │
   │ Learning       │         │ & Reporting    │
   └────────┬───────┘         └───────┬────────┘
            │                         │
            └─────────────┬───────────┘
                          ▼
                ┌───────────────────┐
                │ Streamlit App     │
                └───────────────────┘
```


## Structure du projet :

```
ladefense-mobility/
│
├── data_extraction/
├── data_processing/
├── models/
├── dash_app/
├── automation/
├── config/
├── utils/
│
├── requirements.txt
├── README.md
└── .env
## Stack technique

### Data Engineering
- Python  
- Pandas  
- Requests  
- MinIO  

### Data Science & AI
- Scikit-Learn  
- NumPy  
- Machine Learning  

### Visualisation
- Streamlit  
- Plotly  

### Infrastructure
- Docker  
- MinIO Data Lake  

### Data Sources
- RATP API  
- TomTom Traffic API  
- Visual Crossing Weather API  

---

## Prérequis

- Python 3.8+  
- Docker  
- API Keys :
  - Visual Crossing Weather API  
  - TomTom Traffic API  
  - RATP API  

---

## Installation

1. Cloner le projet
git clone https://github.com/votre-organisation/ladefense-mobility.git
cd ladefense-mobility

2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate

Sur Windows :

venv\Scripts\activate
3. Installer les dépendances
pip install -r requirements.txt
4. Variables d’environnement

Créer un fichier .env :

WEATHER_API_KEY=xxxxxxxx
TOMTOM_API_KEY=xxxxxxxx
RATP_API_KEY=xxxxxxxx
5. Lancer MinIO
docker run -d \
-p 9000:9000 \
-p 9001:9001 \
-v ~/data-lake-ladefense:/data \
minio/minio server /data \
--console-address ":9001"
6. Initialiser le Data Lake
python automation/init_data_lake.py
7. Lancer l’extraction des données
python automation/run_extract.py
8. Lancer le dashboard
streamlit run dash_app/app.py

---

## Cas d’usage

- Prévision du trafic urbain
- Analyse des flux de mobilité
- Optimisation des déplacements
- Aide à la décision
- Smart City Analytics
- Réduction de l’empreinte carbone

---

## Perspectives

- Airflow orchestration
- Data Warehouse PostgreSQL
- Déploiement Cloud (AWS / GCP)
- Modèles avancés (XGBoost, LightGBM)
- Cartographie (Kepler.gl)
- Analyse prédictive des incidents