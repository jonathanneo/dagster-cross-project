with stg_address as (
    select *
    from {{ source('person', 'address') }}
),

stg_stateprovince as (
    select *
    from {{ source('person', 'stateprovince') }}
),

stg_countryregion as (
    select *
    from {{ source('person', 'countryregion') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['stg_address.addressid']) }} as address_key,
    stg_address.addressid,
    stg_address.city as city_name,
    stg_stateprovince.name as state_name,
    stg_countryregion.name as country_name
from stg_address
left join stg_stateprovince 
    on stg_address.stateprovinceid = stg_stateprovince.stateprovinceid
left join stg_countryregion 
    on stg_stateprovince.countryregioncode = stg_countryregion.countryregioncode
