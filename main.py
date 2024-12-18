import time
import random
import logging
import requests
from datetime import datetime
from config import (
    GENERATE_URL, 
    RESERVE_URL, 
    HEADERS, 
    COOKIES, 
    QUERY_PARAMS
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_creator.log'),
        logging.StreamHandler()
    ]
)

def generate_email():
    try:
        response = requests.post(
            GENERATE_URL,
            headers=HEADERS,
            cookies=COOKIES,
            params=QUERY_PARAMS,
            json={"langCode": "ru-ru"}
        )
        response.raise_for_status()
        return response.json()["result"]["hme"]
    except Exception as e:
        logging.error(f"Error generating email: {str(e)}")
        return None

def reserve_email(email):
    try:
        response = requests.post(
            RESERVE_URL,
            headers=HEADERS,
            cookies=COOKIES,
            params=QUERY_PARAMS,
            json={
                "hme": email,
                "label": "13",
                "note": ""
            }
        )
        response.raise_for_status()
        return True
    except Exception as e:
        logging.error(f"Error reserving email: {str(e)}")
        return False

def create_email():
    max_retries = 3
    for attempt in range(max_retries):
        email = generate_email()
        if email:
            if reserve_email(email):
                logging.info(f"Successfully created email: {email}")
                return True
            else:
                logging.warning(f"Failed to reserve email on attempt {attempt + 1}/{max_retries}")
                time.sleep(random.randint(5, 15))  # Wait before retry
        else:
            logging.warning(f"Failed to generate email on attempt {attempt + 1}/{max_retries}")
            time.sleep(random.randint(5, 15))  # Wait before retry
    
    logging.error("Failed to create email after all retries")
    return False

def main():
    while True:
        successful_creations = 0
        failed_attempts = 0
        
        # Try to create 5 emails
        while successful_creations < 5:
            if create_email():
                successful_creations += 1
                failed_attempts = 0  # Reset failed attempts counter
            else:
                failed_attempts += 1
                logging.warning(f"Email creation failed. Attempts failed: {failed_attempts}")
                
                # If we've failed multiple times, take a longer break
                if failed_attempts >= 3:
                    wait_time = random.randint(300, 600)  # 5-10 minutes
                    logging.info(f"Multiple failures detected. Taking a longer break: {wait_time} seconds")
                    time.sleep(wait_time)
                    failed_attempts = 0  # Reset counter after break
            
            # Random delay between email creations (1-3 minutes)
            if successful_creations < 5:  # Don't wait after the last email
                delay = random.randint(60, 180)
                logging.info(f"Waiting {delay} seconds before next email creation...")
                time.sleep(delay)
        
        logging.info(f"Created {successful_creations} emails in this batch")
        
        # Wait for the next hour (3600 seconds = 1 hour)
        next_run = 3600 + random.randint(60, 180)  # 1 hour + 1-3 minutes
        logging.info(f"Waiting {next_run/60:.1f} minutes until next batch...")
        time.sleep(next_run)

if __name__ == "__main__":
    logging.info("Starting email creation service")
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Service stopped by user")
    except Exception as e:
        logging.error(f"Service crashed: {str(e)}")
        # Wait a bit and restart
        time.sleep(60)
        main() 