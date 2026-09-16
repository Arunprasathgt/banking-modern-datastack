import os
from pathlib import Path
from datetime import datetime

import boto3
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load PostgreSQL settings from the project .env
project_folder = Path(__file__).resolve().parent.parent
load_dotenv(project_folder / ".env")

# Load MinIO settings from consumer/.env
load_dotenv(Path(__file__).resolve().parent / ".env", override=True)

# Connect directly to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    dbname=os.getenv("POSTGRES_DB"),
)

# Read every existing customer
query = "SELECT * FROM public.customer"
df = pd.read_sql_query(query, connection)
connection.close()

print(f"Found {len(df)} customer records in PostgreSQL")

# Create a temporary Parquet file
file_name = "customer_backfill.parquet"
df.to_parquet(file_name, engine="fastparquet", index=False)

# Connect to MinIO
s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("MINIO_ENDPOINT"),
    aws_access_key_id=os.getenv("MINIO_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("MINIO_SECRET_KEY"),
)

bucket = os.getenv("MINIO_BUCKET")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
s3_key = f"customer/backfill/customer_{timestamp}.parquet"

# Upload and remove the temporary local file
s3.upload_file(file_name, bucket, s3_key)
os.remove(file_name)

print(f"✅ Uploaded {len(df)} customers to s3://{bucket}/{s3_key}")