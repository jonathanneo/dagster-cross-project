import os
from pathlib import Path

from .dbt_translator import CustomDagsterDbtTranslator
from ..resources import (
    dbt_person_dev_resource,
    dbt_production_dev_resource,
    dbt_sales_dev_resource,
    dbt_analytics_dev_resource,
    PERSON_PROJECT_DIR,
    PRODUCTION_PROJECT_DIR,
    SALES_PROJECT_DIR,
    ANALYTICS_PROJECT_DIR,
)

from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslatorSettings

example_person_manifest_path = Path(PERSON_PROJECT_DIR, "target", "manifest.json")
if not example_person_manifest_path.exists(): 
    dbt_parse_invocation = dbt_person_dev_resource.cli(["parse"]).wait()
    example_person_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
@dbt_assets(
    manifest=example_person_manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(settings=DagsterDbtTranslatorSettings(enable_asset_checks=True)),
)
def dbt_person_assets(context: AssetExecutionContext, dbt_person: DbtCliResource):
    yield from dbt_person.cli(["build"], context=context).stream()

example_production_manifest_path = Path(PRODUCTION_PROJECT_DIR, "target", "manifest.json")
if not example_production_manifest_path.exists(): 
    dbt_parse_invocation = dbt_production_dev_resource.cli(["parse"]).wait()
    example_production_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
@dbt_assets(
    manifest=example_production_manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(settings=DagsterDbtTranslatorSettings(enable_asset_checks=True)),
)
def dbt_production_assets(context: AssetExecutionContext, dbt_production: DbtCliResource):
    yield from dbt_production.cli(["build"], context=context).stream()

example_sales_manifest_path = Path(SALES_PROJECT_DIR, "target", "manifest.json")
if not example_sales_manifest_path.exists(): 
    dbt_parse_invocation = dbt_sales_dev_resource.cli(["parse"]).wait()
    example_sales_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
@dbt_assets(
    manifest=example_sales_manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(settings=DagsterDbtTranslatorSettings(enable_asset_checks=True)),
)
def dbt_sales_assets(context: AssetExecutionContext, dbt_sales: DbtCliResource):
    yield from dbt_sales.cli(["build"], context=context).stream()


example_analytics_manifest_path = Path(ANALYTICS_PROJECT_DIR, "target", "manifest.json")
if not example_analytics_manifest_path.exists(): 
    dbt_parse_invocation = dbt_analytics_dev_resource.cli(["parse"]).wait()
    example_analytics_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
@dbt_assets(
    manifest=example_analytics_manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(settings=DagsterDbtTranslatorSettings(enable_asset_checks=True)),
)
def dbt_analytics_assets(context: AssetExecutionContext, dbt_analytics: DbtCliResource):
    yield from dbt_analytics.cli(["build"], context=context).stream()
