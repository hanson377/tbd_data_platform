from dagster import asset, RunRequest
from .upcoming_events import fetch_calendar, fetch_recent_additions

@asset
def calendar_events():
    """Asset that fetches and posts upcoming calendar events to Slack"""
    fetch_calendar()

@asset
def new_calendar_events():
    """Asset that fetches and posts new calendar events to Slack"""
    fetch_recent_additions()

