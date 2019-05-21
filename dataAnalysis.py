# Libraries
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("data/full-data.csv")

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

# plt.boxplot(dataset['Bus_Delay'], vert=False)
# plt.title("Bus delay box-plot")
# plt.xlabel('values')
# plt.savefig('analysis-results/Bus_Delay outliers.png', bbox_inches='tight', dpi=100)
# plt.show()

# plt.boxplot(dataset['Students_Number'], vert=False)
# plt.title("Students number box-plot")
# plt.xlabel('values')
# plt.savefig('analysis-results/Students_Number outliers.png', bbox_inches='tight', dpi=100)
# plt.show()

print("END")