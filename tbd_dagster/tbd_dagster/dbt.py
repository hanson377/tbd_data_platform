from dagster import asset
from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_PATH = "../tbd_dbt"
DBT_PROFILES_DIR = "../tbd_dbt"

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH,
    profiles_dir=DBT_PROFILES_DIR,
    key_prefix=["tbd_dbt"],  # Optional prefix for your asset keys
)