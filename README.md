## End-to-End ELT Pipeline on Google Cloud
# Overview

In this project, I built an end-to-end ELT (Extract, Load, Transform) data pipeline using Google Cloud Platform (GCP).

The goal of the project was to process a healthcare CSV dataset containing 1 million records of data’ health statistics over several years and make the data available for analytics and visualization through Looker Studio dashboards.

Using Looker Studio, I created interactive visual reports for each country, showing how key health indicators and diseases—such as Tuberculosis, Cancer, COVID-19, Diabetes, and Malaria—have changed over the years. I built dashboard (including France, the USA, Canada, Nigeria, and Italy) visualizes annual health trends, compares disease prevalence, and provides insights into how health conditions have evolved over time.

# How I designed and implemented the pipeline:

  A) Google Cloud Storage (GCS) : I stored the raw CSV file in GCS Bucket, which served as the landing zone for external data uploads.

  B) Compute Engine (VM) + Apache Airflow : I set up a Compute Engine virtual machine and installed Python, Apache Airflow and developed DAG file to orchestrate the pipeline.
  Airflow helps to process of extracting data from GCS, loading it into BigQuery, and performing transformations.

  C) BigQuery (Data Warehouse) : I used BigQuery as the data warehouse and structured it into three logical layers:

                Staging Dataset – holds the raw data loaded directly from GCS.

                Transforming Dataset – contains the cleaned and transformed data using SQL transformations.

                Reporting Dataset – stores the final analytics-ready Views of selected countries and used for reporting.

  D) Looker (Data Visualization) : I connected Looker to the reporting dataset in BigQuery to build dashboards and visualize insights from the processed data.

# Archtecture
<img width="1201" height="651" alt="ELT drawio" src="https://github.com/user-attachments/assets/63608b40-2350-4929-984f-f87300bbb79b" />



# What I Showed in this Project

  Extract – I extracted the CSV file from Google Cloud Storage.

  Load – Using Airflow’s GCSToBigQueryOperator in my DAG file, I loaded the raw data into BigQuery’s staging dataset.

  Transform – I applied SQL transformations within BigQuery Datawarehouse to clean and structure the data into transforming and reporting datasets.

  Visualize – Finally, I connected Looker to the reporting tables to create dashboards for end users.
