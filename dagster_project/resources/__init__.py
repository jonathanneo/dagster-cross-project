import os
from pathlib import Path
from dagster_dbt import DbtCliResource

# DEV ENVIRONMENT 

PERSON_PROJECT_DIR = "../../dbt/person"
dbt_person_dev_resource = DbtCliResource(
    project_dir=PERSON_PROJECT_DIR,
    profiles_dir=PERSON_PROJECT_DIR,
    target="dev",
)

PRODUCTION_PROJECT_DIR = "../../dbt/production"
dbt_production_dev_resource = DbtCliResource(
    project_dir=PRODUCTION_PROJECT_DIR,
    profiles_dir=PRODUCTION_PROJECT_DIR,
    target="dev",
)

SALES_PROJECT_DIR = "../../dbt/sales"
dbt_sales_dev_resource = DbtCliResource(
    project_dir=SALES_PROJECT_DIR,
    profiles_dir=SALES_PROJECT_DIR,
    target="dev",
)

ANALYTICS_PROJECT_DIR = "../../dbt/analytics"
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
