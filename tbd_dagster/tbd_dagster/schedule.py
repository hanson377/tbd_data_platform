from dagster import schedule, RunRequest
from .jobs import calendar_events_job

@schedule(
    cron_schedule="0 9 * * 1",  # Runs every Monday at 9 AM
    job_name="calendar_events_job",
    execution_timezone="America/New_York"
)
def calendar_events_schedule():
    """Schedule for calendar events asset - runs every Monday at 9 AM EST"""
    return RunRequest(
        run_key=None,
        run_config={},
        tags={"owner": "data_team"}
    )