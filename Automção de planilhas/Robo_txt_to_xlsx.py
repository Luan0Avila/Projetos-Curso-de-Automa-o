from openpyxl import Workbook

print("Iniciando robô...")
print("Lendo dados do txt")
file_txt = open("gastos.txt", "r", encoding="utf-8") #abre o txt

arq = file_txt.read() # lê o txt

list_datas = arq.splitlines()

for i in range(0, len(list_datas)): #separa as linhas do txt para criar a planilha
    list_datas[i] = list_datas[i].split(",")

#criando o xlsx
print("Criando xlsx")
wb = Workbook()
ws = wb.active

for row in list_datas: #adicionando dados do txt ao xlsx
    ws.append(row)

print("Salvando o xlsx")
wb.save('gastos.xlsx') # salvando o arquivo

