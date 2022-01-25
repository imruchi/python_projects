#%%
from gettext import install
import pandas as pd
import matplotlib as plt


df=pd.read_csv('ViewingActivity.csv')
df=df.drop(['Attributes','Supplemental Video Type','Device Type','Bookmark','Latest Bookmark','Country'], axis=1)

df['Start Time']=pd.to_datetime(df['Start Time'], utc=True)
df=df.set_index('Start Time')
df=df.tz_convert('Asia/Calcutta')
df=df.reset_index()

df['Duration']=pd.to_timedelta(df['Duration'])
print(df.dtypes)

office=df[df['Title'].str.contains('The Office (U.S.)', regex=False)]
office=office[(office['Duration']>'0 days 00:01:00')]

office['Weekday']=office['Start Time'].dt.weekday

office['Hour']=office['Start Time'].dt.hour

print(office.head())
print(office.shape)
print(office['Duration'].sum())

#Plotting graphs

office['Weekday']=pd.Categorical(office['Weekday'], categories=[0,1,2,3,4,5,6], ordered=True)
office_by_day=office['Weekday'].value_counts()
office_by_day=office_by_day.sort_index()
plt.rcParams.update({'font.size': 23})
office_by_day.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Day')

office['Hour']=pd.Categorical(office['Hour'], categories=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],ordered=True)
office_by_hour=office['Hour'].value_counts()
office_by_hour=office_by_hour.sort_index()
office_by_hour.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Hour')



# %%
