import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score


data_train_df = pd.read_csv('train.csv')

# cleaning the data 

# fixing categorical data 

head = data_train_df.head()
data_train_df['Sex'] = data_train_df.Sex.apply(lambda row: 1 if row == "Male" else 0)

# fixing null values 
total_null = data_train_df.isnull().sum()

# print(total_null)

average_age = np.mean(data_train_df.Age)
data_train_df.Age = data_train_df.Age.fillna(average_age)
data_train_df = data_train_df.Age.apply(lambda row: round(row))

udated_null = data_train_df.isnull().sum()

hist_plot = data_train_df.hist(figsize=(16,8))

plt.close('all')

corr = data_train_df.corr()
plt.figure(figsize=(16,8))
sns.heatmap(corr,annot=True)




