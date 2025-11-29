import requests, json

url = 'http://127.0.0.1:5000/send-message'
payload = {"message": "test"}
try:
    resp = requests.post(url, json=payload, timeout=5)
    print('Status:', resp.status_code)
    try:
        data = resp.json()
        print('Response JSON:', json.dumps(data, indent=2))
    except ValueError:
        print('Response Text:', resp.text)
except Exception as e:
    print('Error:', e)
