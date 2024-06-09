import requests
import backoff
import logging
from requests.exceptions import RequestException
import secret

open_api_key = secret.acn_token

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define exponential backoff configuration
BACKOFF_CONFIG = {
    'wait_gen': backoff.expo,
    'exception': (RequestException, ),
    'max_tries': 5,
    'max_time': 60,
}

@backoff.on_exception(**BACKOFF_CONFIG)
def openai_api(prompt, model="gpt-3.5-turbo-16k", temperature=0.3, top_p=1.0, n=1, stream=False):
    URL = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "top_p": top_p,
        "n": n,
        "stream": stream,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {open_api_key}",
    }

    try:
        response = requests.post(URL, headers=headers, json=payload, stream=False)
        response.raise_for_status()
        logging.info("API request successful")
        return response.json().get('choices')[0].get("message").get("content")
    except RequestException as e:
        logging.error(f"API request failed: {e}")
        raise e

def openai_api2(prompt, model="gpt-3.5-turbo-16k", temperature=0.7, top_p=1.0, n=1, stream=False):
    return openai_api(prompt, model, temperature, top_p, n, stream)