import pandas as pd

df = pd.read_excel("pahittad_data.xlsx")

print(df.head())

print(df.info())

print(df.describe()) 

print(df.columns)

print(df["Stad"].unique())

print(df.sort_values(by="Lön", ascending=False))

print(df[df["Lön"]>35000])