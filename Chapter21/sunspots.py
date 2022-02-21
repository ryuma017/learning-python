from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

# 太陽の黒点データ
data = [
#    Year  Month  Predicted  High  Low
    (2019, 10,    3.4,       10.4, 0,0),
    (2019, 11,    3.2,       11.2, 0,0),
    (2019, 12,    3.1,       12.1, 0,0),
    (2020,  1,    3.3,       12.3, 0,0),
    (2020,  2,    3.4,       13.4, 0,0),
    (2020,  3,    3.4,       13.4, 0,0),
    (2020,  4,    3.0,       13.0, 0,0),
    (2020,  5,    2.8,       12.8, 0,0),
    (2020,  6,    2.6,       12.6, 0,0),
    (2020,  7,    2.4,       12.4, 0,0),
]

drawing = Drawing(400, 250)

pred  = [row[2] for row in data]
high  = [row[3] for row in data]
low   = [row[4] for row in data]
times = [row[0] + row[1] / 12 for row in data]

print(pred)
print(high)
print(low)
print(times)

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [
    list(zip(times, pred)),
    list(zip(times, high)),
    list(zip(times, low))
    ]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)

drawing.add(String(250, 200, "Sunspots", fontsize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, "report.pdf", "Sunspots")