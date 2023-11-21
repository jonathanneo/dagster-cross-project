import os

from dagster import Definitions

from .resources import RESOURCES_DEV
from .assets import dbt_person_assets, dbt_production_assets, dbt_sales_assets, dbt_analytics_assets, airbyte_assets

all_assets = [dbt_person_assets, dbt_production_assets, dbt_sales_assets, dbt_analytics_assets, airbyte_assets]

defs = Definitions(
    assets=all_assets,
    resources=RESOURCES_DEV,
)    
