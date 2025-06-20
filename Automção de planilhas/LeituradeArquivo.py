from openpyxl import load_workbook

wb = load_workbook(filename="nomes.xlsx") #carrega o arquivo xlsx

planilha = wb['Planilha1'] #acessa a planilha do arq

for i in range(2,5): #loop para printar os dados da planilha em um texto
    print("%s tem %s anos." % (planilha['A%s' % i].value, planilha['B%s' % i].value))