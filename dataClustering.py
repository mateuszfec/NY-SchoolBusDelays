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
            print("\t", listposition, "-", i)
            listposition = listposition + 1
        print("")

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
# String multi-replacement
def multipleReplace(dataset, colname, phraseList, replace):
    for key in phraseList:
        dataset[colname] = dataset[colname].replace(key, replace)
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
# Remove unused data
dataset.drop(["Incident_Number", "Last_Updated_On", "Busbreakdown_ID", "Created_On", "Schools_Serviced"], axis=1, inplace=True)

# Get basic info about event (dates and time)
dataset[["Event_Date", "Occurred_On"]] = dataset["Occurred_On"].str.split("T", expand=True)
dataset["Informed_On"] = dataset["Informed_On"].str.split("T", expand=True)[1]

# Calculate time difference between occurred event and information
dataset["Occurred_On"] = pd.to_datetime(dataset["Occurred_On"])
dataset["Informed_On"] = pd.to_datetime(dataset["Informed_On"])
dataset["Reaction_Time"] = dataset["Informed_On"] - dataset["Occurred_On"]

# Bus corporation names unification
dataset["Bus_Company_Name"] = dataset["Bus_Company_Name"].str.split("(", expand=True)[0]
dataset["Bus_Company_Name"] = dataset["Bus_Company_Name"].str.strip()
multipleReplace(dataset, "Bus_Company_Name", {'ALL AMERICAN SCHOOL BUS C'}, "ALL AMERICAN SCHOOL BUS CORP.")
multipleReplace(dataset, "Bus_Company_Name", {'CAREFUL BUS'}, "CAREFUL BUS SERVICE INC")
multipleReplace(dataset, "Bus_Company_Name", {'CONSOLIDATED BUS TRANS. I', 'CONSOLIDATED BUS TRANSIT, INC.'}, "CONSOLIDATED BUS TRANS. INC.")
multipleReplace(dataset, "Bus_Company_Name", {'Don Thomas Buses'}, "DON THOMAS BUSES, INC.")
multipleReplace(dataset, "Bus_Company_Name", {'EMPIRE CHARTER SERVICE IN'}, "EMPIRE CHARTER SERVICE INC")
multipleReplace(dataset, "Bus_Company_Name", {'FIRST STEPS', 'FIRST STEPS TRANS, INC', 'FIRST STEPS TRANSP INC.'}, "FIRST STEPS TRANS INC.")
multipleReplace(dataset, "Bus_Company_Name", {'G.V.C., LTD.'}, "G.V.C. LTD.")
multipleReplace(dataset, "Bus_Company_Name", {'L & M BUS CORP'}, "L & M BUS CORP.")
multipleReplace(dataset, "Bus_Company_Name", {'LEESEL TRANSP CORP'}, "LEESEL TRANSPORTATION CORP")
multipleReplace(dataset, "Bus_Company_Name", {'LOGAN TRANSPORTATION SYST'}, "LOGAN TRANSPORTATION SYSTEMS")
multipleReplace(dataset, "Bus_Company_Name", {'LORINDA ENT. LTD.'}, "LORINDA ENTERPRISES, LTD.")
multipleReplace(dataset, "Bus_Company_Name", {'MONTAUK STUDENT TRANS LLC'}, "MONTAUK STUDENT TRANS, INC.")
multipleReplace(dataset, "Bus_Company_Name", {'MJT BUS'}, "MJT BUS COMPANY, INC")
multipleReplace(dataset, "Bus_Company_Name", {'MONTAUK STUDENT TRANS, IN'}, "MONTAUK STUDENT TRANS, INC.")
multipleReplace(dataset, "Bus_Company_Name", {'PIONEER TRANSPORTATION CO'}, "PIONEER TRANSPORTATION CORP")
multipleReplace(dataset, "Bus_Company_Name", {'QUALITY TRANSPORTATION CO'}, "QUALITY TRANSPORTATION CORP.")
multipleReplace(dataset, "Bus_Company_Name", {'RELIANT TRANS, INC.'}, "RELIANT TRANSPORTATION, INC")
multipleReplace(dataset, "Bus_Company_Name", {'SELBY TRANS CORP.','SELBY TRANSPORTATION'}, "SELBY TRANSPORTATION CORP")
multipleReplace(dataset, "Bus_Company_Name", {'THIRD AVENUE TRANSIT'}, "THIRD AVENUE TRANSIT, INC")
multipleReplace(dataset, "Bus_Company_Name", {'THOMAS BUSES, INC.'}, "THOMAS BUSES INC")

# Convert categorical into dummy variables
dataset = variableToDummies(dataset, "Reason", "Delay_Reason", True)
dataset = variableToDummies(dataset, "School_Age_or_PreK", "School_Level", True)
dataset = variableToDummies(dataset, "Breakdown_or_Running_Late", "Delay_Result", True)
dataset = variableToDummies(dataset, "Bus_Company_Name", "Bus_Company", True)
dataset = variableToDummies(dataset, "Boro", "Boro", True)
dataset = variableToDummies(dataset, "Route_Number", "Route_Number", False)
dataset = variableToDummies(dataset, "Bus_No", "Bus_Number", False)
dataset = variableToDummies(dataset, "Run_Type", "Bus_Run_Type", True)
dataset = variableToDummies(dataset, "School_Year", "School_Year", True)

dataset[["Schools_NOT_Notified", "Schools_Notified"]] = pd.get_dummies(dataset['Has_Contractor_Notified_Schools'])
dataset[["Parents_NOT_Notified", "Parents_Notified"]] = pd.get_dummies(dataset['Has_Contractor_Notified_Parents'])
dataset[["OPT_NOT_Alerted", "OPT_Alerted"]] = pd.get_dummies(dataset['Have_You_Alerted_OPT'])
# TODO: Check is possible to not create temp "NOT" columns

# Remove categorical and dummy helper variables
dataset.drop(["Has_Contractor_Notified_Schools", "Schools_NOT_Notified",
              "Has_Contractor_Notified_Parents", "Parents_NOT_Notified",
              "Have_You_Alerted_OPT", "OPT_NOT_Alerted"], axis=1, inplace=True)

# Set right format of the date type data
dataset[["School_Year", "School_Level", "Delay_Reason", "Delay_Result", "Boro", "Route_Number", "Bus_Company",
         "Bus_Number", "Bus_Run_Type"]] = dataset[["School_Year", "School_Level", "Delay_Reason", "Delay_Result",
                                                   "Boro", "Route_Number", "Bus_Company", "Bus_Number",
                                                   "Bus_Run_Type"]].astype(int)

dataset["Occurred_On"] = pd.to_datetime(dataset["Occurred_On"], format="%H:%M:%S").dt.time
dataset["Informed_On"] = pd.to_datetime(dataset["Informed_On"], format="%H:%M:%S").dt.time

# Delays data preprocessing
# TODO: Set-up the final data of the bus delays

# Final dataset structure
dataset = dataset.rename(columns={'Number_Of_Students_On_The_Bus': 'Students_Number'})
dataset["Students_Number"] = dataset["Students_Number"].astype(int)

dataset = dataset[['How_Long_Delayed',
                   'Event_Date',
                   'Occurred_On',
                   'Informed_On',
                   'Reaction_Time',
                   'Students_Number',
                   'School_Year',
                   'School_Level',
                   'Delay_Reason',
                   'Delay_Result',
                   'Boro',
                   'Route_Number',
                   'Bus_Company',
                   'Bus_Number',
                   'Bus_Run_Type',
                   'OPT_Alerted',
                   'Schools_Notified',
                   'Parents_Notified']]

# print(dataset.dtypes)

# ---------------------------------------------------- K-Means ---------------------------------------------------------
# TODO: k-means clustering

# ----------------------------------------------- Affinity Propagation -------------------------------------------------
# TODO: affinity propagation

print("END")