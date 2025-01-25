from flask import Flask, request, jsonify, send_from_directory
import webbrowser
import threading

app = Flask(__name__)

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

    # Log the received data
    print(f"IP Address: {ip_address}")
    print(f"Location: Latitude={latitude}, Longitude={longitude}")

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
