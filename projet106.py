import csv
import plotly.express as px

marks = []
presence = []

with open ("marksvspresence.csv") as f :
    df = csv.DictReader (f)
    for row in df:
        marks.append(float( row["Marks In Percentage"]))
        presence.append(float(row["Days Present"]))
    
    fig = px.scatter(x=presence,y=marks)
    fig.show()

import numpy as np
corcoef = np.corrcoef(marks,presence)
print(corcoef[0,1])

