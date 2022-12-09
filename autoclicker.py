import tkinter as tk
import time

# define the start_clicking function
def start_clicking():
    global is_clicking
    is_clicking = True

    # start a loop that simulates clicking every half second
    while is_clicking:
        time.sleep(0.5)
        # simulate a mouse click
        # (replace this with the actual code to click the mouse)
        print("click!")

# define the stop_clicking function
def stop_clicking():
    global is_clicking
    is_clicking = False

# create the root window
root = tk.Tk()
root.title("AutoClicker")

# set the minimum size of the window
root.minsize(400, 400)

# create the main frame
frame = tk.Frame(root)
frame.pack()

# create the start button and assign it the keyboard shortcut "s"
start_button = tk.Button(frame, text="Start", command=start_clicking)
start_button.pack()
root.bind("<s>", start_clicking)

# create the stop button and assign it the keyboard shortcut "t"
stop_button = tk.Button(frame, text="Stop", command=stop_clicking)
stop_button.pack()
root.bind("<t>", stop_clicking)

# create the quit button and assign it the keyboard shortcut "q"
quit_button = tk.Button(frame, text="Quit", command=root.quit)
quit_button.pack()
root.bind("<q>", root.quit)

# start the GUI event loop
root.mainloop()
