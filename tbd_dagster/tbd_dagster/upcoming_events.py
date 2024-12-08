import requests
from ics import Calendar
import arrow  # Add this import
from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

# Replace with your calendar's iCal URL
ICAL_URL = "https://calendar.google.com/calendar/ical/iqg6kkdjoii86na8pgtnmi0da8%40group.calendar.google.com/public/basic.ics"

# Add Slack configuration
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_CHANNEL = "#random_chatter"  # Replace with your channel name

def send_to_slack(events_summary):
    try:
        client = WebClient(token=SLACK_TOKEN)
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=":vibe-cat: Weekly Race Calendar Update :vibe-cat:",
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": ":vibe-cat: Upcoming Events :vibe-cat:"}
                },
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": events_summary}
                }
            ]
        )
    except SlackApiError as e:
        print(f"Error sending to Slack: {e.response['error']}")

def fetch_calendar():
    try:
        response = requests.get(ICAL_URL)
        response.raise_for_status()
        calendar = Calendar(response.text)

        now = arrow.now()
        seven_days_future = now.shift(days=7)  # Changed from -7 to 7

        events_summary = []
        print("Upcoming events in the next 7 days:")  # Updated message
        
        for event in calendar.events:
            event_time = arrow.get(event.begin)
                
            if event_time >= now and event_time <= seven_days_future: 
                url = event.description.split('"')[1] if event.description else "No URL"
                
                # Format the date nicely
                formatted_date = event_time.format('dddd, MMMM D YYYY')  # Using Arrow's format
                formatted_time = event_time.format('h:mm A')  # This will give you "2:30 PM" format
                
                # Format event details for both console and Slack
                event_details = (
                    f"📌 *Event:* {event.name}\n"
                    f"📍 *Location:* {event.location or 'No location'}\n"
                    f"🔗 *URL:* {url}\n"
                    f"🕒 *Date:* {formatted_date} at {formatted_time}\n"
                )
                events_summary.append(event_details)
                
                # Print to console
                print("\nEvent Details:")
                print(event_details)
                print("-" * 50)
        
        if events_summary:
            # Send to Slack
            formatted_summary = "\n\n".join(events_summary)
            send_to_slack(formatted_summary)
        else:
            print("No upcoming events found in the next 7 days")
            send_to_slack("No upcoming events found in the next 7 days! Stay thirsty, my friends")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching calendar: {e}")

if __name__ == "__main__":
    fetch_calendar()
