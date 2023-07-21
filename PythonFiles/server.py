from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return 'Flask server is running'


@app.route('/submit', methods=['POST'])
def handle_form_submission():
    try:
        # Get the JSON payload from the request
        data = request.get_json()

        # Extract the form data
        beholdNr = data.get('beholdNr')
        plukkNr = data.get('plukkNr')
        bane = data.get('bane')
        error = data.get('error')
        date = data.get('date')
        time = data.get('time')

        # Store the data in SQLite
        connection = sqlite3.connect('apo.db')
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO box (pickdate, beholderNr, locationId, registrationTime, errorId) VALUES (?, ?, ?, ?, ?)",
            (date, beholdNr, bane, time, error)
        )
        connection.commit()
        connection.close()

        # Send a successful response back to the JavaScript code
        response = {'message': 'Data received and stored successfully'}
        return jsonify(response), 200
    except Exception as e:
        # Send an error response back to the JavaScript code
        response = {'error': str(e)}
        return jsonify(response), 500


if __name__ == '__main__':
    app.run()
