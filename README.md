# Programming Challenge Calendar Generator

This script generates an ICS file with events based on user input for a programming challenge. Users can customize several parameters to tailor the challenge according to their preferences.

## Features

- Customize the programming language for the challenge.
- Set a custom start date or use the default (tomorrow).
- Define the number of days for the challenge.
- Set the duration for each event.
- Choose a start time for each event.
- Specify a timezone or use the system's local timezone.

## Usage

\`\`\`bash
python script_name.py [language] [start_date (DD.MM.YYYY)] [number_of_days=30] [length_in_hours=2] [start_time=20:00] [timezone=local]
\`\`\`

For example:

\`\`\`bash
python script_name.py Python 01.09.2023 30 2 20:00 America/New_York
\`\`\`

This would generate a 30-day Python challenge starting on September 1, 2023, with each event lasting 2 hours and starting at 8:00 PM in the New York timezone.

## Installation

1. Clone this repository:
   \`\`\`bash
   git clone [repository_url]
   \`\`\`

2. Navigate to the project directory:
   \`\`\`bash
   cd [directory_name]
   \`\`\`

3. (Optional) Set up a virtual environment:
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   \`\`\`

4. Install the required packages:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

5. Run the script as mentioned in the [Usage](#usage) section.

## Output

The generated ICS file will be saved in the `ICS` directory. This file can be imported into calendar applications like Google Calendar or Microsoft Outlook.
