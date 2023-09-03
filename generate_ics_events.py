"""
This script generates an ICS file with events based on user input.

The events can be customized based on:
- Programming language
- Start date of the challenge
- Number of days for the challenge
- Category (default is None)
- Duration of each event
- Start time of each event
- Timezone

By default, the script uses:
- Tomorrow as the start date
- 30 days for the challenge
- 2 hours for each event's duration
- 20:00 as the start time
- System's local timezone
"""

from ics import Calendar, Event
from datetime import datetime, timedelta
from dateutil import tz
import pytz
import sys
import os

def main():
    """
    Main function to generate the ICS file.
    """
    # Check the number of arguments and assign defaults if necessary
    if len(sys.argv) < 2:
        print("Usage: python script_name.py [language] [start_date (DD.MM.YYYY)] [number_of_days=30] [category=None] [length_in_hours=2] [start_time=20:00] [timezone=local]")
        sys.exit(1)

    # Extract command line arguments with defaults
    language = sys.argv[1]

    # If start date is provided, parse it. Otherwise, set to tomorrow.
    if len(sys.argv) > 2:
        start_day, start_month, start_year = map(int, sys.argv[2].split('.'))
        naive_start_date = datetime(start_year, start_month, start_day)
    else:
        today = datetime.now()
        naive_start_date = today + timedelta(days=1)
        naive_start_date = naive_start_date.replace(hour=0, minute=0, second=0, microsecond=0)  # Reset time to midnight

    number_of_days = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    category = sys.argv[4] if len(sys.argv) > 4 else None
    length_in_hours = float(sys.argv[5]) if len(sys.argv) > 5 else 2.0
    start_hour, start_minute = map(int, sys.argv[6].split(':')) if len(sys.argv) > 6 else (20, 0)
    timezone_str = sys.argv[7] if len(sys.argv) > 7 else None

    # Get the specified timezone or default to local timezone
    if timezone_str:
        selected_tz = pytz.timezone(timezone_str)
    else:
        selected_tz = tz.tzlocal()

    # Start date with timezone and provided start time
    naive_start_date = naive_start_date.replace(hour=start_hour, minute=start_minute)
    start_date = naive_start_date.astimezone(selected_tz)

    # Create events based on the number of days
    cal = Calendar()
    for i in range(number_of_days):
        event = Event()
        event.name = f"Day {str(i+1).zfill(3)} of {number_of_days} Days {language} Challenge"
        if category:
            event.categories = {category}
        event.begin = start_date + timedelta(days=i)
        event.duration = timedelta(hours=length_in_hours)
        cal.events.add(event)

    # Check if the "ICS" directory exists, if not, create it
    if not os.path.exists("ICS"):
        os.makedirs("ICS")

    # Save the calendar to an ICS file inside the "ICS" folder
    filename = f"ICS/{number_of_days}_days_of_{language}.ics"
    with open(filename, "w") as f:
        f.write(cal.serialize())

    print(f"ICS file '{filename}' generated for {number_of_days} days of {language} starting from {naive_start_date.strftime('%d.%m.%Y')} with selected timezone!")

if __name__ == "__main__":
    main()
