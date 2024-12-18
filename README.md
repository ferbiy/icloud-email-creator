# iCloud Email Generator

This script automatically generates and reserves iCloud email addresses at regular intervals. It creates 5 email addresses every hour with random delays between creations to mimic human behavior.

## Features

- Automatically generates and reserves iCloud email addresses
- Creates 5 emails per batch with random delays (1-3 minutes) between each creation
- Waits approximately 1 hour between batches
- Comprehensive logging to both console and file
- Error handling and graceful failure recovery
- Configurable settings via config file
- Automatic configuration generation from cURL command

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

There are two ways to configure the script:

### Option 1: Using cURL Command (Recommended)

1. In Chrome DevTools (F12):
   - Go to the Network tab
   - Visit iCloud.com, click on creating emails
![image](https://github.com/user-attachments/assets/c175ba4a-736e-4d9d-b9a4-904e527b4d8f)
   - Click on + button
![image](https://github.com/user-attachments/assets/9dd9cbcb-9849-414e-b2b6-533d60995114)
   - See request "generate", click right button on it
![image](https://github.com/user-attachments/assets/078b1c55-85a5-4aac-a13e-03f346d9c7c7)
   - Select "Copy as cURL" (bash)
![image](https://github.com/user-attachments/assets/625158f9-dd60-4f46-9da1-2d7194fa55cb)


2. Create a file named `headers.curl` and paste the cURL command into it

3. Run the configuration generator:
```bash
python create_config.py
```

This will automatically create `config.py` with all necessary settings.

### Option 2: Manual Configuration

1. Copy `config.example.py` to `config.py`:
```bash
cp config.example.py config.py
```

2. Update the `COOKIES` dictionary with your iCloud session cookies from Chrome DevTools

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
