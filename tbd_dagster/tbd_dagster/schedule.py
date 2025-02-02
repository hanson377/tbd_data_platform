from dagster import schedule, RunRequest
from .jobs import calendar_events_job, new_calendar_events_job, posthog_to_duckdb_job


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

@schedule(
    cron_schedule="0 9 * * *",  # Runs every day at 9 AM
    job_name="new_calendar_events_job",
    execution_timezone="America/New_York"
)
def new_calendar_events_schedule():
    """Schedule for calendar events asset - runs every Monday at 9 AM EST"""
    return RunRequest(
        run_key=None,
        run_config={},
        tags={"owner": "data_team"}
    )

@schedule(
    cron_schedule="0 */4 * * *",  # Runs every 4 hours
    job_name="posthog_to_duckdb_job", 
    execution_timezone="America/New_York"
)
def posthog_to_duckdb_schedule():
    """Schedule for PostHog to DuckDB job - runs every 4 hours"""
    return RunRequest(
        run_key=None,
        run_config={},
        tags={"owner": "data_team"}
    )

## yes