from dagster import define_asset_job
from .assets import calendar_events, new_calendar_events

# Define the job that will run the asset
calendar_events_job = define_asset_job(
    name="calendar_events_job",
    selection=["calendar_events"]
)

new_calendar_events_job = define_asset_job(
    name="new_calendar_events_job",
    selection=["new_calendar_events"]
)