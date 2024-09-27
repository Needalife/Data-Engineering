import requests
import time

url = "https://api.polygon.io/v1/open-close/AAPL/2024-09-24?adjusted=true&apiKey=Hzp2QBWvkQ3lhgMA06uuQHXiBHuLLMBb"
count = 0

while True:
    for i in range(5):  # Send 5 requests in a minute
        response = requests.get(url)
        count += 1
        
        print(f"Request {count}: Status Code {response.status_code}")
        
        if response.status_code == 429:
            print("Rate limit reached!")
            break
        elif response.status_code != 200:
            print(f"Error {response.status_code}, stopping test.")
            break
        
        time.sleep(10)  

    time.sleep(60 - 5 * 10) 
