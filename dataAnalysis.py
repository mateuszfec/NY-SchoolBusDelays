# Libraries
import pandas as pd

dataset = pd.read_csv("data/final-data.csv")

# Descriptive statistics df
DS = pd.DataFrame(columns=['Mean',
                           'Standard_Deviation',
                           'Skewness',
                           'Kurt',
                           'Minimum',
                           'Maximum'],
                  index=['Bus_Delay',
                         'Students_Number'])

DS.loc['Bus_Delay'] = [dataset['Bus_Delay'].mean(),
                       dataset['Bus_Delay'].std(),
                       dataset['Bus_Delay'].skew(),
                       dataset['Bus_Delay'].kurt(),
                       dataset['Bus_Delay'].min(),
                       dataset['Bus_Delay'].max()]

DS.loc['Students_Number'] = [dataset['Students_Number'].mean(),
                             dataset['Students_Number'].std(),
                             dataset['Students_Number'].skew(),
                             dataset['Students_Number'].kurt(),
                             dataset['Students_Number'].min(),
                             dataset['Students_Number'].max()]

print("END")