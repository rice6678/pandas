#%%
import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")

print(df["City"].head())
df["City"] = df["City"].str.upper()
print(df["City"].head())
# %%
print(df["Time"].head())
df["Time"]=pd.to_datetime(df["Time"])
print(df["Time"].head())
# %%
print(df["Time"].dt.day_name())

# %%
print(df["Time"].dt.day_name().value_counts())
# %%
df["Time"].dt.day_name().value_counts().plot(kind="bar")
# %%
