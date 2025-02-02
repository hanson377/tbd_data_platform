from dagster import asset, RunRequest
from .upcoming_events import fetch_calendar, fetch_recent_additions
from .posthog_to_motherduck import load_posthog

@asset
def calendar_events():
    """Asset that fetches and posts upcoming calendar events to Slack"""
    fetch_calendar()

@asset
def new_calendar_events():
    """Asset that fetches and posts new calendar events to Slack"""
    fetch_recent_additions()

@asset 
def elt_posthog_to_duckdb():
    load_posthog()