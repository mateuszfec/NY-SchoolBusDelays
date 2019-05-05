# Libraries
import numpy as np
import pandas as pd


# Dataset transformations
from pandas import DataFrame

dataset = pd.read_csv("data/bus-breakdown-and-delays.csv", dtype={"Incident_Number": str})
dataset.fillna(0, inplace=True)

# Data preprocessing
dataset.drop(["Incident_Number", "Last_Updated_On"], axis=1, inplace=True)

# Occurred_On splitting
new1 = dataset["Occurred_On"].str.split(pat="T", n=1, expand=True)
dataset["Occurred_On_Date"] = new1[0]
dataset["Occurred_On_Time"] = new1[1]

# Created_On splitting
new2 = dataset["Created_On"].str.split("T",n=1, expand=True)
dataset["Created_On_Time"] = new2[1]

# Informed_On splitting
new3 = dataset["Informed_On"].str.split("T", n=1, expand=True)
dataset["Informed_On_Time"] = new3[1]

dataset.drop(["Occurred_On", "Created_On", "Informed_On"], axis=1, inplace=True)
dataset.rename(columns={'Occurred_On_Date': 'Event Date'}, inplace=True)

dataset["Occurred_On_Time"] = pd.to_datetime(dataset["Occurred_On_Time"])
dataset["Created_On_Time"] = pd.to_datetime(dataset["Created_On_Time"])

dataset["Reaction Time"] = dataset["Created_On_Time"]-dataset["Occurred_On_Time"]
dataset.drop(["Occurred_On_Time", "Created_On_Time"], axis=1, inplace=True)

#potrzebne jest przekonwertowanie tego na dummies (bo wtedy będą ciągłe) ale coś u mnie się sypie
pd.get_dummies(dataset)
# w zasadzie wszystkie zmienne tutaj są jakościowe (w sensie że nie ma jak dla nich wyliczyć statystyk opisowych)
# tylko przeszkadza ta kolumna z czasem trwania bo jest ona strasznie nieregularnie zrobiona

#TO DO:
#k-means clustering
#affinity propagation

#print(dataset.dtypes)
print("END")