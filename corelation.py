import csv
import plotly.express as px

coffee = []
sleep = []
with open("coffee_hours.csv") as f :
    df = csv.DictReader(f)
    for row in df:
        coffee.append(float(row["Coffee in ml"]))
        sleep.append(float(row["sleep in hours"]))
    
    fig =px.scatter(x=coffee,y=sleep)
    fig.show()


import numpy as np
corelation = np.corrcoef(coffee,sleep)
print(corelation[0,1])