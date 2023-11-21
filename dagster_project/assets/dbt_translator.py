from typing import Any, Mapping, Optional

from dagster import AssetKey, AutoMaterializePolicy
from dagster_dbt import DagsterDbtTranslator


class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    @classmethod
    def get_group_name(cls, dbt_resource_props: Mapping[str, Any]) -> Optional[str]:
        return dbt_resource_props["fqn"][0]
    @classmethod
    def get_asset_key(cls, dbt_resource_props: Mapping[str, Any]) -> Optional[str]:
        dagster_metadata = dbt_resource_props.get("meta", {}).get("dagster", {})
        asset_key_config = dagster_metadata.get("asset_key", [])
        if asset_key_config:
            return AssetKey(asset_key_config)

        if dbt_resource_props["resource_type"] == "source":
            if dbt_resource_props.get("identifier"):
                source_resource_name = dbt_resource_props.get("identifier")
            else: 
                source_resource_name = dbt_resource_props["name"]
            components = [dbt_resource_props["source_name"],  dbt_resource_props["schema"], source_resource_name]
        else:
            project_name = dbt_resource_props["fqn"][0]
            if dbt_resource_props.get("alias"): 
                resource_name = dbt_resource_props.get("alias")
            else: 
                resource_name = dbt_resource_props["name"]
            components = [project_name, dbt_resource_props["schema"], resource_name]
        
        return AssetKey(components)
    
    def get_auto_materialize_policy(
        self, dbt_resource_props: Mapping[str, Any]
    ) -> Optional[AutoMaterializePolicy]:
        return AutoMaterializePolicy.eager()
