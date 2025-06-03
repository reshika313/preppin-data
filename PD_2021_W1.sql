SELECT 
    ORDER_ID,
    CUSTOMER_AGE,
    BIKE_VALUE,
    EXISTING_CUSTOMER,
    DAY(DATE) AS DAY_OF_MONTH,
    QUARTER(DATE) AS QUARTER,
    CAST(SPLIT(STORE_BIKE, ' - ')[0] AS STRING) AS STORE,

    CASE
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Graval' THEN 'Gravel'
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Gravle' THEN 'Gravel'
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Rood' THEN 'Road'
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Rowd' THEN 'Road'
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Mountaen' THEN 'Mountain'
        ELSE SPLIT(STORE_BIKE, ' - ')[1]
    END AS BIKE

FROM PD2021_WK01
WHERE TO_NUMBER(ORDER_ID) > 10
ORDER BY TO_NUMBER(ORDER_ID);