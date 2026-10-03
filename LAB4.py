import pandas as pd
import numpy as np

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Study_Hours": [5, 6, np.nan, 4, 7],
    "Attendance": [80, 85, 75, np.nan, 90],
    "Marks": [75, 82, 68, 55, np.nan],
    "Result": ["Pass", "Pass", "Pass", "Fail", "Pass"]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull().sum())

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
print(df)

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].median())
print(df)

df["Study_Hours"] = df["Study_Hours"].ffill()
print(df)

df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
    })
print(df)

df["Result"] = df["Result"].map({
    "Pass": 1,
    "Fail": 0
    })
print(df)

print(df.isnull().sum())

print(df)
