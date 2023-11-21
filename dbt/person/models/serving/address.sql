select 
    addressid,
    city,
    stateprovinceid
from {{ source('person', 'address') }}