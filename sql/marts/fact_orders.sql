CREATE TABLE fact_orders AS
SELECT
    o.order_id,
    o.customer_id,
    o.order_status,
    o.order_purchase_ts,
    SUM(i.price + i.freight_value) AS total_order_value
FROM stg_orders o
LEFT JOIN stg_order_items i
    ON o.order_id = i.order_id
GROUP BY
    o.order_id,
    o.customer_id,
    o.order_status,
    o.order_purchase_ts;
