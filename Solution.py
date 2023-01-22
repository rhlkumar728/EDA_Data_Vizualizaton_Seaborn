import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/Dell/Downloads/Mobile price New - Mobile price New (1).csv')
df.head()

#Shape of Dataset
df.shape

#DataTypes of Coulmns

df.dtypes

#Null Values of DataSet

df.isna()

#Count of Null Values of Dataset

df.isna().sum()

#Handling Null Values

# As we have very less Null Values so we will be Dropping Null Values

df.dropna(inplace=True)

#Statistical Summary of Numerical Coulmns

df.describe()

#Summary of Dataset

df.info()

#Cleaning the Data

#Here in the Dataset we have few Coumns which has to be number data type but it's not numerical

#These are ram,px_width,mobile_width,battery_power

#Let's see what's there

col=['ram','px_width','mobile_wt','battery_power']

for c in col:
    print(c)
    print(df[c].nunique())
    print(df[c].unique())
    print(df[c].value_counts())

#By seeing the above result it is very clear that there is Strings as 
#well in the data so we will be removing the string and will only be keeping number

#Regex Function we will use

col=['ram','px_width','mobile_wt','battery_power']

for c in col:
    df[c]=df[c].str.replace('[^0-9\.]','',regex=True)

#We will convert these coulmns into Numeric and error=coerce will change all values to Null if not a number
col=['ram','px_width','mobile_wt','battery_power']

for c in col:
    df[c]=pd.to_numeric(df[c],errors='coerce')


#Now again we will analyze the null values

df.isna().sum()

#We will Again drop the Null Values

df.dropna(inplace=True)

#We will again check data types

df.dtypes

#Now we will do outlier analysis

#Let's see outlier by boxplot

col=['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
       'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
       'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
       'touch_screen', 'wifi', 'price_range']
for c in col:
    plt.figure()
    sns.boxplot(df[c])

#Dots that are out of max and min range are outlier and we will remove them using iqr
col=['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
       'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
       'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time']
for c in col:
    percentile25=df[c].quantile(0.25)
    percentile75=df[c].quantile(0.75)
    iqr=percentile75-percentile25
    upper_limit=percentile75+(1.5*iqr)
    lower_limit=percentile25-(1.5*iqr)
    df=df[df[c]<upper_limit]
    df=df[df[c]>lower_limit]
    plt.figure()
    sns.boxplot(y=c,data=df)

#We will again check the shape

df.shape

#We will again check head
df.head()

#we will summarzie the data again

df.info()

# Vizualization using Seaborn

sns.pairplot(df)

sns.scatterplot(x=df['battery_power'],y=df['price_range'],hue=df['touch_screen'])

df.corr()

sns.heatmap(df.corr())

sns.histplot(df['price_range'])

sns.barplot(x=df['three_g'],y=df['price_range'],hue=df['touch_screen'])

sns.countplot(df['battery_power'])

sns.barplot(x=df['four_g'],y=df['price_range'])

sns.scatterplot(x=df['battery_power'],y=df['mobile_wt'],color='Red')

sns.distplot(x=df['mobile_wt'])

