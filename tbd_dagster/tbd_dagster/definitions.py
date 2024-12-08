from dagster import Definitions
from .assets import calendar_events, new_calendar_events
from .jobs import calendar_events_job, new_calendar_events_job
from .schedule import calendar_events_schedule, new_calendar_events_schedule

defs = Definitions(
    assets=[calendar_events,new_calendar_events],
    jobs=[calendar_events_job,new_calendar_events_job],
    schedules=[calendar_events_schedule,new_calendar_events_schedule]
)