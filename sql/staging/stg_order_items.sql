CREATE TABLE stg_order_items AS
SELECT
    order_id,
    product_id,
    price,
    freight_value
FROM raw_order_items;
