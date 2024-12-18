import json
import re
import logging
from pathlib import Path
from urllib.parse import urlparse, parse_qs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_curl_command(file_path):
    """Parse cURL command and extract configuration"""
    with open(file_path, 'r') as f:
        curl_command = f.read()
    
    config = {}
    
    # Extract URL and query parameters
    url_match = re.search(r"curl '([^']+)'", curl_command)
    if url_match:
        full_url = url_match.group(1)
        parsed_url = urlparse(full_url)
        
        # Base URL
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        config['GENERATE_URL'] = f"{base_url}{parsed_url.path}"
        # Add RESERVE_URL using the same base URL
        config['RESERVE_URL'] = f"{base_url}/v1/hme/reserve"
        
        # Query parameters
        query_params = parse_qs(parsed_url.query)
        config['QUERY_PARAMS'] = {
            key: value[0] for key, value in query_params.items()
        }
    
    # Extract headers
    headers = {}
    header_matches = re.finditer(r"-H '([^:]+): ([^']+)'", curl_command)
    for match in header_matches:
        key = match.group(1)
        value = match.group(2)
        
        # Handle cookies separately
        if key.lower() == 'cookie':
            cookies = {}
            cookie_pairs = value.split('; ')
            for pair in cookie_pairs:
                if '=' in pair:
                    cookie_key, cookie_value = pair.split('=', 1)
                    # Remove quotes if they exist
                    cookie_value = cookie_value.strip('"')
                    cookies[cookie_key] = cookie_value
            config['COOKIES'] = cookies
        else:
            headers[key] = value
    
    config['HEADERS'] = headers
    
    # Extract data if present
    data_match = re.search(r"--data-raw '([^']+)'", curl_command)
    if data_match:
        try:
            config['DATA'] = json.loads(data_match.group(1))
        except json.JSONDecodeError:
            config['DATA'] = data_match.group(1)
    
    return config

def create_config_file(config_data, output_path='config.py'):
    """Create a Python config file from the parsed data"""
    with open(output_path, 'w') as f:
        for key, value in config_data.items():
            f.write(f"{key} = {repr(value)}\n\n")

def main():
    # Check for headers.curl file
    header_file = Path('headers.curl')
    
    if not header_file.exists():
        logger.error("No headers.curl file found")
        return
    
    logger.info("Found headers.curl file")
    
    try:
        config_data = parse_curl_command(header_file)
        create_config_file(config_data)
        logger.info("Successfully created config.py")
        
    except Exception as e:
        logger.error(f"Error processing curl command: {e}")
        raise e

if __name__ == "__main__":
    main() 