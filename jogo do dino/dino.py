from PIL import ImageGrab
import pyautogui

def isCollision(data):
    for i in range(750, 790):
        for j in range(290, 330):
            if data[i, j] < 100:
                print("Pulando")
                pyautogui.keyDown("up")
                return
    return

while True:
    """Tira os prints da tela"""
    image = ImageGrab.grab().convert("L")
    data = image.load()
    isCollision(data)
    


    #image.show()
    #break;