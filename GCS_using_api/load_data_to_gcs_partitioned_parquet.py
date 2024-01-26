#Using pyarrow used for chunking logic partitioning here
import pyarrow as pa
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

#Google service credentials

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "home/src/google-cred.json"

bucket_name  = 'dezoomcamp_nyc_taxi'
project_id = 'api_to_bigquery'

table_name = "green_taxi_data"

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(data,*args, **kwargs) -> None:
    
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date
    
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pa.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols = ['tpep_pickup_date'],
        filesystem =gcs  
    )