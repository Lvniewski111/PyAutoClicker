import time
from tkinter import *

# Set the number of clicks
num_clicks = 0

# Set the delay between clicks (in seconds)
delay = 0.5

# Function to start the auto clicker
def start_clicking():
    global num_clicks
    num_clicks = 100
    perform_clicks()

# Function to stop the auto clicker
def stop_clicking():
    global num_clicks
    num_clicks = 0

# Function to perform the clicks
def perform_clicks():
    global num_clicks
    while num_clicks > 0:
        # Use the time module to pause execution for the specified
        # delay
        time.sleep(delay)

        # Simulate a click
        print("click")
        num_clicks -= 1

# Create the GUI
root = Tk()
root.title("Auto Clicker")

# Bind the keyboard shortcuts Ctrl+Shift+S and Ctrl+Shift+E
# to the start and stop buttons, respectively
root.bind("<Control-Shift-s>", lambda event: start_clicking())
root.bind("<Control-Shift-e>", lambda event: stop_clicking())

# Create the start button
start_button = Button(root, text="Start (Ctrl+Shift+S)", command=start_clicking)
start_button.pack()

# Create the stop button
stop_button = Button(root, text="Stop (Ctrl+Shift+E)", command=stop_clicking)
stop_button.pack()

# Start the GUI event loop
root.mainloop()



"""
This code will create a GUI with two buttons, "Start" and "Stop". When the "Start" button is clicked,
or the keyboard shortcut Ctrl+Shift+S is pressed, the auto clicker will perform 100 clicks with a delay of 0.5 seconds
between each click. You can modify the num_clicks and delay variables to change the number of clicks and the delay between
clicks, respectively. The "Stop" button, or the keyboard shortcut Ctrl+Shift+E, will stop the auto clicking.

Please note that this code is just a simulation of an auto clicker and will not actually interact with anything on
your computer. It just prints "click" to the console to simulate

"""
