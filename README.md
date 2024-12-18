# iCloud Email Generator

This script automatically generates and reserves iCloud email addresses at regular intervals. It creates 5 email addresses every hour with random delays between creations to mimic human behavior.

## Features

- Automatically generates and reserves iCloud email addresses
- Creates 5 emails per batch with random delays (1-3 minutes) between each creation
- Waits approximately 1 hour between batches
- Comprehensive logging to both console and file
- Error handling and graceful failure recovery
- Configurable settings via config file

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository: 
```bash
git clone <repository-url>
cd icloud-email-generator
```

2. Install the required dependencies:
```bash
pip install requests
```


## Configuration

1. Open `config.py` and update the `COOKIES` dictionary with your iCloud session cookies. To get these:

   - Open Chrome DevTools (F12)
   - Go to the Network tab
   - Visit iCloud.com and log in
   - Look for any request to `icloud.com`
   - In the request headers, find the `Cookie` section
   - Copy all cookies and add them to the `COOKIES` dictionary in `config.py`

Example cookie format:
```python
COOKIES = {
"X-APPLE-WEBAUTH-USER": "your-cookie-value",
"X-APPLE-DS-WEB-SESSION-TOKEN": "your-token-value",
# Add all other cookies...
}
```

## Usage

Run the script:
```bash
python main.py
```


The script will:
1. Create 5 email addresses with random delays between each creation
2. Wait approximately 1 hour
3. Repeat the process

To stop the script, press `Ctrl+C`.

## Logging

The script creates a log file `email_creator.log` in the same directory. The log includes:
- Successful email creations
- Errors and failures
- Waiting periods
- Script start/stop events

## Error Handling

The script handles various types of errors:
- Network connection issues
- API response errors
- Invalid cookies
- Other unexpected errors

If an error occurs during email creation, the script will log the error and continue with the next attempt.

## Customization

You can modify these parameters in `main.py`:
- Number of emails per batch (default: 5)
- Delay between email creations (default: 1-3 minutes)
- Wait time between batches (default: ~1 hour)

## Important Notes

- Make sure to keep your cookies updated as they may expire
- Excessive use may trigger rate limiting or account restrictions
- This script is for educational purposes only

## License

MIT License - feel free to modify and distribute as needed.