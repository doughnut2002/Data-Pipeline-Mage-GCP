
# API to Postgres Pipeline

## Table of Contents
1. [API Ingestion](#api-ingestion)
2. [Data Transformation](#data-transformation)
3. [Load Data to Postgres](#load-data-to-postgres)
4. [Check Data in Postgres using Test Block](#check-data-in-postgres)

This is the DAG diagram or tree structure of the pipeline

![api_to_postgres](../images/api_to_postgres_tree.png)

## 1. API Ingestion <a name="api-ingestion"></a>

### Description
This step involves ingesting data from an API using a Python script.

### Script Location 
[api_data_load.py](./api_data_load.py)

### Execution
```bash
python C:\Users\DELL\Desktop\projects\Datapipeline-Mage-GCP-Postgres\mage-magic\data_loaders\api_data_load.py
```

---

## 2. Data Transformation <a name="data-transformation"></a>

### Description
Transform the ingested data using a Python script with specific processing.

### Script Location
[transform_data.py](./tranform_data.py)

### Execution
```bash
python C:\Users\DELL\Desktop\projects\Datapipeline-Mage-GCP-Postgres\mage-magic\transformers\tranform_data.py
```

---

## 3. Load Data to Postgres <a name="load-data-to-postgres"></a>

### Description
Load the processed data into a Postgres database using a Python script.

### Script Location
[data_loader_to_postgres.py](./data_loader_to_postgres.pyy)

### Execution
```bash
python C:\Users\DELL\Desktop\projects\Datapipeline-Mage-GCP-Postgres\mage-magic\data_exporters\data_loader_to_postgres.py
```

---

## 4. Check Data in Postgres using Test Block <a name="check-data-in-postgres"></a>

### Description
Verify whether the data has been successfully uploaded to the Postgres database using a test block.

### Script Location
[data_load_test.sql](../mage-magic/data_loaders/data_load_test.sql)

---

**Note:** Ensure that all required dependencies are installed, and appropriate access credentials are set up for API ingestion and Postgres data export.
