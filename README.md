# Banking Modern Data Stack

An end-to-end banking data engineering project that captures PostgreSQL changes using Debezium, streams events through Kafka, stores Parquet files in MinIO, loads raw data into Snowflake, transforms the data with dbt, tracks SCD Type 2 history, and orchestrates batch processing with Apache Airflow.

## Architecture

```text
PostgreSQL
    ↓ Debezium CDC
Apache Kafka
    ↓ Python consumer
MinIO (Parquet)
    ↓ Apache Airflow
Snowflake RAW
    ↓ dbt staging views
dbt snapshots (SCD Type 2)
    ↓
Dimension and fact tables
```

## Technologies

- PostgreSQL — operational source database
- Debezium — change data capture
- Apache Kafka — event streaming
- MinIO — S3-compatible object storage
- Apache Parquet — columnar storage format
- Snowflake — cloud data warehouse
- dbt Core — transformations and snapshots
- Apache Airflow — batch orchestration
- Docker Compose — local infrastructure
- Python — data generation, consumption and backfilling
