"""
Student Performance Data Cleaning & Visualization Project
Run: python student_performance_analysis.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create an output folder
os.makedirs("output", exist_ok=True)

# 2. Load the raw dataset
df = pd.read_csv("student_performance_raw.csv")

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

print("\n--- DATASET INFORMATION ---")
print(df.info())

print("\n--- MISSING VALUES BEFORE CLEANING ---")
print(df.isnull().sum())

print("\nDuplicate rows before cleaning:", df.duplicated().sum())

# 3. Remove exact duplicate rows
df = df.drop_duplicates()

# 4. Correct invalid values using simple range checks
# Study hours should be between 0 and 16 per day.
df.loc[~df["Study_Hours"].between(0, 16), "Study_Hours"] = float("nan")

# Attendance and scores should be between 0 and 100.
for column in ["Attendance", "Math_Score", "Reading_Score", "Writing_Score"]:
    df.loc[~df[column].between(0, 100), column] = float("nan")

# 5. Fill missing numeric values with each column's median
numeric_columns = [
    "Study_Hours", "Attendance",
    "Math_Score", "Reading_Score", "Writing_Score"
]
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill any missing category with the most common category
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

# 6. Add an average score column
score_columns = ["Math_Score", "Reading_Score", "Writing_Score"]
df["Average_Score"] = df[score_columns].mean(axis=1).round(2)

# Add a simple performance category
def performance_category(score):
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Needs Improvement"

df["Performance_Level"] = df["Average_Score"].apply(performance_category)

# 7. Save the cleaned dataset
df.to_csv("output/student_performance_cleaned.csv", index=False)

print("\n--- MISSING VALUES AFTER CLEANING ---")
print(df.isnull().sum())
print("\nDuplicate rows after cleaning:", df.duplicated().sum())
print("\n--- SUMMARY STATISTICS ---")
print(df.describe())

# 8. Create visualizations
sns.set_theme(style="whitegrid")

# Chart 1: Average score by gender
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Gender", y="Average_Score", errorbar=None)
plt.title("Average Student Score by Gender")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("output/average_score_by_gender.png")
plt.close()

# Chart 2: Distribution of average scores
plt.figure(figsize=(7, 5))
sns.histplot(data=df, x="Average_Score", bins=12, kde=True)
plt.title("Distribution of Student Average Scores")
plt.xlabel("Average Score")
plt.tight_layout()
plt.savefig("output/average_score_distribution.png")
plt.close()

# Chart 3: Study hours compared with average score
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Study_Hours", y="Average_Score", hue="Gender")
plt.title("Study Hours vs Average Score")
plt.tight_layout()
plt.savefig("output/study_hours_vs_score.png")
plt.close()

# Chart 4: Correlation heatmap
plt.figure(figsize=(8, 6))
correlation = df[numeric_columns + ["Average_Score"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Student Performance Variables")
plt.tight_layout()
plt.savefig("output/correlation_heatmap.png")
plt.close()

# 9. Print useful findings
print("\n--- PROJECT FINDINGS ---")
print("Number of students:", len(df))
print("Overall average score:", round(df["Average_Score"].mean(), 2))
print("Average study hours:", round(df["Study_Hours"].mean(), 2))
print("Average attendance:", round(df["Attendance"].mean(), 2))
print("\nStudents by performance level:")
print(df["Performance_Level"].value_counts())

print("\nProject completed! Check the output folder for the cleaned CSV and charts.")
