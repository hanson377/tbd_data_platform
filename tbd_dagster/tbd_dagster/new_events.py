import requests
from ics import Calendar
import arrow  # Add this import
from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from .upcoming_events import send_to_slack

# Replace with your calendar's iCal URL
ICAL_URL = "https://calendar.google.com/calendar/ical/iqg6kkdjoii86na8pgtnmi0da8%40group.calendar.google.com/public/basic.ics"

# Add Slack configuration
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_CHANNEL = "#random_chatter"  # Replace with your channel name


def fetch_recent_additions(hours_lookback=24):
    try:
        response = requests.get(ICAL_URL)
        response.raise_for_status()
        calendar = Calendar(response.text)

        now = arrow.now()
        recent_threshold = now.shift(hours=-hours_lookback)

        events_summary = []
        print(f"Events added in the last {hours_lookback} hours:")
        
        for event in calendar.events:
            # Check if the event has a created timestamp
            if event.created and arrow.get(event.created) >= recent_threshold:
                event_time = arrow.get(event.begin)
                url = event.description.split('"')[1] if event.description else "No URL"
                
                # Format the date nicely
                formatted_date = event_time.format('dddd, MMMM D YYYY')
                formatted_time = event_time.format('h:mm A')
                
                # Format event details for both console and Slack
                event_details = (
                    f"🆕 *New Event Added!*\n"
                    f"📌 *Event:* {event.name}\n"
                    f"📍 *Location:* {event.location or 'No location'}\n"
                    f"🔗 *URL:* {url}\n"
                    f"🕒 *Date:* {formatted_date} at {formatted_time}\n"
                    f"📅 *Added:* {arrow.get(event.created).humanize()}\n"
                )
                events_summary.append(event_details)
                
                # Print to console
                print("\nEvent Details:")
                print(event_details)
                print("-" * 50)
        
        if events_summary:
            # Send to Slack
            formatted_summary = "\n\n".join(events_summary)
            send_to_slack(formatted_summary, ":new: Recently Added Events :new:")
        else:
            print(f"No new events added in the last {hours_lookback} hours")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching calendar: {e}")



if __name__ == "__main__":
    fetch_recent_additions()
