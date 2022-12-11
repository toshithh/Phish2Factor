import pyautogui
import os
import time
from PIL import ImageGrab
import pytesseract
from pytesseract import Output

def web_exec(unm, pswd):
    os.system("start msedge -inprivate https://accounts.google.com --start-fullscreen ")

    w,h = pyautogui.size()
    time.sleep(2)
    pyautogui.press('f11')
    time.sleep(2)
    pyautogui.typewrite(f"{unm}\n")
    time.sleep(3.2)
    pyautogui.typewrite(f"{pswd}\n")
    time.sleep(3.2)
    pytesseract.pytesseract.tesseract_cmd = (r"C:/Program Files/Tesseract-OCR/tesseract") # needed for Windows as OS
    screen =  ImageGrab.grab()  # screenshot
    cap = screen.convert('L')   # make grayscale

    data=pytesseract.image_to_boxes(cap,output_type=Output.DICT)
    string = "".join(data['char'])
    if "StepVerification" in string:
        if "Googlesentanotification" in string:
            return 1
        if "OTP" in string:
            return 2
        else:
            return 1
    else: return 0