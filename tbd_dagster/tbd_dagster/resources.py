from dagster import EnvVar
from dagster_dbt import DbtCliResource

dbt = DbtCliResource(
    project_dir="../tbd_dbt",  # Path to your dbt project
    profiles_dir="../tbd_dbt",  # Path to your dbt profiles directory 
    target="dev"  # Your default dbt target
)