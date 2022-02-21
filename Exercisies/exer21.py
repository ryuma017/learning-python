from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

population = []
pop_men = []
pop_women = []
year_1 = []

pop_15to19 = []
year_2 = []

file = open("c03_aichi_utf8.csv", "r")
for line in file:
    zlist = line.split(",")
    if "総数" == zlist[2]:
        population.append(int(zlist[6]))
        pop_men.append(int(zlist[7]))
        pop_women.append(int(zlist[8]))
        year_1.append(int(zlist[5]))

    if "15～19歳" == zlist[2]:
        pop_15to19.append(int(zlist[6]))
        year_2.append(int(zlist[5]))

drawing = Drawing(400, 450)

print(population)
print(pop_men)
print(pop_women)
print(year_1)

print(pop_15to19)
print(year_2)

lp_1 = LinePlot()
lp_1.x = 50
lp_1.y = 250
lp_1.height = 125
lp_1.width = 300
lp_1.data = [
    list(zip(year_1, population)),
    list(zip(year_1, pop_men)),
    list(zip(year_1, pop_women))
    ]
lp_1.lines[0].strokeColor = colors.green
lp_1.lines[1].strokeColor = colors.blue
lp_1.lines[2].strokeColor = colors.red

lp_2 = LinePlot()
lp_2.x = 50
lp_2.y = 50
lp_2.height = 125
lp_2.width = 300
lp_2.data = [list(zip(year_2, pop_15to19))]
lp_2.lines[0].strokeColor = colors.green

drawing.add(lp_1)
drawing.add(lp_2)

drawing.add(String(150, 420, "Population Trends of Aichi", fontsize=30, fillColor=colors.black))
drawing.add(String(140, 400, "green:total blue:men red:women", fontsize=15, fillColor=colors.black))
drawing.add(String(150, 200, "Population Trends of Aichi 15-19", fontsize=30, fillColor=colors.black))
renderPDF.drawToFile(drawing, "exer21.pdf", "Population")