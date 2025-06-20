from openpyxl import load_workbook

#Escolhendo o arquivo
dest_filename = 'book2.xlsx'
wb = load_workbook(filename=dest_filename)
ws = wb['Data']

#move a linha 2 de A à Z uma pra cima
ws.move_range("A2:Z2", rows=-1)


#movendo colunas
ws.move_range("F10:F10", cols=-2)

ws.move_range("C13:E15", cols=-2, rows=-1)

wb.save(filename=dest_filename)