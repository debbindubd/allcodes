import pyautogui
import time

# Allow some time to switch to the Facebook conversation window
print("You have 5 seconds to switch to the Facebook conversation window...")
time.sleep(5)

# Function to send the message with a counter
def send_message(counter):
    message = f"😥 ({counter})"
    pyautogui.typewrite(message)
    pyautogui.press("enter")

# Initialize the counter
counter = 1

# Send the message every 5 seconds
try:
    while True:
        send_message(counter)
        counter += 1
        time.sleep(5)
except KeyboardInterrupt:
    print("Script stopped by user")