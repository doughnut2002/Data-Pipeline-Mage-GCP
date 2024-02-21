## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup](#setup)
    - [Clone Repository](#clone-repository)
    - [Copy Environment File](#copy-environment-file)
3. [Docker](#docker)
    - [Build Docker Image](#build-docker-image)
    - [Run Docker Container](#run-docker-container)
    - [Note for Docker on Compute Engine](#note-for-docker-on-compute-engine)
4. [API to PostgreSQL](#api-to-postgresql)
    - [Update io_config.yaml](#update-io-configyaml)
    - [Test Connection](#test-connection)
    - [API to PostgreSQL Steps](#api-to-postgresql-steps)
5. [API to GCS](#api-to-gcs)
    - [Create GCP Bucket](#create-gcp-bucket)
    - [Connect Service Account](#connect-service-account)
    - [Test Connection](#test-connection-1)
    - [API to GCS Steps](#api-to-gcs-steps)
6. [GCS to BigQuery](#gcs-to-bigquery)
    - [GCS to BigQuery Steps](#gcs-to-bigquery-steps)
7. [Mage Deployment](#mage-deployment)
    - [Prerequisites](#prerequisites)
    - [Study Backfills and Topics](#study-backfills-and-topics)

### Project Overview:

![architecture](./images/architecture.png)
(Image credit: Matt Palmer)

... (rest of the content remains the same)

## Setup

1. **Clone the repository:**

   ```bash
   git clone {githubrepo}
   cd {githubrepo}
   ```

2. **Copy the `devenv` file to `.env`:**

   ```bash
   cp devenv .env
   ```

## Docker

3. **Build Docker image:**

   ```bash
   docker compose -f docker-compose.yml build
   ```

4. **Run the Docker container:**

   ```bash
   docker compose -f docker-compose.yml up
   ```

   **Note:** If running Docker on Compute Engine, add the user to the Docker group:

   ```bash
   sudo usermod -aG docker $USER
   ```

   Then use `docker compose`, or use `sudo docker compose -f docker-compose.yml build` (not recommended).

## API to PostgreSQL

5. **Update the `io_config.yaml` file with your `.env` credentials:**

   ```yaml
   dev:
     # PostgreSQL
     POSTGRES_CONNECT_TIMEOUT: 10
     POSTGRES_DBNAME: "{{ env_var('POSTGRES_DBNAME') }}"
     POSTGRES_SCHEMA: "{{ env_var('POSTGRES_SCHEMA') }}" # Optional
     POSTGRES_USER: "{{ env_var('POSTGRES_USER') }}"
     POSTGRES_PASSWORD: "{{ env_var('POSTGRES_PASSWORD') }}"
     POSTGRES_HOST: "{{ env_var('POSTGRES_HOST') }}"
     POSTGRES_PORT: "{{ env_var('POSTGRES_PORT') }}"
   ```

   Test the connection using a simple `test_block`.

6. **Follow the steps in [api_to_postgres.md](./Postgres_using_api/api_to_postgres.md) file in [Postgres_using_api](./Postgres_using_api/) folder.**

## API to GCS

7. **Create a GCP bucket to load data.**

8. **Connect your service account to `mage io_config.yaml` file:**

   ```yaml
   GOOGLE_SERVICE_ACC_KEY_FILEPATH: "home/src/google-cred.json"
   ```

   Test the connection in the `test_block`.

9. **Follow the steps in [api_to_gcs.md](./GCS_using_api/api_to_GCS.md) file in [GCS_using_api](./GCS_using_api) folder.**

## GCS to BigQuery

10. **Follow the steps in [gcs_to_bigquery.md](./Bigquery_using_api/gcs_to_bigquery.md) file in [Bigquery_using_api](./Bigquery_using_api) folder.**

## Mage Deployment

11. **Ensure the following prerequisites are met:**
    - Terraform: [Install Terraform](https://www.terraform.io/downloads.html)
    - Google Cloud CLI: [Install Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
    - Google Cloud Permissions:
        - Artifact Registry Reader
        - Artifact Registry Writer
        - Cloud Run Developer
        - Cloud SQL Admin
        - Service Account Token Creator
    - Mage Terraform Templates

12. **Study backfills and other relevant topics.**

Thankyou