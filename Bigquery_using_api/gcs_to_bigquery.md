# GCS to BigQuery Pipeline

## Table of Contents
1. [GCS Ingestion](#gcs-ingestion)
2. [Data Transformation](#data-transformation)
3. [Load Data to BigQuery (SQL)](#load-data-to-bigquery-sql)
4. [Load Data to BigQuery (Python)](#load-data-to-bigquery-python)


This is the DAG diagram or tree structure of the pipeline

![gcs_to_bigquery](../images/gcs_to_bigquery.png)

## 1. GCS Ingestion <a name="gcs-ingestion"></a>

### Description
This step involves ingesting data from Google Cloud Storage (GCS) using a Python script.

### Script Location
[gcs_data_load.py](./gcs_data_load.py)

### Execution
```bash
python C:\Users\DELL\Desktop\projects\Datapipeline-Mage-GCP-Postgres\mage-magic\data_loaders\gcs_data_load.py
```

---

## 2. Data Transformation <a name="data-transformation"></a>

### Description
Transform the ingested data using a Python script with specific processing.

### Script Location
[transform_staged_data.py](./transfomr_staged_data.py)

### Execution
```bash
python C:\Users\DELL\Desktop\projects\Datapipeline-Mage-GCP-Postgres\mage-magic\transformers\tranform_staged_data.py
```

---

## 3. Load Data to BigQuery (SQL) <a name="load-data-to-bigquery-sql"></a>

### Description
Load the processed data into BigQuery using a SQL script.

### Script Location
[write_sql_to_bigquery.py](./write_sql_to_bigquery.sql)

### Execution
```bash
python C:\Users\DELL\Desktop\projects\Datapipeline-Mage-GCP-Postgres\mage-magic\data_exporters\write_sql_to_bigquery.py
```

---

## 4. Load Data to BigQuery (Python) <a name="load-data-to-bigquery-python"></a>

### Description
Load the processed data into BigQuery using a Python script.

### Script Location
[export_data_to_bigquery.py](./export_data_to_bigquery.py)

### Execution
```bash
python C:\Users\DELL\Desktop\projects\Datapipeline-Mage-GCP-Postgres\mage-magic\data_exporters\export_data_to_bigquery.py
```

---

**Note:** Ensure that all required dependencies are installed, and appropriate access credentials are set up for GCS data ingestion and BigQuery data export.

