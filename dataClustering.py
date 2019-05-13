# Libraries
import pandas as pd

# -------------------------------------------------- Functions ---------------------------------------------------------
# Convert categorical variable into dummies
def variableToDummies(dataset, colname, finalName, legend):
    tempdummies = pd.get_dummies(dataset[colname])
    if legend:
        listposition = 1
        print(finalName+":")
        for i in tempdummies.columns:
            print("\t", listposition, "- "+i)
            listposition = listposition + 1

    element = 1
    for key, value in tempdummies.iterrows():
        for i, j in value.iteritems():
            if j == 1:
                # tempdummies.at[key, i] = element
                # print("Value changed")
                tempdummies.at[key, "temp_summary_272727"] = int(element)
                # print("Value added")
            element = element + 1
        element = 1

    tempdummies.fillna(0, inplace=True)
    dataset.drop([colname], axis=1, inplace=True)
    dataset[finalName] = tempdummies["temp_summary_272727"]

    return dataset

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
              "Occurred_On", "Occurred_On_Time",
              "Created_On", "Created_On_Time", "Created_On_Date",
              "Informed_On", "Informed_On_Date"], axis=1, inplace=True)

# Convert categorical into dummy variables
dataset = variableToDummies(dataset, "Reason", "Delay_Reason", True)
# TODO: convert rest of categorical variables into dummy ;)

dataset[["Schools_NOT_Notified", "Schools_Notified"]] = pd.get_dummies(dataset['Has_Contractor_Notified_Schools'])
dataset[["Parents_NOT_Notified", "Parents_Notified"]] = pd.get_dummies(dataset['Has_Contractor_Notified_Parents'])

# Remove categorical variables
dataset.drop(["Has_Contractor_Notified_Schools", "Schools_NOT_Notified",
              "Has_Contractor_Notified_Parents", "Parents_NOT_Notified"], axis=1, inplace=True)

# ---------------------------------------------------- K-Means ---------------------------------------------------------
# TODO: k-means clustering

# ----------------------------------------------- Affinity Propagation -------------------------------------------------
# TODO: affinity propagation

print("END")


