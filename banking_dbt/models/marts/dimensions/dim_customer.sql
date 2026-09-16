{{ config(materialized='table') }}

SELECT
    customer_id,
    first_name,
    last_name,
    email,
    created_at,
    dbt_valid_from AS effective_from,
    dbt_valid_to AS effective_to,
    dbt_valid_to IS NULL AS is_current
FROM {{ ref('customers_snapshot') }}