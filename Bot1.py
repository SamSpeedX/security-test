import requests
import time
import random

TARGET_URL = input("TARGET_URL: ")
BOT_AGENTS = [
    "python-requests/2.25.1",
    "curl/7.64.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Scrapy/2.4.1 (+https://scrapy.org)",
]

HEADERS_LIST = [
    {"Accept-Language": "en-US,en;q=0.9"},
    {"Accept-Language": "sw-TZ,sw;q=0.9"},
    {"Accept-Encoding": "gzip, deflate"},
]

def spam_requests(endpoint="/"):
    for i in range(5000):  # Increase number of requests
        headers = {
            "User-Agent": random.choice(BOT_AGENTS),
        }
        headers.update(random.choice(HEADERS_LIST))
        url = TARGET_URL + endpoint
        try:
            r = requests.get(url, headers=headers, timeout=5)
            print(f"Request {i+1}: Status {r.status_code} | UA: {headers['User-Agent']}")
            if r.status_code == 429:
                print("⚠️ Rate limiting detected!")
                break
        except Exception as e:
            print(f"Request {i+1}: Failed - {e}")
        time.sleep(0.05)  # decrease delay for faster traffic

if __name__ == "__main__":
    spam_requests("/")
    spam_requests("/login")
