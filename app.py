from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from google.oauth2 import service_account

app = Flask(__name__)

# Load credentials
SERVICE_ACCOUNT_FILE = 'client_secrets.json'
SCOPES = ['https://www.googleapis.com/auth/webmasters']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Create API client
search_console = build('searchconsole', 'v1', credentials=credentials)

@app.route('/sites', methods=['GET'])
def list_sites():
    """List verified sites in Google Search Console."""
    response = search_console.sites().list().execute()
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
