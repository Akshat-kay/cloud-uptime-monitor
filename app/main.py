from flask import Flask, Response
import requests

app = Flask(__name__)

TARGETS = [
    "https://www.loblaw.ca",
    "https://akshatkashyap.cloud",
    "https://example.com"
]

@app.route('/')
def index():
    return "Uptime Checker for Multiple Sites"

@app.route('/metrics')
def metrics():
    output = ""
    for url in TARGETS:
        name = url.replace("https://", "").replace("http://", "").replace(".", "_").replace("/", "")
        try:
            r = requests.get(url, timeout=5)
            status = 1 if r.status_code == 200 else 0
        except:
            status = 0
        output += f"uptime_status{{site=\"{url}\"}} {status}\n"
    return Response(output, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
