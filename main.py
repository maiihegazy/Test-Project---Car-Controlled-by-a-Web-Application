from flask import Flask , render_template as rt , request as req
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

enL = 6
enR = 12
mL_a = 27
mL_b = 22
mR_a = 23
mR_b = 24
speed = 100

GPIO.setup(enL , GPIO.OUT) #Enable A
GPIO.setup(enR , GPIO.OUT) #Enable B
GPIO.setup(mL_a , GPIO.OUT) #out1
GPIO.setup(mL_b , GPIO.OUT) #out2
GPIO.setup(mR_a , GPIO.OUT) #out3
GPIO.setup(mR_b , GPIO.OUT) #out4


left_wheels = GPIO.PWM(enL,100) 
right_wheels = GPIO.PWM(enR,100)
left_wheels.start(0)
right_wheels.start(0)



def forward():
	
	GPIO.output(mL_a , 1)
	GPIO.output(mL_b , 0)
	GPIO.output(mR_a , 1)
	GPIO.output(mR_b , 0)

	left_wheels.ChangeDutyCycle(speed)
	right_wheels.ChangeDutyCycle(speed)

def backward():
	GPIO.output(mL_a , 0)
	GPIO.output(mL_b , 1)

	GPIO.output(mR_a , 0)
	GPIO.output(mR_b , 1)

	left_wheels.ChangeDutyCycle(speed)
	right_wheels.ChangeDutyCycle(speed)

def Left():
	GPIO.output(mL_a , 0)
	GPIO.output(mL_b , 1)

	GPIO.output(mR_a , 1)
	GPIO.output(mR_b , 0)
	
	left_wheels.ChangeDutyCycle(speed)
	right_wheels.ChangeDutyCycle(speed)

def Right():
	GPIO.output(mL_a , 1)
	GPIO.output(mL_b , 0)

	GPIO.output(mR_a , 0)
	GPIO.output(mR_b , 1)

	left_wheels.ChangeDutyCycle(speed)
	right_wheels.ChangeDutyCycle(speed)

def Stop():
    GPIO.output(mL_a , 0)
    GPIO.output(mL_b , 0)
    GPIO.output(mR_a , 0)
    GPIO.output(mR_b , 0)

    left_wheels.ChangeDutyCycle(0)
    right_wheels.ChangeDutyCycle(0)

def end():
    
    GPIO.output(mL_a , 0)
    GPIO.output(mL_b , 0)
    GPIO.output(mR_a , 0)
    GPIO.output(mR_b , 0)
    
    left_wheels.stop()
    right_wheels.stop()
    
    GPIO.cleanup()

#from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
#from send_email import send_email 
#from sqlalchemy.sql import func

app = Flask (__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/height_collector'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model) :
    __tablename__ = "data"
    id = db.Column(db.Integer , primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__ (self , email_ , height_):
        self.email_ = email_
        self.height_ = height_
'''
@app.route('/') #/ == home page
def home ():
    return rt("index.html")

@app.route('/success' , methods = ['POST']) 
def success ():
  #while{
    if req.method == 'POST' : 
        #email = req.form["email_name"]
        #height = req.form["height"]
        #up = req.form["up"]
        up = req.form['up']
        down = req.form['down']
        right = req.form['right']
        left = req.form['left']
        stop = req.form['stop']
        print(req.form)
        
        if(up == "1"):
            print("up")
            forward()        
        elif(down == "1"):
            print("down")
            backward()
        elif(right == "1"):
            print("right")
            Right()
        elif(left == "1"):
            print("left")
            Left()
        elif(stop == "1"):
            print("stop")
            Stop()
        else:
            Stop()
        return rt("success.html")
    else : 
        return rt("index.html" , text = "Seems like we've got something from that email address already!")


if __name__ == "__main__" :
    #app.run(debug = True)  #runs on local host
    app.run(host='0.0.0.0') #runs on local network
    