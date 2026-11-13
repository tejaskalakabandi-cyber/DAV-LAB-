import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files

uploaded = files.upload()


df = pd.read_csv("students.csv")

print("Student Dataset:")
print(df)

print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

print("\n-- Histogram --")

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=10)
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

print("\n-- Box Plot --")

plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Marks"])
plt.title("Box Plot of Student Marks")
plt.xlabel("Marks")
plt.show()

print("\n-- Scatter Plot --")

plt.figure(figsize=(8, 5))
sns.scatterplot(
data=df,
x="StudyHours",
y="Marks",
hue="Result")
palette={"Pass": "green", "Fail": "red"}
s=70
sns.regplot(
    data=df,
    x="StudyHours",
    y="Marks",
    scatter=False
)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend(title="Result")
plt.show()

print("\n-- Pair Plot --")

sns.pairplot(
    df[
        [
            "StudyHours",
            "Attendance",
            "PrevMarks",
            "Marks"
        ]
    ],
    diag_kind="hist"
)

plt.show()

correlation = df [
            [

            "StudyHours",
            "Attendance",
            "PrevMarks",
            "Marks"
            ]
].corr()
print("\n Correlation Matrix")
print(correlation)

plt.figure(figsize=(8,6))
sns.heatmap(
    correlation ,
    annot = True
)
