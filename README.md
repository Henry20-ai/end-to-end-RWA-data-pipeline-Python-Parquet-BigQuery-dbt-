# 🚀 End-to-End RWA Data Pipeline: CoinGecko → Parquet → BigQuery → dbt

A modern data pipeline for extracting, storing, and transforming Real-World Asset (RWA) market data using Python, Apache Parquet, Google BigQuery, and dbt Core.

---

## 🏗️ Architecture & Tech Stack

1. Extraction: Python script calling the CoinGecko API to pull market data for major RWA tokens.
2. Storage: Raw response data is normalized and saved locally as compressed Parquet files using pandas and pyarrow.
3. Loading: The Parquet file is uploaded into Google BigQuery for raw storage.
4. Transformation: dbt is used to build staging models and downstream analytical marts with testing for data quality.

---

## 📂 Project Structure

```text
Python Project/
├── .gitignore                  # Ignores local virtual environment and generated artifacts
├── .venv/                      # Local Python environment (ignored)
├── README.md                   # Project overview and setup documentation
├── First script.py             # CoinGecko extraction and Parquet export script
├── rwa_market_data.parquet     # Local raw market snapshot (ignored)
├── my_project/                 # dbt project directory
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_rwa_market.sql
│   │   │   ├── src_rwa.yml
│   │   └── marts/
│   │       ├── rwa_market_mart.sql
│   │       └── schema.yml
│   ├── analyses/
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   └── tests/
├── .dbt/                       # dbt profile and local cache (ignored)
└── .env                        # Local environment variables (ignored)
```

---

## 🧪 Local Setup

1. Create and activate the virtual environment:

```powershell
cd "C:/Users/PC/Pictures/Screenshots/Python Project"
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install pandas pyarrow requests dbt-bigquery
```

3. Run the Python extraction script:

```powershell
python "First script.py"
```

4. Validate the dbt project:

```powershell
cd my_project
.\..\venv\Scripts\Activate.ps1
dbt debug
dbt run
dbt test
```

---

## ☁️ BigQuery Configuration

The dbt project is configured to connect to the Google Cloud project and dataset used for the raw RWA market data.

Required connection details:
- Project ID: n8n-gemini-demo-490307
- Dataset: RWA_dataset

Authentication is done using Google Application Default Credentials (ADC).

---

## ✅ Data Quality

The dbt project includes basic verification for model quality, including:
- unique token IDs
- not-null token IDs
- downstream analytics mart validation

---

## 📝 Notes

This project is intentionally structured so raw extraction, local persistence, BigQuery ingestion, and model transformation remain decoupled and easy to maintain.

It is designed to be extended for additional RWA tokens, enrichment logic, and broader analytics layers.

