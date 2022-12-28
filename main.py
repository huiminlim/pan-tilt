import time
import tkinter as tk

import RPi.GPIO as GPIO

servoPIN = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization

def rotate():
    p.ChangeDutyCycle(5)
    time.sleep(0.1)
    p.ChangeDutyCycle(0)

root = tk.Tk()

root.title('Hello Python')
root.geometry("300x100+100+100")

frame = tk.Label(root)
frame.pack(anchor=tk.CENTER, padx=10, pady=10)
button_minus = tk.Button(frame, text="turn", command=rotate)
button_minus.pack(anchor=tk.CENTER, padx=10, pady=10)

root.mainloop()

p.stop()
GPIO.cleanup()
