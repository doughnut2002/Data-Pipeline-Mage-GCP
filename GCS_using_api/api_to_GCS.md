
# Data Pipeline Steps

## Table of Contents
1. [API Ingestion](#api-ingestion)
2. [Data Transformation](#data-transformation)
3. [Load Data to GCS (Parquet)](#load-data-to-gcs-parquet)
4. [Load Data to GCS (Partitioned Parquet)](#load-data-to-gcs-partitioned-parquet)
5. [Incremental Data Load to GCS](#incremental-data-load-to-gcs)


This is the DAG diagram or tree structure of the pipeline

![api_to_gcs](../images/api_to_gcs_tree.png)

## 1. API Ingestion <a name="api-ingestion"></a>

### Description
This step involves ingesting data from an API using a Python script.

### Script Location  [api_data_load.py](./api_data_load.py)

---

## 2. Data Transformation <a name="data-transformation"></a>

### Description
Transform the ingested data using a Python script with specific processing.

### Script Location  [transform_data.py](./tranform_data.py)

---

## 3. Load Data to GCS (Parquet) <a name="load-data-to-gcs-parquet"></a>

### Description
Load the processed data directly into Google Cloud Storage (GCS) in Parquet file format.

### Script Location [load_data_to_gcs_parquet.py](./load_data_to_gcs_parquet.py)

---

## 4. Load Data to GCS (Partitioned Parquet) <a name="load-data-to-gcs-partitioned-parquet"></a>

### Description
Load the processed data into GCS in a partitioned format using PyArrow for improved efficiency.

### Script Location [load_data_to_gcs_parquet.py](./load_data_to_gcs_partitioned_parquet.py)

---

## 5. Incremental Data Load to GCS <a name="incremental-data-load-to-gcs"></a>

### Description
Export data incrementally to GCS using a parameterized execution approach for daily updates.

### Script Location [incremental_data_load_to_gcs.py](./incremental_data_load_to_gcs.py)

---

**Note:** Ensure that all required dependencies are installed, and appropriate access credentials are set up for API ingestion and GCS data export.
