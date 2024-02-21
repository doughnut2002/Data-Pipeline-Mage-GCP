import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    months=["01","02","03","04","05","06","07","08","09","10","11","12"]    
    taxi_dtypes ={
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag':str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
        }
    parse_dates=['tpep_pickup_datetime','tpep_dropoff_datetime']   
    final_data=pd.DataFrame()


    for i in months:
            url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-{i}.csv.gz'
            df=pd.read_csv(url,sep=',',compression="gzip",dtype=taxi_dtypes,parse_dates=parse_dates)
            final_data=pd.concat([final_data,df],ignore_index=True)
        
    return final_data
