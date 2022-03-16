import pandas as pa
import csv 
import plotly.graph_objects as pg

data = pa.read_csv("data.csv")

# print(data.groupby("level")["attempt"].mean())

fig = pg.Figure(pg.Bar(
    x=data.groupby("level")["attempt"].mean(),
    y= ["Level 1","Level 2","Level 3","level 4"],orientation='h'
))
fig.show()

df = pa.read_csv("data.csv")

student_df = df.loc[df['student_id'] == "TRL_abc"]

print(student_df.groupby("level")["attempt"].mean())

fig1 = pg.Figure(pg.Bar(
            x=student_df.groupby("level")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation='h'))

fig1.show()

