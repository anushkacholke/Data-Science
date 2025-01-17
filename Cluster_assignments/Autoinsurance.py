# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:03:33 2024

@author: Sai
"""
'''5.Perform clustering on mixed data. Convert the categorical variables to numeric
 by using dummies or label encoding and perform normalization techniques.
 The dataset has the details of customers related to their auto insurance. 
 Refer to Autoinsurance.csv dataset.'''

#business objective
'''
business objective is to perform clustering on customers
based on their similar characteristics
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


autoIns = pd.read_csv("F:/Data science/ML/Anushka_Cholke/Insurance Dataset.csv")
autoIns.columns
'''Index(['Premiums Paid', 'Age', 'Days to Renew', 'Claims made', 'Income'],
 dtype='object')'''

autoIns.dtypes
'''
Premiums Paid      int64
Age                int64
Days to Renew      int64
Claims made      float64
Income             int64
dtype: object
'''
#most of colmns are of object type so we need to convert 
# them to numeric using dummies

autoIns
autoIns.describe()
'''
Premiums Paid         Age  Days to Renew   Claims made         Income
count     100.000000  100.000000     100.000000    100.000000     100.000000
mean    12542.250000   46.110000     120.400000  12578.993367  102250.000000
std      6790.731666   13.887641      88.055767  13695.906762   43517.237964
min      2800.000000   23.000000       1.000000   1978.260870   28000.000000
25%      6975.000000   34.000000      56.000000   5220.648735   65125.000000
50%     11825.000000   45.000000      89.000000   8386.043907  102250.000000
75%     15475.000000   54.500000     186.500000  14670.889520  139375.000000
max     29900.000000   82.000000     321.000000  99676.744190  176500.000000'''



# PDF and CDF
counts, bin_edges = np.histogram(autoIns['Claims made'], bins=10, density = True)
pdf = counts/(sum(counts))
print(pdf);
print(bin_edges)

#compute CDF
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:], cdf)
plt.show();

#Boxplot and outlier treatment

sns.boxplot(autoIns['Claims made'])
sns.boxplot(autoIns['Premiums Paid'])
sns.boxplot(autoIns['Age'])
sns.boxplot(autoIns['Days to Renew'])
sns.boxplot(autoIns['Income'])

#do not have outliers

#we need to remove outliers from other cols
#1
iqr = autoIns['Claims made'].quantile(0.75)-autoIns['Claims made'].quantile(0.25)
iqr

q1 = autoIns['Claims made'].quantile(0.25)
q3 = autoIns['Claims made'].quantile(0.75)

l_limit = q1-(1.5*iqr)
u_limit = q3+(1.5*iqr)

autoIns['Claims made'] = np.where(autoIns['Claims made'] >u_limit,u_limit,np.where(autoIns['Claims made']<l_limit,l_limit,autoIns['Claims made']))
sns.boxplot(autoIns['Claims made'])

#2
iqr = autoIns['Premiums Paid'].quantile(0.75)-autoIns['Premiums Paid'].quantile(0.25)
iqr

q1 = autoIns['Premiums Paid'].quantile(0.25)
q3 = autoIns['Premiums Paid'].quantile(0.75)

l_limit = q1-(1.5*iqr)
u_limit = q3+(1.5*iqr)

autoIns['Days to Renew'] = np.where(autoIns['Days to Renew'] >u_limit,u_limit,np.where(autoIns['Days to Renew']<l_limit,l_limit,autoIns['Days to Renew']))
sns.boxplot(autoIns['Days to Renew'])


q1 = autoIns['Premiums Paid'].quantile(0.25)
q3 = autoIns['Premiums Paid'].quantile(0.75)

l_limit = q1-(1.5*iqr)
u_limit = q3+(1.5*iqr)


autoIns.describe()


df_n= pd.get_dummies(autoIns)
df_n.shape

#now we have dataset df_n with all dtypes int
df_n.describe() 
#there is huge difference between min, max,and mean values in dataset cols
#so we need to normalize this data

def norm_func(i):
    x = (i-i.min())/(i.max()-i.min())
    return x

df_normal = norm_func(df_n)
desc = df_normal.describe()
desc

df_normal.columns
#in this Premiums Paid contains NAN values so 
#we will drop it

df_normal.drop(['Premiums Paid'],axis =1, inplace=True)
#now all data is normalized
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

z = linkage(df_normal,method='complete',metric='euclidean')
plt.figure(figsize=(15,8))
plt.title('Hierarchical clustering dendrogram')
plt.xlabel('index')
plt.ylabel('Distance')
#ref of dendrogram

sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#now apply clustering 
from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters=3,
                                     linkage='complete',
                                     affinity='euclidean').fit(df_normal)
#apply labels to clusters
h_complete.labels_
cluster_labels = pd.Series(h_complete.labels_)
#assign this series to autoIns dataframe as column
autoIns['cluster'] = cluster_labels

autoInsNew = autoIns.iloc[:]
autoInsNew.iloc[:,2:].groupby(autoInsNew.cluster).mean()

autoInsNew.to_csv("AutoInsuranceNew.csv",encoding='utf-8')
import os
os.getcwd()


####################################################
#KMeans Clustering on auto insurance
#for this we will used normalized data set df_normal

from sklearn.cluster import KMeans
#total sum of squares
TWSS = []

#initially we will find the ideal cluster number using elbow curve

k = list(range(2,8))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_normal)
    TWSS.append(kmeans.inertia_)
  
TWSS
'''
[17.677095466832803,
 12.625878739294848,
 9.956086421059808,
 8.224047738940808,
 6.820125910910157,
 6.056997712391481]'''
