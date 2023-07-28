import requests

def check_endpoint(url):
    print("Checking endpoint: " + url)
    try:
        response = requests.get(url, timeout=5)  # 5 seconds timeout for waiting for a response
        response.raise_for_status()  # This will raise an exception if the HTTP response wasn't successful
        return True
    except requests.RequestException:
        return False