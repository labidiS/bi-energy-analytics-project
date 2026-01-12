CREATE TABLE stg_customers AS
SELECT
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
FROM raw_customers;
