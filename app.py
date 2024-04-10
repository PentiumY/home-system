from flask import Flask, render_template
import serial

app = Flask(__name__)
#arduino = serial.Serial('COM3', 9600)  # Adjust the port accordingly

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<state>')
def control_led(state):
    if state == 'on':
        print("on")
        #arduino.write(b'1')  # Sending '1' to turn LED ON
    elif state == 'off':
        print("off")
        #arduino.write(b'0')  # Sending '0' to turn LED OFF
    return state

if __name__ == '__main__':
    app.run(debug=True)
