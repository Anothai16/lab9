import RPi.GPIO as GPIO
from flask import Flask

LedPin1 = 11
LedPin2 = 13

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(LedPin1, GPIO.OUT)  
GPIO.setup(LedPin2, GPIO.OUT)  

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/<ledselect>/<option>')
def control_led(ledselect, option):  
    if option == "on":
        if ledselect == '1':
            GPIO.output(LedPin1, GPIO.HIGH)  
            return "เปิด LED ดวงที่ 1" 
        elif ledselect == '2':
            GPIO.output(LedPin2, GPIO.HIGH)  
            return "เปิด LED ดวงที่ 2"  
    elif option == "off":
        if ledselect == '1':
            GPIO.output(LedPin1, GPIO.LOW)  
            return "ปิด LED ดวงที่ 1"  
        elif ledselect == '2':
            GPIO.output(LedPin2, GPIO.LOW)  
            return "ปิด LED ดวงที่ 2"  
    else:
        print("คำสั่งไม่ถูกต้อง")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
