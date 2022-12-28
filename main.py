import time
import tkinter as tk

import RPi.GPIO as GPIO

baseServoPIN = 13
topServoPIN = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(baseServoPIN, GPIO.OUT)
GPIO.setup(topServoPIN, GPIO.OUT)
p1 = GPIO.PWM(baseServoPIN, 50) # GPIO 13 for PWM with 50Hz
p2 = GPIO.PWM(topServoPIN, 50) # GPIO 19 for PWM with 50Hz
p1.start(0) # Initialization
p2.start(0) # Initialization

def rotate_base():
    p1.ChangeDutyCycle(5)
    time.sleep(0.1)
    p1.ChangeDutyCycle(0)

def rotate_top():
    p2.ChangeDutyCycle(5)
    time.sleep(0.1)
    p2.ChangeDutyCycle(0)

root = tk.Tk()

root.title('Hello Python')
root.geometry("300x100+100+100")

frame = tk.Label(root)
frame.pack(anchor=tk.CENTER, padx=10, pady=10)
button_base = tk.Button(frame, text="Base", command=rotate_base)
button_base.pack(side=tk.LEFT, padx=10, pady=10)
button_top = tk.Button(frame, text="Top", command=rotate_top)
button_top.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()

p1.stop()
p2.stop()
GPIO.cleanup()
