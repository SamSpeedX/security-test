import requests
import time
import random

TARGET_URL = input("Target URL: ")
BOT_AGENTS = [
    "python-requests/2.25.1",
    "curl/7.64.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Scrapy/2.4.1 (+https://scrapy.org)",
]

def spam_requests(endpoint="/"):
    for i in range(100):
        headers = {
            "User-Agent": random.choice(BOT_AGENTS)
        }
        url = TARGET_URL + endpoint
        try:
            r = requests.get(url, headers=headers, timeout=5)
            print(f"Request {i+1}: Status {r.status_code} | UA: {headers['User-Agent']}")
        except Exception as e:
            print(f"Request {i+1}: Failed - {e}")
        time.sleep(0.1)  # small delay to mimic traffic

if __name__ == "__main__":
    spam_requests("/")
    spam_requests("/login")
