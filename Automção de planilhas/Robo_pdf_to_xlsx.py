from PyPDF2 import PdfReader
from openpyxl import Workbook

pdf_file = open("gastos.pdf", "rb") #abre o arquivo no modo de leitura

read_pdf = PdfReader(pdf_file) #usa a biblioteca para ler o pdf

number_of_pages = len(read_pdf.pages) # pega o numero de páginas do pdf

page = read_pdf.pages[0] # vai na pagina escolhida do pdf

page_content = page.extract_text() #extrai o conteudo

parsed = page_content.splitlines() #transforma o texto em lista

list_datas = []
for line in parsed:
    parts = line.strip().split()
    # Detecta o cabeçalho pela presença das palavras-chave
    if "Tipo" in parts and "Valor" in parts and "Pagamento" in parts:
        list_datas.append(["Tipo", "Valor", "Forma de Pagamento"])

    if len(parts) == 3:
        list_datas.append(parts)


wb = Workbook()
ws = wb.active

for row in list_datas:
    ws.append(row)

wb.save(filename="gastos.xlsx")

print(list_datas)