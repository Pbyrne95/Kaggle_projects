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

head = data_train_df.head()
tail = data_train_df.tail()

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
data_train_df["Age"] = data_train_df.Age.apply(lambda row: round(row))

# distribution of the dataset 
#%%
hist_plot = data_train_df.hist(figsize=(16,8))

# checking the correlated variables 
#%%

corr = data_train_df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(corr,annot=True)

# Let compare the number of people survived vs not survived 

#%%

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
# plt.show()

# find survival rate based on age 
#%%
most_survived_age = dict()
amount,max_age = 0,0
for age,survival in zip(data_train_df.Age,data_train_df.Survived):
    if age not in most_survived_age:
        most_survived_age[age] = survival
    else:
        most_survived_age[age] += survival

    if most_survived_age[age] > max_age:
        max_age = age
        amount = most_survived_age[age]

# top ten ages for survival 

sorted_dict = sorted(most_survived_age.items(), key=lambda i:i[1])
x =  len(sorted_dict)//2

oldest_passengers = sorted(most_survived_age.items(), key=lambda i:i[0])[x+5:]
print(oldest_passengers)

most_survived = sorted_dict[-10:]

# distribution of ages 

#%%
data_train_df[data_train_df.Survived == 1]["Age"].hist()
plt.title("Distribution of ages")
plt.xlabel("Age")
plt.ylabel("Number of people")
# plt.show()

# comparision between number of males and females survived 
#%%
males_survival = data_train_df[(data_train_df.Sex == 1) & (data_train_df.Survived == 1)]["Sex"].count()
female_survival = data_train_df[(data_train_df.Sex == 0) & (data_train_df.Survived == 1)]["Sex"].count()

text_sex = ["males","females"]
new_labels = [males_survival,female_survival]
for i in range(len(text)):
    plt.bar(text_sex[i],new_labels[i])
    plt.text(text_sex[i],new_labels[i],str(new_labels[i]),fontsize=16,fontweight='bold')
plt.title('surival between sexes')
plt.xlabel("sex")
plt.ylabel("count")
# plt.show()

# Number of Survived people based on the class
lis=[data_train_df[(data_train_df.Pclass == 1) & (data_train_df.Survived == 1)],data_train_df[(data_train_df.Pclass == 2) & (data_train_df.Survived == 1)],data_train_df[(data_train_df.Pclass == 2) & (data_train_df.Survived == 1)]]
def check_leng(row): return len(row)
new_lis = list(map(check_leng,lis))



""" MODELING AND TRAINING THE DATASET """ 





#%%