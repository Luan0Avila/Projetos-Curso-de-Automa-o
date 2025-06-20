from openpyxl import Workbook

wb = Workbook() #cria uma instancia de objeto

nome_arquivo = "arquivo.xlsx" 

ws1 = wb.active #cria uma planilha no arquivo
ws1.title = "Planilha 1" #nomeia a planilha criada

dados = [ #cada array é uma linha dentro da planlha
    ['Ano','Lucro','Custos'],
    [2015, '30%', '40%'],
    [2016, '55%', '30%'],
    [2017, '90%', '70%'],
]

for linha in dados: #faz um loop para adicionar cada item do array na planilha
    ws1.append(linha)

ws2 = wb.create_sheet(title="Pi") #cria uma segunda planilha no arquivo
ws2['F5'] = 3.14  #adiciona um dado em uma célula especifica do arquivo


wb.save(filename=nome_arquivo) #salva a planilha