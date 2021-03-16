import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_train_df = pd.read_csv('train.csv')




data_train_df['Sex'] = data_train_df['Sex'].apply(lambda row: 1 if row == "male" else 0)
data_train_df['Age'] = data_train_df['Age'].fillna(np.mean(data_train_df.Age),axis=0)
data_train_df['Age'] = data_train_df['Age'].apply(lambda row: round(row))

## make a function comparing survival the  youngest and ten oldest 
def oldest_vs_young(dataf,columnName):
    cut_off = np.mean(dataf.columnName)
    young_df = dataf[dataf[columnName] <= cut_off]
    old_df = dataf[dataf[columnName] > cut_off]
    plt.plot(young_df.columnName,old_df.columnName,marker='o',color='b',label=columnName)
    plt.title('old vs young')
    plt.xlabel('Age')
    plt.ylabel('Frequncy')
    plt.show()
print(oldest_vs_young(data_train_df,"Age"))
