import plotly.express as px
import csv
import numpy as np
with open("project.csv") as csvfile:
    df = csv.DictReader(csvfile)
    fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
    fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Days Present"]))
            cold_drink_sales.append(float(row["Marks In Percentage"]))

    return {"x" : ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation Value is",correlation)
def setup():
    dataPath = "project.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
setup()

