import logging
import requests
from bs4 import BeautifulSoup
import json
import re
import sys
from html import unescape

def fetch_html(url):
    logging.debug(f"Fetching HTML from {url}")
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def extract_json_data(doc):
    logging.debug("Extracting JSON data from HTML")
    script = doc.find("script", string=lambda s: s and "AoPS.bootstrap_data" in s)
    if not script:
        raise ValueError("Script containing AoPS.bootstrap_data not found")

    content = script.string
    start = content.find('{')
    bracket_count = 0
    for i in range(start, len(content)):
        if content[i] == '{':
            bracket_count += 1
        elif content[i] == '}':
            bracket_count -= 1
        if bracket_count == 0:
            end = i + 1
            break
    else:
        raise ValueError("Failed to find end of JSON object")

    return json.loads(content[start:end])

def extract_rendered_post(data):
    try:
        return data['preload_cmty_data']['topic_data']['posts_data'][0]['post_rendered']
    except (KeyError, IndexError):
        raise ValueError("Failed to extract rendered post HTML")

def clean_html_to_text(raw_html):
    # Replace <img ... alt="..."> with alt text
    text = re.sub(r'<img [^>]*alt="([^"]*)"[^>]*>', r'\1', raw_html)
    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities
    text = unescape(text)
    # Strip extra whitespace
    return text.strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    url = sys.argv[1]

    try:
        doc = fetch_html(url)
        json_data = extract_json_data(doc)
        raw_html = extract_rendered_post(json_data)
        clean_text = clean_html_to_text(raw_html)
        print(clean_text)
    except Exception as e:
        logging.error(f"Failed to fetch and parse problem: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
