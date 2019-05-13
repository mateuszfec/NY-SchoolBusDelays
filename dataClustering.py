# Libraries
import pandas as pd

# ------------------------------------------------- Data import --------------------------------------------------------
# Sample data
sampleData = True
sampleHeight = 0.035

# Full data
fullData = pd.read_csv("data/bus-breakdown-and-delays.csv", dtype={"Incident_Number": str})
fullData.fillna(0, inplace=True)

if sampleData:
    dataset = fullData.sample(frac=sampleHeight)
else:
    dataset = fullData

# print(dataset.count)

# ---------------------------------------------- Data preprocessing ----------------------------------------------------
# Split dates and time
dataset[["Event Date", "Occurred_On_Time"]] = dataset["Occurred_On"].str.split("T", expand=True)
dataset[["Created_On_Date", "Created_On_Time"]] = dataset["Created_On"].str.split("T", expand=True)
dataset[["Informed_On_Date", "Informed_On_Time"]] = dataset["Informed_On"].str.split("T", expand=True)

# Set right format of the data
dataset["Occurred_On_Time"] = pd.to_datetime(dataset["Occurred_On_Time"])
dataset["Created_On_Time"] = pd.to_datetime(dataset["Created_On_Time"])

# Calculate difference between event occurred time and system creation time
dataset["Reaction_Time"] = dataset["Created_On_Time"]-dataset["Occurred_On_Time"]

# Remove unused data
dataset.drop(["Incident_Number",
              "Last_Updated_On",
              "Occurred_On",
              "Occurred_On_Time",
              "Created_On",
              "Created_On_Time",
              "Informed_On",
              "Created_On_Date",
              "Informed_On_Date"], axis=1, inplace=True)




#potrzebne jest przekonwertowanie tego na dummies (bo wtedy będą ciągłe) ale coś u mnie się sypie
pd.get_dummies(dataset)
# w zasadzie wszystkie zmienne tutaj są jakościowe (w sensie że nie ma jak dla nich wyliczyć statystyk opisowych)
# tylko przeszkadza ta kolumna z czasem trwania bo jest ona strasznie nieregularnie zrobiona


# ---------------------------------------------------- K-Means ---------------------------------------------------------
# TODO: k-means clustering

# ----------------------------------------------- Affinity Propagation -------------------------------------------------
# TODO: affinity propagation

print("END")