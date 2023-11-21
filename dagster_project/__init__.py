import os

from dagster import Definitions

from .resources import RESOURCES_DEV
from .assets import dbt_example_person_assets, dbt_example_production_assets, dbt_example_sales_assets, dbt_example_analytics_assets

all_assets = [dbt_example_person_assets, dbt_example_production_assets, dbt_example_sales_assets, dbt_example_analytics_assets]

defs = Definitions(
    assets=all_assets,
    resources=RESOURCES_DEV,
)    
