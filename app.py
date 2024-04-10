from flask import Flask, render_template, request, jsonify
import serial

app = Flask(__name__)
#arduino = serial.Serial('COM3', 9600)  # Adjust the port accordingly

tempState: dict = {
    "Main light": False
}

itemDict: dict = {
    1: {
        "name": "Main light",
        "path": "house/lights/mainLight"
    }
}

def findItem(id):
    item = itemDict[id]
    return item

def getItemData(id):
    state = tempState[findItem(id)["name"]]
    return state

def setItemData(id, state):
    global tempState
    name = findItem(id)["name"]
    tempState[name] = state

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    #print('Received data from client:', data)
    # Process the received data as needed

    print(f"Setting {findItem(data["itemID"])["name"]} to {data["state"]}")
    setItemData(data["itemID"],data["state"])

    # You can send a response back to the client if necessary
    return jsonify({'message': 'Data received successfully'})


if __name__ == '__main__':
    app.run(debug=True)
