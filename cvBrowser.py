import cv2, pytesseract
from PIL import ImageGrab
import pyautogui
import time, os, threading, socket
import pandas as pd
import numpy as np



class CVBrowser:
    def __init__(self, browser="firefox", url="accounts.google.com", ref_file="google/google_stages.csv") -> None:
        threading.Thread(target=os.system, args = (f"firefox -private {url}", )).start()
        self.reference_file = pd.read_csv(ref_file)
        self.reference_file.dropna(inplace=True)
        self.stage = -1
        self.done = -1
        time.sleep(3)


    def grabImg(self):
        screen = np.array(ImageGrab.grab(xdisplay=':0.0'))
        return screen
    

    def __process_text(self, img, location):
        text = pytesseract.image_to_string(img).strip().replace("\n", " ")
        return (text.lower().strip(), location)


    def analyze(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        dilation = cv2.dilate(thresh, rect_kernel, iterations=1)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        text = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped = img[y:y+h, x:x+w]
            text.append(self.__process_text(cropped, (x,y,w,h)))
        return(text)

    
    def action(self, _text, stage, info="", clean=True):
        if stage==-1 or self.done == stage:
            return 0
        index = list(self.reference_file["stage"]).index(stage)
        identifier = str(list(self.reference_file["element"])[index]).lower()
        actions = str(list(self.reference_file["actions"])[index]).split(",")
        actions = [x.strip().lower() for x in actions]
        element = None
        for x in _text:
            if identifier in x[0]:
                element = x
        if not element: return 0
            
        if "select" in actions:
            pyautogui.moveTo(element[1][0]+element[1][2]/2, element[1][1]+element[1][3]/2)
            pyautogui.click()
            if clean:
                pyautogui.hotkey("ctrl", "a")
                pyautogui.press("backspace")
        if "username" in actions:
            if info:
                pyautogui.write(info)
            else: return 0
        if "password" in actions:
            if info:
                pyautogui.write(info)
            else: return 0
        if "enter" in actions:
            pyautogui.press("enter")
        if "end" in actions:
            return self.cleanup()
        self.done = stage
        return 1
        

    def detect_stage(self, _text):
        _text = [x[0] for x in _text]
        text = " ".join(_text)
        _text = []
        for i in range(len(self.reference_file["text"])):
            score = 0
            identifier = self.reference_file["text"][i].split("|;")
            identifier = [x.lower().strip() for x in identifier]
            for x in identifier:
                if x in text:
                    score += 1
            score /= len(identifier)
            _text.append((self.reference_file["stage"][i], score))
        _text.sort(key=lambda x: x[1])
        try:
            if _text[-1][1] == 0:
                return -1
        except IndexError:
            pass
        else:
            self.stage = _text[-1][0]
            return self.stage



#obj = CVBrowser()

if __name__ == "__main__":    
    while True:
        img = obj.grabImg()
        text = obj.analyze(img)
        stg = obj.detect_stage(text)
        obj.action(text, stg, "toshithh")
        print(stg)