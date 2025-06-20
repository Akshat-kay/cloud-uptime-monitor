from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Uptime Checker: Monitoring https://www.loblaw.ca"

@app.route('/metrics')
def metrics():
    try:
        response = requests.get("https://www.loblaw.ca", timeout=5)
        status = 1 if response.status_code == 200 else 0
    except Exception:
        status = 0
    return Response(f"uptime_loblaw_status {status}\n", mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
