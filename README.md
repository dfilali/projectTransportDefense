# 🚆 Urban Mobility Intelligence Platform

## 🎯 Business Context

Urban transport systems are increasingly complex and vulnerable to disruptions (delays, incidents, congestion, infrastructure failures).

The objective of this project is to design a **data-driven intelligence system** capable of:
- analyzing urban mobility data
- detecting disruption patterns
- simulating transport scenarios
- supporting decision-making for mobility optimization

This project demonstrates a **Data Engineering + Machine Learning pipeline applied to real-world mobility challenges**.

---

## 🧠 Key Objectives

- Ingest and process urban transport data (GTFS / open data sources)
- Build a scalable data pipeline for analytics
- Engineer meaningful mobility features
- Apply machine learning models for prediction and analysis
- Provide insights for operational decision-making

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


---

## ⚙️ Tech Stack

**Data Engineering**
- Python
- Apache Spark
- Pandas

**Machine Learning**
- Scikit-learn
- NumPy
- Model evaluation metrics (precision, recall, F1-score)

**Data Processing**
- ETL pipelines
- Feature engineering
- Data cleaning & preprocessing

**Visualization (optional depending on your implementation)**
- Kepler.gl
- Matplotlib / Seaborn

---

## 📊 Key Features

- End-to-end data pipeline for mobility data
- Data cleaning and transformation at scale
- Feature engineering for transport behavior analysis
- Predictive modeling for mobility patterns
- Scenario-based analysis of transport disruptions

---

## 📈 Business Impact

This project demonstrates how data can be leveraged to:

- Improve **transport operational efficiency**
- Reduce **analysis and decision-making time**
- Support **data-driven urban planning**
- Identify **critical disruption patterns in mobility systems**

---

## 🧪 Machine Learning Approach

Depending on the implementation:

- Supervised learning for prediction tasks
- Clustering for mobility pattern segmentation
- Time-series analysis for demand / traffic trends

Evaluation metrics:
- Accuracy
- Precision / Recall
- F1-score
- ROC-AUC (if applicable)

---

## 🚀 How to Run the Project

```bash
# Clone repository
git clone https://github.com/dfilali/projectTransportDefense.git

# Navigate to project
cd projectTransportDefense

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run main pipeline (Extract, Process & Validate)
python main.py

# Run the Streamlit Dashboard
streamlit run app/dash_app/app.py
```

---

## 📁 Project Structure

```text
projectTransportDefense/
│
├── main.py                    # Main pipeline entry point
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
│
├── pipelines/
│   └── main_pipeline.py       # Orchestrates the ETL data steps
│
├── src/                       # Core Data Engineering codebase
│   ├── configuration/         # Configuration & API endpoints
│   ├── utils/                 # Data lake connectors & logger
│   ├── data_extraction/       # API ingestion (RATP, IDFM, weather)
│   ├── data_processing/       # Refinement scripts (Parquet conversion)
│   ├── models/                # ML models (traffic, weather impact)
│   └── automation/            # Scheduler service (run_extract.py)
│
├── app/
│   └── dash_app/              # Streamlit web application
│       ├── app.py             # Dashboard main script
│       └── components/        # Isolated map and status widgets
│
└── data/
    └── data_static_extraction/# Static datasets & ingestion scripts
```