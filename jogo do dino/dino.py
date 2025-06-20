from PIL import ImageGrab
import pyautogui


def isCollision(data):
    """Função que faz o dino pular"""
    for x in range(750, 790): # verifica o eixo x
        for y in range(290, 330): # verifica o exio y
            if data[x, y] < 100: # verifica se o exio x e y são menores que 100 caso sim executa a função de pulo 
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