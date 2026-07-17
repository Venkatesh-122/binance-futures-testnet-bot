import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from bot.logging_config import logger

BASE_URL = "https://testnet.binancefuture.com"

def send_api_request(method, endpoint, params, api_key, api_secret):
    """
    Signs the parameters with the secret key and sends a direct REST call.
    """
    params['timestamp'] = int(time.time() * 1000)
    
    query_string = urlencode(params)
    signature = hmac.new(
        api_secret.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    final_query = f"{query_string}&signature={signature}"
    
    headers = {
        "X-MBX-APIKEY": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    logger.debug(f"Sending request to {endpoint} with params: {params}")
    
    if method == "POST":
        response = requests.post(f"{BASE_URL}{endpoint}", data=final_query, headers=headers)
    else:
        response = requests.get(f"{BASE_URL}{endpoint}?{final_query}", headers=headers)
        
    response.raise_for_status()
    return response.json()