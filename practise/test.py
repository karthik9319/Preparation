import pandas as pd

df = pd.read_csv('CPU_Util_.csv')

df['TimeStamp'] = pd.to_datetime(df['Time (GMT)'])

df['Hr'] = [x. hour for x in df['TimeStamp']]

df.drop(['TimeStamp'], axis=1)

print("Mean of KPI Value: ",df.groupby('Hr').mean())

x = df.groupby('Hr').min()

# print(x['KPI Value'])

y = df.groupby('Hr').max()

print("Min of KPI Value: ",x['KPI Value'])

print("Max of KPI Value: ", y['KPI Value'])