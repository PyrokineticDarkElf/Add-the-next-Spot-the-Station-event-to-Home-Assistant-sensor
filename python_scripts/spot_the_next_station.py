import feedparser
from datetime import datetime, timedelta
import json

def extract_spot_the_station_info():
    feed_url = "https://spotthestation.nasa.gov/sightings/xml_files/United_Kingdom_England_London.xml"
    feed = feedparser.parse(feed_url)

    spot_the_station_info = {}

    current_time = datetime.now()

    for item in feed.entries:
        title = item.title
        description = item.description

        # Normalize the description by replacing "<br />" with "<br/>"
        description = description.replace("<br />", "<br/>")

        info_lines = description.split("<br/>")
        info_dict = {}

        for line in info_lines:
            line_parts = line.split(":", 1)
            if len(line_parts) == 2:
                key = line_parts[0].strip()
                value = line_parts[1].strip()
                info_dict[key] = value

        # Convert date and time strings to datetime objects
        date_str = info_dict.get("Date", "")
        time_str = info_dict.get("Time", "")
        datetime_str = f"{date_str} {time_str}"
        event_start = datetime.strptime(datetime_str, "%A %b %d, %Y %I:%M %p")

        # Exclude past events
        if event_start < current_time:
            continue

        # Calculate end time by adding duration to start time
        duration_str = info_dict.get("Duration", "")
        duration_minutes = int(duration_str.split()[0])
        event_end = event_start + timedelta(minutes=duration_minutes)

        # Stringify Times
        event_start_string = event_start.strftime("%Y-%m-%d %H:%M")
        event_end_string = event_end.strftime("%Y-%m-%d %H:%M")
        info_dict["Event Start"] = event_start_string
        info_dict["Event End"] = event_end_string

        spot_the_station_info = info_dict
        break

    return spot_the_station_info

next_event = extract_spot_the_station_info()
print(json.dumps(next_event))
