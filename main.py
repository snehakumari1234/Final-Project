# 1. Data Loading and Label Encoding
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1.a) Load Data
df = pd.read.csv
print(df.head())

# 1.b) Checking for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# 1.c) Converting category columns using label encoding
label_encoder = LabelEncoder()
df['Category_column'] = label_encoder.fit_transform(df['Category_column'])
print(df.head())

# 2.a) Histogram Plot
plt.figure(figsize=(10, 6))
plt.hist(df['score_column'], bins=20, color='blue', alpha=0.7, edgecolor='black')
plt.title('Score Distribution')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

# 2.b) Average scores by category
average_scores_gender = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
average_scores_lunch = df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean()
average_scores_test_prep = df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()

print("Average scores by Gender:")
print(average_scores_gender)

print("\nAverage scores by Lunch Type:")
print(average_scores_lunch)

print("\nAverage scores by Test preparation status:")
print(average_scores_test_prep)

# 2.c) Correlation Heatmap
df = pd.read.csv('student_performance.csv')
df_encoded = pd.get_dummies(df, columns=['gender', 'lunch', 'test preparation course'], drop_first=True)
numeric_cols = df_encoded.select_dtypes(include=['int64', 'float64'])
corr_matrix = numeric_cols.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f',
            linewidths=0.5, annot_kws={'size': 10})
plt.title('Student Performance Correlation Heatmap', pad=20, fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# 3.a) Creating average score
df = pd.read.csv
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
print(df.head())

# 3.c) Creating binary result column
df = pd.read.csv
df['result_binary'] = np.where(df['average_score'] >= 50, 1, 0)
print(df[['average_score', 'result_binary']].head())
      
