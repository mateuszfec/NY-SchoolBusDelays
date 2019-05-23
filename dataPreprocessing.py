# Libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import re

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
    # TODO: Check is possible to return column with datatype (int32)
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
delaysOutliers = 6
studentsOutliers = 3

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
multipleReplace(dataset, "Bus_Company_Name", {'`', 'Ms.', '1967', '1992'}, "Unknown")
multipleReplace(dataset, "Bus_Company_Name", {'ALL AMERICAN SCHOOL BUS C'}, "ALL AMERICAN SCHOOL BUS CORP.")
multipleReplace(dataset, "Bus_Company_Name", {'CAREFUL BUS'}, "CAREFUL BUS SERVICE INC")
multipleReplace(dataset, "Bus_Company_Name", {'CONSOLIDATED BUS TRANS. I', 'CONSOLIDATED BUS TRANSIT, INC.'}, "CONSOLIDATED BUS TRANS. INC.")
multipleReplace(dataset, "Bus_Company_Name", {'Don Thomas Buses', 'DON THOMAS BUSES'}, "DON THOMAS BUSES, INC.")
multipleReplace(dataset, "Bus_Company_Name", {'EMPIRE CHARTER SERVICE IN'}, "EMPIRE CHARTER SERVICE INC")
multipleReplace(dataset, "Bus_Company_Name", {'FIRST STEPS', 'FIRST STEPS TRANS, INC', 'FIRST STEPS TRANSP INC.'}, "FIRST STEPS TRANS INC.")
multipleReplace(dataset, "Bus_Company_Name", {'G.V.C., LTD.', 'GVC LTD.'}, "G.V.C. LTD.")
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
multipleReplace(dataset, "Bus_Company_Name", {'SELBY TRANS CORP.', 'SELBY TRANSPORTATION'}, "SELBY TRANSPORTATION CORP")
multipleReplace(dataset, "Bus_Company_Name", {'SMART PICK'}, "SMART PICK INC")
multipleReplace(dataset, "Bus_Company_Name", {'phillip bus service'}, "PHILLIPS BUS SERVICE")
multipleReplace(dataset, "Bus_Company_Name", {'THIRD AVENUE TRANSIT'}, "THIRD AVENUE TRANSIT, INC")
multipleReplace(dataset, "Bus_Company_Name", {'THOMAS BUSES, INC.'}, "THOMAS BUSES INC")

# Convert categorical into dummy variables
multipleReplace(dataset, "Reason", {'0'}, "Unknown")
dataset = variableToDummies(dataset, "Reason", "Delay_Reason", True)
dataset = variableToDummies(dataset, "School_Age_or_PreK", "School_Level", True)
dataset = variableToDummies(dataset, "Breakdown_or_Running_Late", "Delay_Result", True)
dataset = variableToDummies(dataset, "Bus_Company_Name", "Bus_Company", True)
multipleReplace(dataset, "Boro", {0}, "Unknown")
dataset = variableToDummies(dataset, "Boro", "Boro", True)
dataset = variableToDummies(dataset, "Route_Number", "Route_Number", False)
dataset = variableToDummies(dataset, "Bus_No", "Bus_Number", False)
multipleReplace(dataset, "Run_Type", {'0'}, "Unknown")
dataset = variableToDummies(dataset, "Run_Type", "Bus_Run_Type", True)
dataset = dataset[dataset['School_Year'] != '2019-2020']
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

# Delays data preprocessing (hours)
hours = dataset['How_Long_Delayed'].str.split('(h|H)', expand=True)
hours.fillna(0, inplace=True)
hours['hours_summary'] = hours[0].where(hours[1] != 0, 0).str.strip()
dataset['Delay_From_Hours'] = hours['hours_summary']
del hours

multipleReplace(dataset, "Delay_From_Hours", {'0', '45 -1', "45-1", ''}, "0")
multipleReplace(dataset, "Delay_From_Hours", {'1/2', '30MINS-1'}, "30")
multipleReplace(dataset, "Delay_From_Hours", {'1', '1-', "1:00", "1:", "one", "ONE", 'I', "\\1", "MORE T", '45minTO 1'}, "60")
multipleReplace(dataset, "Delay_From_Hours", {'1 1/2', '1.5', "1:30", "30MINS-1"}, "90")
multipleReplace(dataset, "Delay_From_Hours", {'40-1', "40/1"}, "100")
multipleReplace(dataset, "Delay_From_Hours", {'1:45', "45 MIN/1", "45 min-1", "45/1", "451", "45MIN-1",
                                        "45min -1", '45min - 1', "45min-1", "45min/1", "45mini/1", "45mins 1"}, "105")
multipleReplace(dataset, "Delay_From_Hours", {'50-1', "50min 1"}, "110")
multipleReplace(dataset, "Delay_From_Hours", {'2', "2.0", "2:"}, "120")
multipleReplace(dataset, "Delay_From_Hours", {'3'}, "180")
multipleReplace(dataset, "Delay_From_Hours", {'4'}, "240")
dataset["Delay_From_Hours"].fillna(0, inplace=True)
dataset["Delay_From_Hours"] = dataset["Delay_From_Hours"].astype(int)
# test = variableToDummies(dataset, "full_hours", "test_sample", True)

# Delays data preprocessing (minutes)
minutes = dataset['How_Long_Delayed'].str.split('(m|M)', expand=True)
minutes.fillna(0, inplace=True)
minutes['minutes_stripped'] = minutes[0].where(minutes[1] != 0, 0).str.strip(' AaPp:+-_,n!?*&?SONiol.')
minutes.fillna(0, inplace=True)

r = re.compile(r'[0-9].*(-|:).*[0-9]')
regmatch = np.vectorize(lambda x: bool(r.match(x)))
minutes['minutes_condition'] = minutes[0].astype(str, copy=True, errors='raise')
minutes['minutes_condition_bool'] = regmatch(minutes['minutes_condition'].values)

minutes['minutes_summary'] = minutes["minutes_condition"].where(
    (minutes['minutes_stripped'] == 0) & minutes['minutes_condition_bool'] == True, minutes['minutes_stripped'])
# test = variableToDummies(minutes, 'minutes_condition', "test_sample", True)

multipleReplace(minutes, "minutes_summary", {'1:40', '1:20', '1:40', '1:30'}, "2")
multipleReplace(minutes, "minutes_summary", {'02:19'}, "3")
multipleReplace(minutes, "minutes_summary", {'3.5'}, "4")
multipleReplace(minutes, "minutes_summary", {'07:41', '8:07', '7:29'}, "8")
multipleReplace(minutes, "minutes_summary", {'25:30'}, "26")
multipleReplace(minutes, "minutes_summary", {'10 15', '10*-15'}, "10-15")
multipleReplace(minutes, "minutes_summary", {'25  30'}, "20-30")
multipleReplace(minutes, "minutes_summary", {'15-*20', '15*-20', 'est.15-20'}, "15-20")
multipleReplace(minutes, "minutes_summary", {'20 dart'}, "20")
multipleReplace(minutes, "minutes_summary", {'20in/30', 'Est.20-30'}, "20-30")
multipleReplace(minutes, "minutes_summary", {'IHR40'}, "40")
multipleReplace(minutes, "minutes_summary", {'40-1 hour', '40-1HR', '40-1hr'}, "40-60")
multipleReplace(minutes, "minutes_summary", {'45 -1 hour', '45 -1hour', '45-1 HR', '45-1HR', '45-1hour', '45-1hr'}, "45-60")
multipleReplace(minutes, "minutes_summary", {'50-1 hour', '50-1HR', '50-1hr'}, "50-60")
multipleReplace(minutes, "minutes_summary", {'1hr-1 1/2'}, "60-90")
multipleReplace(minutes, "minutes_summary", {'1hr - 1:45'}, "60-105")
multipleReplace(minutes, "minutes_summary", {'est. 12'}, "12")
multipleReplace(minutes, "minutes_summary", {'est. 20'}, "20")
multipleReplace(minutes, "minutes_summary", {'est. 25'}, "25")
multipleReplace(minutes, "minutes_summary", {'est. 30'}, "30")
multipleReplace(minutes, "minutes_summary", {'est. 35'}, "35")
multipleReplace(minutes, "minutes_summary", {'est.20'}, "20")
multipleReplace(minutes, "minutes_summary", {'est.35'}, "35")
multipleReplace(minutes, "minutes_summary", {'est.9:15'}, "10")
multipleReplace(minutes, "minutes_summary", {'0', '', '1 20', '1 30', '1 HOUR 15', '1 HR 30', '1hr 15', '1hr 30',
                                             '1H15', '1HOUR15', '1HR 30', '1HR 45', '1HR/20', '1HR20', '1hour 20',
                                             '1hour 30', '1hour45', '1hr /30', '1hr 10', '1hr 15', '1hr 20', '1hr 30',
                                             '1hr 40', '1hr 45', '1hr&30', '1hr. 20', '1hr/', '1hr/15', '1hr/20',
                                             '1hr/30', '1hr20', '1hr45', '1hrs 20', '1 hr 15', '1 hr 30', '1:00',
                                             '1:00 h', '1:00 hour', '1:30 H/', '1:30 HR', '1:30 h', '1:45hr',
                                             '1hr - 11/2'}, "0")
# test = variableToDummies(minutes, "minutes_summary", "test_sample", True)

minutes["minutesBasic"] = pd.to_numeric(minutes[0], errors='coerce')
minutes["minutesBasic"].fillna(0, inplace=True)

minutesAverage = minutes['minutes_summary'].str.split('(-|/|to)', expand=True)
minutesAverage[0] = minutesAverage[0].str.strip()
minutesAverage[2] = minutesAverage[2].str.strip()
minutesAverage.fillna(0, inplace=True)
minutesAverage[0] = minutesAverage[0].astype(int)
multipleReplace(minutesAverage, 2, {''}, "0")
minutesAverage[2] = minutesAverage[2].astype(int)
# test = variableToDummies(test, 2, "test_sample", True)

dataset["Delay_From_Minutes"] = minutes["minutesBasic"].where(minutesAverage[2] == 0)
dataset["Avg_From_Minutes"] = ((minutesAverage[0] + minutesAverage[2])/2).where(minutesAverage[2] != 0)
dataset["Delay_From_Minutes"].fillna(0, inplace=True)
dataset["Avg_From_Minutes"].fillna(0, inplace=True)
del minutes, minutesAverage, r, regmatch

dataset["Bus_Delay"] = dataset["Delay_From_Hours"] + dataset["Delay_From_Minutes"] + dataset["Avg_From_Minutes"]
dataset["Bus_Delay"] = dataset["Bus_Delay"].astype(int)
dataset.drop(["How_Long_Delayed", "Delay_From_Hours", "Delay_From_Minutes", "Avg_From_Minutes"], axis=1, inplace=True)
dataset = dataset[dataset['Bus_Delay'] != 0]

# Final dataset structure
dataset = dataset.rename(columns={'Number_Of_Students_On_The_Bus': 'Students_Number'})
dataset["Students_Number"] = dataset["Students_Number"].astype(int)

dataset = dataset[['Bus_Delay',
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

# ------------------------------------- Removing outliers using Z-Score method -----------------------------------------
# Info about the data BEFORE outlier detection
print("Dataset dimension BEFORE:", dataset.shape)

plt.boxplot(dataset['Bus_Delay'], vert=False)
plt.title("Bus delay box-plot BEFORE")
plt.xlabel('values')
plt.savefig('analysis-results/Bus_Delay outliers BEFORE.png', bbox_inches='tight', dpi=100)
plt.show()
# todo: Move plots into function
plt.boxplot(dataset['Students_Number'], vert=False)
plt.title("Students number box-plot BEFORE")
plt.xlabel('values')
plt.savefig('analysis-results/Students_Number outliers BEFORE.png', bbox_inches='tight', dpi=100)
plt.show()

# Detect and remove outliers from Bus_Delay
zscoreDelays = np.abs(stats.zscore(dataset['Bus_Delay']))
if sampleData:
    dataset = dataset[(zscoreDelays < delaysOutliers)]
else:
    dataset = dataset[(zscoreDelays < 0.75)]
del zscoreDelays

# Detect and remove outliers from Students_Number
zscoreStudents = np.abs(stats.zscore(dataset['Students_Number']))
if sampleData:
    dataset = dataset[(zscoreStudents < studentsOutliers)]
else:
    dataset = dataset[(zscoreStudents < 0.80)]
del zscoreStudents

# Info about the data AFTER outlier detection
print("Dataset dimension AFTER:", dataset.shape)

plt.boxplot(dataset['Bus_Delay'], vert=False)
plt.title("Bus delay box-plot AFTER")
plt.xlabel('values')
plt.savefig('analysis-results/Bus_Delay outliers AFTER.png', bbox_inches='tight', dpi=100)
plt.show()

plt.boxplot(dataset['Students_Number'], vert=False)
plt.title("Students number box-plot AFTER")
plt.xlabel('values')
plt.savefig('analysis-results/Students_Number outliers AFTER.png', bbox_inches='tight', dpi=100)
plt.show()

# -------------------------------------------------- Export data -------------------------------------------------------
if sampleData:
    dataset.to_csv("data/final-data.csv", sep=',', index=False, encoding='utf-8')
else:
    dataset.to_csv("data/full-data.csv", sep=',', index=False, encoding='utf-8')

print("END")