import requests

resp = requests.post(
    "http://127.0.0.1:8000/query",
    json={"user_input": "Show me all transactions above 5000"}
)

print("Status:", resp.status_code)
print("Raw response:", resp.text)   # see what server returned
