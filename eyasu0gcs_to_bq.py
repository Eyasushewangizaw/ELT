from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

# DAG default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# DAG definition
with DAG(
    dag_id='load_gcs_to_bq',
    default_args=default_args,
    description='Load a CSV file from GCS to BigQuery',
    schedule=None,  # Set as required (e.g., '@daily', '0 12 * * *')
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['bigquery', 'gcs', 'csv'],
) as dag:

    # Task to load CSV from GCS to BigQuery
    load_csv_to_bigquery = GCSToBigQueryOperator(
        task_id='eyasu_load_csv_to_bq',
        bucket='eyasubucketsrc',  
        source_objects=['global_health_data.csv'],  
        destination_project_dataset_table='eyasuproject2.eyasudataset1.eyasutable1',  
        source_format='CSV', 
        allow_jagged_rows=True,
        ignore_unknown_values=True,
        write_disposition='WRITE_TRUNCATE',  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
        skip_leading_rows=1,  
        field_delimiter=',',  # Delimiter for CSV, default is ','
        autodetect=True,  # Automatically infer schema from the file
      
    )

    load_csv_to_bigquery