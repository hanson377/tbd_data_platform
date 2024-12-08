from dagster import asset, RunRequest
from .upcoming_events import fetch_calendar

@asset
def calendar_events():
    """Asset that fetches and posts calendar events to Slack"""
    fetch_calendar()