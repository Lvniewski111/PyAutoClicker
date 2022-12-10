import tkinter as tk
import time
import pyautogui

# define mouse tracking
def getMousePosition():
    pyautogui.displayMousePosition()
    coords = pyautogui.position()
    return coords


# define the start_clicking function
def start_clicking():
    global is_clicking
    is_clicking = True

    # start a loop that simulates clicking every half second
    while is_clicking:
        time.sleep(1.0)  
        pyautogui.click()
        print("click!")

# define the stop_clicking function
def stop_clicking():
    global is_clicking
    is_clicking = False

# create the root window
root = tk.Tk()
root.title("AutoClicker")

# set the minimum size of the window
root.minsize(400, 200)

# create the main frame
frame = tk.Frame(root)
frame.pack()

# create the start button and assign it the keyboard shortcut "s"
start_button = tk.Button(frame, text="START", command=start_clicking, font= ('Helvetica 20 bold'))
start_button.pack()
root.bind("<s>", start_clicking)

# create the stop button and assign it the keyboard shortcut "t"
stop_button = tk.Button(frame, text="STOP", command=stop_clicking, font= ('Helvetica 20 bold'))
stop_button.pack()
root.bind("<t>", stop_clicking)

# create the quit button and assign it the keyboard shortcut "q"
quit_button = tk.Button(frame, text="QUIT", command=root.quit, font= ('Helvetica 20 bold'))
quit_button.pack()
root.bind("<q>", root.quit)

# start the GUI event loop
root.mainloop()
