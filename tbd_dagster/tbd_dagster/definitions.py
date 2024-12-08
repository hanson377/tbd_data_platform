from dagster import Definitions
from .assets import calendar_events
from .jobs import calendar_events_job
from .schedule import calendar_events_schedule

defs = Definitions(
    assets=[calendar_events],
    jobs=[calendar_events_job],
    schedules=[calendar_events_schedule]
)