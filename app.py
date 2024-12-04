from flask import Flask, render_template, request, jsonify
import threading
from honeypot import start_honeypot
import logging

# Set up Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log_click', methods=['POST'])
def log_click():
    logging.info("Button clicked on the web page!")
    return jsonify({"message": "Click logged successfully"}), 200

if __name__ == '__main__':
    # Start the honeypot in a separate thread
    honeypot_thread = threading.Thread(target=start_honeypot, args=('0.0.0.0', 9090), daemon=True)
    honeypot_thread.start()

    # Run the Flask app
    app.run(debug=True)
