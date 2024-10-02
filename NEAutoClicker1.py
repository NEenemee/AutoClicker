# Attempt to make an auto clicker using Python

# Time and threading import
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener

# Messages for user
start_msg = "Welcome to my autoclicker application by Nick Eliopoulos"
sec_msg = "To exit the application press F6. To start the auto clicker press F8."
thd_msg = "Type how fast you would like to have the button pressed (in seconds): "


button = Button.left
start_stop_key = Key.f8
stop_app_key = Key.f6

# Function to get user input with error handling
def get_user_input():
    while True:
        try:
            input_delay = float(input(thd_msg))
            return input_delay
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get the delay input
print(start_msg, sec_msg)
delay = get_user_input()

# Used to control clicks
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    print("App is ready to be used.")    

    def start_clicking(self):
        self.running = True
        print("App is Running")

    def stop_clicking(self):
        self.running = False
        print("App is Stopped")

    def exit(self):
        if self.running == True:
            self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

# Instance of mouse controller is created 
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

# On press method to take a key as argument
def on_press(key):
    try:
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == stop_app_key:
            click_thread.exit()
            listener.stop()
    except Exception as e:
        print(f"An error occurred: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()
