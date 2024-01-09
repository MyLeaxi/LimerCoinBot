import pyautogui
import time
import os
import cv2
import random
import keyboard
import numpy as np

input("Başlıyoruz (Enter'a basın.)")

print("Geri sayım bitti!")
os.system("cls")
def show_banner():
    banner = r'''
 _                     _ 
| |                   (_)
| |     ___  __ ___  ___ 
| |    / _ \/ _` \ \/ / |
| |___|  __/ (_| |>  <| |
|______\___|\__,_/_/\_\_|
    
  Limercoin Auto Game Bot =)
  Discord.gg/7WAe2ySZNN
  '''

    terminal_genislik = os.get_terminal_size().columns
    metin_genislik = max(len(satir) for satir in banner.splitlines())
    bosluk_miktari = (terminal_genislik - metin_genislik) // 2
    for satir in banner.splitlines():
        print(' ' * bosluk_miktari + satir)

show_banner()
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("Geri sayım bitti!")
os.system("title ByLeaxi - Discord.gg/7WAe2ySZNN")

def perform_actions():
    game_image_path = 'ff/Game.png'
    start_image_path = 'ff/Start.png'
    play_image_path = 'ff/Play.png'
    fins_image_path = 'ff/fins.png'
    res_image_path = 'ff/res.png'
    second_image_path = 'ff/Coin.png'
    third_image_path = 'ff/Puzzle.png'
    fourth_image_path = 'ff/2048.png'
    btc_image_path = 'ff/Coin/btc.png'
    eth_image_path = 'ff/Coin/eth.png'
    bnb_image_path = 'ff/Coin/bnb.png'
    x_image_path = 'ff/Coin/x.png'

    location = pyautogui.locateOnScreen(game_image_path, confidence=0.8)

    if location:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        time.sleep(1)

        time.sleep(3)
        
        play_locations = list(pyautogui.locateAllOnScreen(play_image_path, confidence=0.8))
        if play_locations:
            random_location = random.choice(play_locations)
            px, py = pyautogui.center(random_location)
            pyautogui.click(px, py)
        else:
            print("Play düğmesi bulunamadı.")
    else:
        print("Oyun başlatma düğmesi bulunamadı.")



    time.sleep(1)
    second_location = pyautogui.locateOnScreen(second_image_path, confidence=0.8)
    third_location = pyautogui.locateOnScreen(third_image_path, confidence=0.8)
    fourth_location = pyautogui.locateOnScreen(fourth_image_path, confidence=0.8)

    if second_location:
        print("(COIN CATCHER) Oynanıyor ")
        time.sleep(1)
        start = pyautogui.locateOnScreen(start_image_path, confidence=0.8)
        if start:
            px, py = pyautogui.center(start)
            pyautogui.click(px, py)
        time.sleep(1)

        while True:
            fins = pyautogui.locateOnScreen(fins_image_path, confidence=0.6)
            res = pyautogui.locateOnScreen(res_image_path, confidence=0.6)
            btc = pyautogui.locateOnScreen(btc_image_path, confidence=0.9)
            eth = pyautogui.locateOnScreen(eth_image_path, confidence=0.9)
            bnb = pyautogui.locateOnScreen(bnb_image_path, confidence=0.9)
            x = pyautogui.locateOnScreen(x_image_path, confidence=0.9)

            if fins is not None:
                px, py = pyautogui.center(fins)
                pyautogui.click(px, py)
                time.sleep(10)
                break
            if res is not None:
                break
            if btc is not None:
                x, y = pyautogui.center(btc)
                pyautogui.click(x, y + 30)
            elif eth is not None:
                x, y = pyautogui.center(eth)
                pyautogui.click(x, y + 30)
            elif bnb is not None:
                x, y = pyautogui.center(bnb)
                pyautogui.click(x, y + 30)
            elif x is not None:
                x, y = pyautogui.center(x)
                pyautogui.click(x, y + 30)

            time.sleep(0.1)

    elif third_location:
        print("(COIN PUZZLE) Bakım Aşamasında ")
        pass
    elif fourth_location:
        print("(2048) Oynanıyor ")
        start = pyautogui.locateOnScreen(start_image_path, confidence=0.8)
        if start:
            px, py = pyautogui.center(start)
            pyautogui.click(px, py)
        while True:
            movements = ['right', 'down', 'left', 'up']
    
            for move in movements:
                keyboard.press(move)
                time.sleep(0.5)
                keyboard.release(move)
    
            fins = pyautogui.locateOnScreen(fins_image_path, confidence=0.6)
            res = pyautogui.locateOnScreen(res_image_path, confidence=0.6)
    
            if fins is not None:
                px, py = pyautogui.center(fins)
                pyautogui.click(px, py)
                time.sleep(10)
                break
    
            if res is not None:
                break
    else:
        print("Hiçbir Fotoğraf Bulunamadı.")

while True:
    perform_actions()
