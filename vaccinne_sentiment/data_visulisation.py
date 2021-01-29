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


corr = new_df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(corr,annot=True)

# Scatter plot between Hour and interactions

fig, ax = plt.subplots(1,figsize=(12,8))
sns.kdeplot(new_df.Hour,new_df.TotalInteractions, cmap='Blues',shade=True,thresh=0.05,clip=(-1,300))

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

fig, ax = plt.subplots(figsize=(8, 6))
l1,l2 = new_df.polarity,new_df.subjectivty
list_sum = []
for row1,row2 in zip(l1,l2):
    list_sum.append(row1+row2)

new_df['total'] = list_sum

# Plot histogram of the polarity values
new_df.total.hist(bins=[-0.5, -0.25, 0.25, 0.5,],
             ax=ax,
             color="purple")

plt.title("Sentiments from Tweets in the last 30 days")
plt.show()
#%%