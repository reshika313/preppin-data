SELECT 
    ORDER_ID, --selecting the existing fields I need for the final output
    CUSTOMER_AGE,
    BIKE_VALUE,
    EXISTING_CUSTOMER,
    DAY(DATE) AS DAY_OF_MONTH, --coverting date into day
    QUARTER(DATE) AS QUARTER, --converting date into quarter
    CAST(SPLIT(STORE_BIKE, ' - ')[0] AS STRING) AS STORE, --splitting store bike field to create the store field

    CASE
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Graval' THEN 'Gravel' --fixing spelling mistakes and creating the bike field by splitting
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Gravle' THEN 'Gravel'
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Rood' THEN 'Road'
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Rowd' THEN 'Road'
        WHEN SPLIT(STORE_BIKE, ' - ')[1] = 'Mountaen' THEN 'Mountain'
        ELSE SPLIT(STORE_BIKE, ' - ')[1]
    END AS BIKE

FROM PD2021_WK01 --converting order id into an integer and filtering and ordering this column
WHERE TO_NUMBER(ORDER_ID) > 10
ORDER BY TO_NUMBER(ORDER_ID);
