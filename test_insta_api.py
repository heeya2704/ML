import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def test_fastapi_endpoints():
    print("Testing FastAPI Instagram Like Counter API...\n")
    
    # 1. Test GET /
    try:
        r_home = requests.get(f"{BASE_URL}/")
        print("1. GET / Response:")
        print(f"   Status Code: {r_home.status_code}")
        print(f"   Response JSON: {json.dumps(r_home.json(), indent=2)}\n")
    except Exception as e:
        print(f"1. GET / Error: {e}\n")

    # 2. Test POST /predict-likes with current_likes=1200 and new_likes=350 (Task 3)
    try:
        payload_valid = {"current_likes": 1200, "new_likes": 350}
        headers = {"Content-Type": "application/json"}
        r_valid = requests.post(f"{BASE_URL}/predict-likes", json=payload_valid, headers=headers)
        print("2. POST /predict-likes Valid Request (Task 3):")
        print(f"   Status Code: {r_valid.status_code}")
        print(f"   Response JSON: {json.dumps(r_valid.json(), indent=2)}\n")
    except Exception as e:
        print(f"2. POST /predict-likes Error: {e}\n")

    # 3. Test POST /predict-likes with missing field 'new_likes' (Task 4)
    try:
        payload_invalid = {"current_likes": 1200}
        headers = {"Content-Type": "application/json"}
        r_invalid = requests.post(f"{BASE_URL}/predict-likes", json=payload_invalid, headers=headers)
        print("3. POST /predict-likes Missing Field Request (Task 4 Validation):")
        print(f"   Status Code: {r_invalid.status_code}")
        print(f"   Response JSON: {json.dumps(r_invalid.json(), indent=2)}\n")
    except Exception as e:
        print(f"3. POST /predict-likes Validation Error: {e}\n")

if __name__ == "__main__":
    test_fastapi_endpoints()
