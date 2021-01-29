#%%
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


# To do list in commments 


data_train_df = pd.read_csv('train.csv')

 # fixing sex 1 for male 0 for female
data_train_df["Sex"] = data_train_df.Sex.apply(lambda row: 1 if row == 'male' else 0)

# exploring the top five rows + bottom
# print(data_train_df.head())
# print(data_train_df.tail())

# checking the number of rows and columns in the dataset

row = f"Number of rows: {data_train_df.shape[0]}"
columns = f"Number of columns: {data_train_df.shape[1]}"

# drop name ticket and cabin column - as not needed 
data_train_df = data_train_df.drop(["Name","Ticket","Cabin"],axis=1)
# getting descriptive info about the data 
describe_stats = data_train_df.describe()
# cheecking the data types
dtype = data_train_df.dtypes

# replacing age nan with the mean 
mean_age = np.mean(data_train_df.Age)
data_train_df["Age"] = data_train_df["Age"].fillna(mean_age)
check_na = data_train_df.isnull().sum()

# distribution of the dataset 
hist_plot = data_train_df.hist(figsize=(16,8))

# checking the correlated variables 
corr = data_train_df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(corr,annot=True)

# Let compare the number of people survived vs not survived 
surive_dict = dict()
surive_dict['survided'] = len([i for i in data_train_df.Survived if i == 1])
surive_dict['died'] = len([i for i in data_train_df.Survived if i == 0])

text = ['survided','died']
labels = [surive_dict['survided'],surive_dict['died']]

plt.figure(figsize=(8,6),dpi=100)

for i in range(len(text)):
    plt.bar(text[i],labels[i])
    plt.text(text[i],labels[i],str(labels[i]),fontsize=16,fontweight='bold')

plt.title("Number of people survived vs not survived")
plt.xlabel("Survived vs not survived")
plt.ylabel("Number of people")
plt.show()

# find survival rate based on age 
most_survived_age = dict()

# top ten ages for survival 

# distribution of ages 

# comparision between number of males and females survived 

# Number of Survived people based on the class

""" MODELING AND TRAINING THE DATASET """ 





#%%