from itertools import count
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.express as px
import random

df = pd.read_csv("BellCurve.csv")
df2 = pd.read_csv("Bellcurve.csv")

fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=True)

fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)

fig.show()
fig2.show()

count = []
diceResult = []

for i in range(0,100):

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    diceResult.append(dice1 + dice2)

    count.append(i)

fig3 = px.bar(x = diceResult, y = count)
fig3.show()

