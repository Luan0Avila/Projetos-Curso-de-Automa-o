from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

ws['A1'] = "Você vai ver uma imagem abaixo"

img = Image("logo.jpg")

ws.add_image(img, 'A2')

wb.save(filename="logo.xlsx")