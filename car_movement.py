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

def left():
	GPIO.output(mL_a , 0)
	GPIO.output(mL_b , 1)

	GPIO.output(mR_a , 1)
	GPIO.output(mR_b , 0)
	
	left_wheels.ChangeDutyCycle(speed)
	right_wheels.ChangeDutyCycle(speed)

def right():
	GPIO.output(mL_a , 1)
	GPIO.output(mL_b , 0)

	GPIO.output(mR_a , 0)
	GPIO.output(mR_b , 1)

	left_wheels.ChangeDutyCycle(speed)
	right_wheels.ChangeDutyCycle(speed)

def stop():
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
