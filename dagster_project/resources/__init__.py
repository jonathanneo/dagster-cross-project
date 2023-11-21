import os
from pathlib import Path
from dagster_dbt import DbtCliResource
from dagster_airbyte import AirbyteResource

# airbyte resource

airbyte_instance = AirbyteResource(
    host="localhost",
    port="8000",
    # If using basic auth, include username and password:
    username="airbyte",
    password="password",
)

# dbt resource 

CURRENT_DIRECTORY = Path(__file__).parent.resolve()

PERSON_PROJECT_DIR = CURRENT_DIRECTORY / "../../dbt/person"
dbt_person_dev_resource = DbtCliResource(
    project_dir=PERSON_PROJECT_DIR,
    profiles_dir=PERSON_PROJECT_DIR,
    target="dev",
)

PRODUCTION_PROJECT_DIR = CURRENT_DIRECTORY / "../../dbt/production"
dbt_production_dev_resource = DbtCliResource(
    project_dir=PRODUCTION_PROJECT_DIR,
    profiles_dir=PRODUCTION_PROJECT_DIR,
    target="dev",
)

SALES_PROJECT_DIR = CURRENT_DIRECTORY / "../../dbt/sales"
dbt_sales_dev_resource = DbtCliResource(
    project_dir=SALES_PROJECT_DIR,
    profiles_dir=SALES_PROJECT_DIR,
    target="dev",
)

ANALYTICS_PROJECT_DIR = CURRENT_DIRECTORY / "../../dbt/analytics"
dbt_analytics_dev_resource = DbtCliResource(
    project_dir=ANALYTICS_PROJECT_DIR,
    profiles_dir=ANALYTICS_PROJECT_DIR,
    target="dev",
)

RESOURCES_DEV = {
    "dbt_person": dbt_person_dev_resource,
    "dbt_production": dbt_production_dev_resource,
    "dbt_sales": dbt_sales_dev_resource,
    "dbt_analytics": dbt_analytics_dev_resource,
}
