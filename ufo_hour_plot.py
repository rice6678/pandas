import pandas as pd
df=pd.read_csv("https://bit.ly/uforeports")

df["Hour"]=0
for i in range(len(df)):
    a=df.loc[i,"Time"]
   # print(a,a[-5:-3])
    df.loc[i,"Hour"]=int(a[-5:-3])

df["Hour"].value_counts().plot(kind='bar')
