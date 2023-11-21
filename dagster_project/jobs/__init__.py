from dagster import AssetSelection, define_asset_job, ScheduleDefinition

ingestion_job = define_asset_job("ingestion_job", AssetSelection.groups("person", "production", "sales"))

ingestion_schedule = ScheduleDefinition(job=ingestion_job, cron_schedule="*/3 * * * *")

