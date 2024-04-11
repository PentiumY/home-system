from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def index():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/print', methods=['POST'])
def print_something():
    data = request.json
    message = data.get('message')
    print(message)
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True, port="8001")
