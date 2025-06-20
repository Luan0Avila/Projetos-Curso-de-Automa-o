from openpyxl import Workbook
from openpyxl.chart import (
    AreaChart, 
    Reference, 
    Series
)
#cria a planilha
wb = Workbook()
ws = wb.active

rows = [
    ['Ano', 'Lucro', 'Custos'],
    [2015, 40, 30],
    [2016, 40, 25],
    [2017, 50, 35],
    [2018, 60, 25],
    [2019, 55, 45],
    [2020, 65, 40]
]

#adiciona os dados na planilha
for row in rows:
    ws.append(row)

#cria o grafico
chart = AreaChart()
chart.title = "Lucros x Custos"
chart.style = 13
chart.x_axis.title = "Ano"
chart.y_axis.title = "Porcecntagem"

#passa os anos dos dados
categorias = Reference(ws, min_col=1, min_row=1, max_row=6)
#passa os lucros e custos dos dados
dados = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=6)

#adicioona esses dados ao grafico
chart.add_data(dados, titles_from_data=False)
chart.set_categories(categorias)

#adiciona o grafico a planilha
ws.add_chart(chart, "A10")

wb.save(filename="chart.xlsx")

