import random
for i in range(5):
    r=random.randint(0,len(df))
    rec.appen(r)
print(rec)
for i in range(5):
    r=random.randint(0,len(df))
    rec.append(r)
for i in range(len(rec)):
             print(df.loc[rec[i]])
