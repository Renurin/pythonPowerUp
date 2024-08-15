# Step 1: Open web browser

import webbrowser
import time
webbrowser.open('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(3)

# Step 2: Log in the system

import pyautogui
pyautogui.PAUSE = 0.5 # Pause between commands

pyautogui.press('tab')
pyautogui.write("calabreso@gmail.com")
pyautogui.press('tab')
pyautogui.write("tosk")
pyautogui.press('enter')

# Step 3: Import the database to get the products

import pandas as pd


