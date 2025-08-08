from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/dashboard-data")
def dashboard_data():
    # Sample: Jira ticket count (replace with real API and token)
    # For demo, we just fake the data
    data = [
        {"tool": "Jira", "tickets": 12334},
        {"tool": "Bitbucket", "commits": 28},
        {"tool": "Confluence", "pages": 5}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

