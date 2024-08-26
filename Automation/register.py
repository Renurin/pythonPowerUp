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
products = pd.read_csv("C:\\Users\\Renan\\Desktop\\Pasta_do_Renan_=)\\Python\\pythonPowerUp\\pythonPowerUp\\Automation\\produtos.csv") # insert full path (not gonna commit path)


# Step 4: Record a product in the website
for line in products.index:
    pyautogui.click(x=964, y=244)
    code = products.loc[line,"codigo"]
    pyautogui.write(str(code))

    pyautogui.press('tab')
    brand = products.loc[line,"marca"]
    pyautogui.write(str(brand))

    pyautogui.press('tab')
    typeProduct = products.loc[line,"tipo"]
    pyautogui.write(str(typeProduct))

    pyautogui.press('tab')
    category = products.loc[line,"categoria"]
    pyautogui.write(str(category))

    pyautogui.press('tab')
    price = products.loc[line,"preco_unitario"]
    pyautogui.write(str(price))

    pyautogui.press('tab')
    cost = products.loc[line,"custo"]
    pyautogui.write(str(cost))

    pyautogui.press('tab')
    obs = products.loc[line, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab')
    pyautogui.press('enter')

    # Scroll all the way up
    pyautogui.scroll(5000)

    # Step 5: Loop