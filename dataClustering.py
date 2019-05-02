# Libraries
import numpy as np
import pandas as pd


# Dataset transformations
from pandas import DataFrame

dataset = pd.read_csv("data/bus-breakdown-and-delays.csv", dtype={"Incident_Number": str})
dataset.fillna(0, inplace=True)

# Data preprocessing
dataset.drop(["Incident_Number", "Last_Updated_On"], axis=1, inplace=True)

new1 = dataset["Occurred_On"].str.split(pat="T", n=1, expand=True)
dataset["Occurred_On_Date"] = new1[0]
dataset["Occurred_On_Time"] = new1[1]

new2 = dataset["Created_On"].str.split("T",n=1, expand=True)
dataset["Created_On_Date"]=new2[0]
dataset["Created_On_Time"]=new2[1]

print("END")