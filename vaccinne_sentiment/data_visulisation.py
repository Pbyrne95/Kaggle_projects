#%%
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots 
import pandas as pd
import json

data = {}
with open('output.json','r') as json_file:
    data = json.load(json_file)

# Data Visulasation 
new_df = pd.DataFrame(data)
print(new_df)

corr = new_df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(corr,annot=True)


# Scatter plot between Hour and interactions

def make_kdeplot(df,row,row2):
    fig, ax = plt.subplots(1,figsize=(12,8))
    sns.kdeplot(df.row, df.row2, cmap='Blues',
    shade=True,thresh=0.05,clip=(-1,300))



# Findeing the most interactions in the month of December 
new_df['day'] = pd.DatetimeIndex(new_df['date']).day 
daysforplot = new_df.groupby('day',as_index=False).agg({'TotalInteractions':'sum'})
fig = px.scatter(daysforplot,
                x = 'day',
                y= 'TotalInteractions',
                color_continuous_scale='Rainbow',
                color='TotalInteractions',
                size='TotalInteractions',
                title = 'Most engaging days')

fig.show()

#%%