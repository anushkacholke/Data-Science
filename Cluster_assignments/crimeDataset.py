# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:26:14 2024

@author: Sai
"""
import pandas as pd
import numpy as np
df=pd.read_csv("F:/Data science/ML/crime_data.csv")
df.columns

#Feature 1: Murder
#1.Data type
murder_dtype=df['Murder'].dtype
#possible values/Range
murder_min = df['Murder'].min()
murder_max = df['Murder'].max()
# 3. Missing Values
murder_missing = df['Murder'].isnull().sum()
# 4. Example Value
murder_example = df['Murder'].iloc[0]
##Information of Murder feature
murder_dtype
murder_min
murder_max
murder_missing
murder_example

#Feature 2: Rape
#1.Data type
Rape_dtype=df['Rape'].dtype
#possible values/Range
Rape_min = df['Rape'].min()
Rape_max = df['Rape'].max()
# 3. Missing Values
Rape_missing = df['Rape'].isnull().sum()
# 4. Example Value
Rape_example = df['Rape'].iloc[0]
##Information of Rape feature
Rape_dtype
Rape_min
Rape_max
Rape_missing
Rape_example

#Feature 3: UrbanPop
#1.Data type
UrbanPop_dtype=df['UrbanPop'].dtype
#possible values/Range
UrbanPop_min = df['UrbanPop'].min()
UrbanPop_max = df['UrbanPop'].max()
# 3. Missing Values
UrbanPop_missing = df['UrbanPop'].isnull().sum()
# 4. Example Value
UrbanPop_example = df['UrbanPop'].iloc[0]
##Information of UrbanPop feature
UrbanPop_dtype
UrbanPop_min
UrbanPop_max
UrbanPop_missing
UrbanPop_example

#Feature 3: Assault
#1.Data type
Assault_dtype=df['Assault'].dtype
#possible values/Range
Assault_min = df['Assault'].min()
Assault_max = df['Assault'].max()
# 3. Missing Values
Assault_missing = df['Assault'].isnull().sum()
# 4. Example Value
Assault_example = df['Assault'].iloc[0]
##Information of UrbanPop feature
Assault_dtype
Assault_min
Assault_max
Assault_missing
Assault_example

#EDA(Exploratory data analysis)
df.describe()

import matplotlib.pyplot as plt
import seaborn as sns

##Univariate Analysis
# Histogram for a numerical feature
plt.figure(figsize=(8,6))
sns.histplot(df['Murder'],kde=True)
plt.title('Distribution of murder rate')
plt.show()
#Boxplot to detect outliers
plt.figure(figsize=(8, 6))
sns.boxplot(df['Murder'])
plt.title('Boxplot of Murder Rates')
plt.show()

##Bivarient Analysis
#scatter plot between 2 numbrical features
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Murder'], y=df['Assault'])
plt.title('Murder vs Assault')
plt.show()
# Correlation matrix and heatmap
corr_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

##data cleaning 
# Handling missing values (example: fill missing values with median)
df['Murder'].fillna(df['Murder'].median(), inplace=True)

# Detecting and handling outliers (example: capping)
Q1 = df['Murder'].quantile(0.25)
Q3 = df['Murder'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df['Murder'] = df['Murder'].clip(lower_bound, upper_bound)

# Correcting data types (example: convert UrbanPop to integer)
df['UrbanPop'] = df['UrbanPop'].astype(int)

# Handling duplicates
df.drop_duplicates(inplace=True)

##Features Engineering
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
# Creating a new feature (example: Crime Rate)
df['CrimeRate'] = df['Murder'] + df['Assault'] + df['Rape']
# Standardizing the features
scaler = StandardScaler()
df[['Murder', 'Assault', 'Rape']] = scaler.fit_transform(df[['Murder', 'Assault', 'Rape']])
# Feature selection (example: dropping highly correlated features)
corr_matrix = df.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
df.drop(columns=to_drop, inplace=True)

#Model building
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

df = pd.read_csv('F:/Data science/ML/crime_data.csv')

# Drop the 'Unnamed: 0' column if it's not needed
df.drop(['Unnamed: 0'], axis=1, inplace=True)

# Normalize the entire dataset using your normalization function
def norm_fun(i):
    x = (i-i.min())/(i.max()-i.min())
    return x

df_norm = df.apply(norm_fun)
b = df_norm.describe()
print(b)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Now apply K-means clustering
wcss = []  # Within-cluster sum of squares
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

# Plotting the scree plot (Elbow Method)
plt.figure(figsize=(10, 6))
plt.plot(K, wcss, marker='o')
plt.title('Scree Plot to determine the optimal number of clusters')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

