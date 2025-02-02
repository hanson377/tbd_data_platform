from dagster import Definitions
from .assets import calendar_events, new_calendar_events, elt_posthog_to_duckdb
from .jobs import calendar_events_job, new_calendar_events_job, posthog_to_duckdb_job
from .schedule import calendar_events_schedule, new_calendar_events_schedule, posthog_to_duckdb_schedule

defs = Definitions(
    assets=[calendar_events,new_calendar_events, elt_posthog_to_duckdb],
    jobs=[calendar_events_job,new_calendar_events_job, posthog_to_duckdb_job],
    schedules=[calendar_events_schedule,new_calendar_events_schedule, posthog_to_duckdb_schedule]
)
