from flask import Flask, send_from_directory, jsonify, request
import requests, random
#test
app = Flask(__name__, static_folder='static')
j = 0
# Serve the main page
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Endpoint that forwards the message to the external API
@app.route('/send-message', methods=['POST'])
def send_message():
    payload = request.json or {"what is this site?"}
    try:
        resp = requests.post('https://teztink.free.beeceptor.com', json=payload, timeout=5)
        # Try to parse JSON response, fallback to text
        try:
            api_resp = resp.json()
        except ValueError:
            api_resp = {"text": resp.text}
        return jsonify({"status": "success", "api_response": api_resp}), resp.status_code
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

@app.route('/get-message/<path:subpath>', methods=['GET'])
def get_message(subpath):
    try:
        resp = requests.get(f'https://teztink.free.beeceptor.com/{subpath}', timeout=5)
        resp.raise_for_status()
       
        try:
            api_resp = resp.json()
        except ValueError:
            api_resp = {"text": resp.text}
            
        return jsonify({"status": "success", "api_response": api_resp}), resp.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=random.randint(1000, 9999))
