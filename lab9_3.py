import RPi.GPIO as GPIO
from flask import Flask, render_template, request

LedPin1 = 11
LedPin2 = 13

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LedPin1, GPIO.OUT)  
GPIO.setup(LedPin2, GPIO.OUT)  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def control_led():
    ledselect, option = request.form['ledselect'].split('/')
    if ledselect.isdigit() and option in ['on', 'off']:
        if ledselect == '1':
            GPIO.output(LedPin1, GPIO.HIGH if option == 'on' else GPIO.LOW)
        elif ledselect == '2':
            GPIO.output(LedPin2, GPIO.HIGH if option == 'on' else GPIO.LOW)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
