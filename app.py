from flask import Flask, render_template, request, jsonify
import serial

app = Flask(__name__)
#arduino = serial.Serial('COM3', 9600)  # Adjust the port accordingly

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print('Received data from client:', data)
    # Process the received data as needed
    # You can send a response back to the client if necessary
    return jsonify({'message': 'Data received successfully'})


if __name__ == '__main__':
    app.run(debug=True)
