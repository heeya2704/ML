import requests
import json

BASE_URL = "http://127.0.0.1:5002"

def test_sentiment_api():
    print("Testing Flipkart Review Sentiment Prediction API...\n")
    
    test_reviews = [
        "The camera quality is excellent, sharp display and great value for money!",
        "Very bad product, battery drains rapidly and customer service is unhelpful.",
        "Product arrived in perfect condition, super fast shipping and high quality!"
    ]
    
    headers = {"Content-Type": "application/json"}
    
    for idx, review in enumerate(test_reviews, start=1):
        try:
            r = requests.post(f"{BASE_URL}/predict", json={"review": review}, headers=headers)
            print(f"Review {idx}: '{review}'")
            print(f"  Status Code: {r.status_code}")
            print(f"  Response: {json.dumps(r.json(), indent=2)}\n")
        except Exception as e:
            print(f"Error testing review {idx}: {e}\n")

if __name__ == "__main__":
    test_sentiment_api()
