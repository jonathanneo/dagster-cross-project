select * from {{ source('sales', 'salesorderdetail') }}
