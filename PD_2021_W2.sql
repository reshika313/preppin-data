-- Forming the first output which aggregates quantity sold, order value and average bike value by brand and type

SELECT 
    REGEXP_REPLACE(MODEL, '[^A-Za-z]', '') AS BRAND, -- Removing any non letter character from the column model
    BIKE_TYPE,
    SUM(QUANTITY) AS QUANTITY_SOLD,-- Aggregating quantity, order value and average value of each bike
    SUM(QUANTITY * VALUE_PER_BIKE) AS ORDER_VALUE,
    AVG(VALUE_PER_BIKE) AS AVG_VALUE_SOLD_PER_BRAND_AND_TYPE
FROM PD2021_WK02_BIKE_SALES
GROUP BY 
    REGEXP_REPLACE(MODEL, '[^A-Za-z]', ''), -- Grouping by brand and bike type
    BIKE_TYPE
ORDER BY ORDER_VALUE DESC;

WITH SECOND_OUTPUT AS ( -- Creating CTE to reference within same query
    SELECT
        REGEXP_REPLACE(MODEL, '[^A-Za-z]', '') AS BRAND,
        STORE,
        TO_DATE(ORDER_DATE, 'DD/MM/YYYY') AS ORDER_DATE, -- Correcting date format
        TO_DATE(SHIPPING_DATE, 'DD/MM/YYYY') AS SHIPPING_DATE,
        QUANTITY,
        VALUE_PER_BIKE,
        DATEDIFF('day', TO_DATE(ORDER_DATE, 'DD/MM/YYYY'), -- Adjusting date format
        TO_DATE(SHIPPING_DATE, 'DD/MM/YYYY')) AS DAYS_TO_SHIP
    FROM PD2021_WK02_BIKE_SALES
)

-- Second output which aggregates quantity sold, order value and average days to ship by brand and store

SELECT -- CTE needed because cannot use nested aggregates
    BRAND,
    STORE,
    SUM(QUANTITY * VALUE_PER_BIKE) AS TOTAL_ORDER_VALUE,
    SUM(QUANTITY) AS TOTAL_QUANTITY_SOLD,
    AVG(DAYS_TO_SHIP) AS AVG_DAYS_TO_SHIP
FROM SECOND_OUTPUT
GROUP BY BRAND, STORE
ORDER BY TOTAL_ORDER_VALUE DESC; 