from openpyxl import load_workbook

nome_arq = "book.xlsx"
wb = load_workbook(filename=nome_arq)

ws = wb['Data']

ws.delete_rows(1, 3)


ws.delete_cols(1,5)

wb.save(filename=nome_arq)