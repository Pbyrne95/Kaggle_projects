
#%%
import pandas as pd 
import numpy as np  
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import re
from textblob import TextBlob
from wordcloud import WordCloud



data = pd.read_csv(r"vaccination_tweets.csv")

## Defining variables which describe the dataset 


data_type = data.dtypes
data_columns = data.columns
data_null = len(data.isna())
data_len = len(data)
list_of_regex = [r'@[^\s]+',r'\B#\S+',r"http\S+",r'\w+']
findall_regex_list = [r'\w+']

## deffining dfunctions to be used through the dataset 

def removeNull(df):
    for elem in df.columns:
        if df[elem].isnull().any() == True:
            df.dropna(axis=0,inplace=True)
    return df

new_df = removeNull(data)


def onlyNums(elem): return re.sub("\D+", "",elem) 

def str_to_datetime(row): return date.today() - datetime.strptime(str(row[:10]),'%Y-%m-%d').date() 

def df_min_max(row):
    return {
            "smallest":min(row),
            "biggest": max(row)
            }

def avg_count(element,creteria):
    count = 0 
    for elem in element:
        if elem == creteria:
            count+=1
    return count

def total_percentage(element,creteria): return creteria / (len(element) - creteria) * 100

def max_value(lis):
    dict_count = dict()
    max_count,max_word = 0,''
    for word in lis:
        temp = word[word.rfind('#')+1:]
        if temp not in dict_count:
            dict_count[temp] = 1
        else:
            dict_count[temp] +=1
        if dict_count[temp] > max_count:
            max_count = dict_count[temp] 
            max_word = temp
    return max_count,max_word
   
def list_builder(lis): return [i.split(' ')[0] for i in lis if i != '']

def df_two_cats_max(df,row):
    hours_dict = dict()
    most_activity,param = 0,''
    for rowone,rowtwo in zip(df.row1,df.row2):
        if row1 not in hours_dict:
            hours_dict[rowone] = rowtwo
        elif rowone in hours_dict:
            hours_dict[rowone] + rowtwo
        if hours_dict[rowone] > most_activity:
            most_activity = hours_dict[rowone]
            hour = row1
        return [most_activity,hour]

def regex_commands(row,reg_command):return new_df.tweets.apply(lambda row: re.sub(reg_command,"",row))

def findall_regax(row,reg_command): return new_df.tweets.apply(lambda row:" ".join(re.findall(reg_command,row)))

def Text_polarity(lis): return TextBlob(lis).sentiment.polarity

def Text_subjectivity(lis): return TextBlob(lis).sentiment.subjectivity

# Verified Or Not 
from datetime import datetime, date, timedelta
date_list = new_df['user_created']
today_dates=[]


new_df['AreVerified'] = new_df.user_verified.apply(lambda row: "Verified" if row == True else "Unverified")

Amount_of_Ver = len([i for i in new_df.AreVerified if i == "Verified"])
Amount_of_unver = len([i for i in new_df.AreVerified if i == "Unverified"])

total_accounts = len(new_df.AreVerified)
var_pct = round(Amount_of_Ver / (total_accounts - Amount_of_Ver) * 10 ,2)
unvar_pct = round(Amount_of_unver/(total_accounts - Amount_of_unver) * 10, 2)


# Account Age

lis = list(new_df["user_created"].apply(lambda row: str_to_datetime(row)))
new_df['days_old'] = [int(onlyNums(str(i)[:8])) for i in lis]

account_ages = df_min_max(new_df['days_old'])

#Calculating interquertile range 

quantile_range = [i/10 for i in range(1,10)]
quartile_range = [i * 0.25 for i in range(1,4)]
quantiles = np.quantile(new_df['days_old'],quantile_range)
quartile =  np.quantile(new_df['days_old'],quartile_range)

# # Total tweet Engagement 

total_interactions = []
for row1,row2 in zip(new_df['retweets'],new_df['favorites']):
    total_interactions.append(row1 + row2)

new_df['TotalInteractions'] = total_interactions
interactions_min_max = df_min_max(new_df['TotalInteractions'])

# Average tweet Length and  Short vs Long 

new_df = new_df.rename(columns={'text':'tweets'})
tweet_length = new_df['tweets'].apply(lambda row: len(row))
average_tweet_length = round(np.average(tweet_length))
new_df['below_above'] = new_df.tweets.apply(lambda row: "Above_Average" if len(row) > average_tweet_length \
                                            else ("Average" if len(row) == average_tweet_length else "Below_Average"))

abv_avg,avg,blw_agv = avg_count(new_df["below_above"],"Above_Average"),avg_count(new_df["below_above"],"Average"),avg_count(new_df["below_above"],"Below_Average")
abv_pcnt,avg_pcnt,blw_pcnt = total_percentage(new_df["below_above"],abv_avg),total_percentage(new_df["below_above"],avg),total_percentage(new_df["below_above"],blw_agv)

# Hashtag words and  Mentions Count 
startHash,startsMen,startshttp,end = '#','@','https',' '
list_of_hashtags,list_of_mentions,list_media = [],[],[]
list_of_tweets = new_df.tweets
for words in list_of_tweets:
    list_of_hashtags.append(words[words.rfind(startHash):words.rfind(end)])
    list_of_mentions.append(words[words.rfind(startsMen):words.rfind(end)])
    list_media.append(words[words.rfind(startshttp):words.rfind(end)])

actual_hashtags,actual_mentions,actual_media = list_builder(list_of_hashtags),list_builder(list_of_mentions),list_builder(list_media)

mentions = ["".join(re.sub(r'\s+','',i,flags=re.I)) for i in actual_mentions]

mentions_max_count = max_value(mentions)
hashtags_max_values = max_value(actual_hashtags)

# Account Followers 
loc_df = new_df['user_location'].str.split(',',expand=True)
loc_df=loc_df.rename(columns={0:'fst_loc',1:'snd_loc'})

# Remove Spaces 
loc_df['snd_loc'] = loc_df['snd_loc'].str.strip()
# Rename States 
state_fix = {'Ontario': 'Canada','United Arab Emirates': 'UAE','TX': 'USA','NY': 'USA'
            ,'FL': 'USA','England': 'UK','Watford': 'UK','GA': 'USA','IL': 'USA'
            ,'Alberta': 'Canada','WA': 'USA','NC': 'USA','British Columbia': 'Canada','MA': 'USA','ON':'Canada'
            ,'OH':'USA','MO':'USA','AZ':'USA','NJ':'USA','CA':'USA','DC':'USA','AB':'USA','PA':'USA','SC':'USA'
            ,'VA':'USA','TN':'USA','New York':'USA','Dubai':'UAE','CO':'USA'}

loc_df = loc_df.replace({"snd_loc": state_fix}) 
new_df['Hour'] = sorted(pd.DatetimeIndex(new_df['date']).hour)
new_df['Hour'] = new_df.Hour.apply(lambda row: row +1)


# Engagement - Date 
tweets_dates = new_df.Hour

# Location/Tweets


# NLP Analysis 


# preprocessing the text for Sentimental analysis -> 

new_df.tweets = new_df.tweets.str.lower()

p1=0
run_time = len(list_of_regex)-1
while p1 < run_time:
    if p1 < run_time:
        new_df.tweets = new_df.tweets.apply(lambda row: regex_commands(row,list_of_regex[p1]))
        p1+=1
    elif p1 == run_time:
        new_df.tweets = new_df.tweets.apply(lambda row: re.sub(r'\s+',' ',row,flags=re.I))
        p1+=1

# Dealing with special charecters
new_df.tweets = new_df.tweets.apply(lambda row:findall_regax(row,findall_regex_list[0]))

#initialising sentiment analysis using Textblob

new_df['polarity'] = new_df.tweets.apply(lambda row: Text_polarity(row))
new_df['subjectivty'] = new_df.tweets.apply(lambda row: Text_subjectivity(row))

compare_times_df = new_df.Hour,new_df.tweets,new_df.polarity,new_df.subjectivty

# Data Visulasation 

corr = new_df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(corr,annot=True)
# plt.show()

#Scatter plot between Hour and interactions

fig, ax = plt.subplots(1,figsize=(12,8))
sns.kdeplot(new_df.Hour, new_df.TotalInteractions, cmap='Blues',
            shade=True,thresh=0.05,clip=(-1,300))


# Verfified Engagement

data_for_plots = new_df.copy()
verified_end = data_for_plots.groupby('AreVerified',as_index=False).agg({'TotalInteractions':'sum',})
fig1 = px.bar(verified_end,
            x = 'AreVerified',
            y = 'TotalInteractions',
            color = 'TotalInteractions',
            color_continuous_scale ='Rainbow',
            title = "Engagement By User Type")
# fig1.show()

#%%