# url_checker.py - Check URLs with Safe Browsing APIs
import requests

SAFE_BROWSING_API = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

def check_url(url):
    """
    Checks URL using Google Safe Browsing API.
    Returns True if URL is safe, False if unsafe.
    """
    payload = {
        "client": {
            "clientId": "SafeGuardAI",
            "clientVersion": "1.0.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    response = requests.post(SAFE_BROWSING_API, json=payload)
    if response.status_code == 200:
        data = response.json()
        return not bool(data.get("matches", []))  # Safe if no matches
    return True  # Assume safe if API fails
