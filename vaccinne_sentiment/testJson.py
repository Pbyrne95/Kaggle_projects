import json

#dictionary called data to hold the json file as you add functionality to it 
data = {}

with open('output.json','r') as json_file:
    # Sorry Fam
    data = json.load(json_file)

hashtags,dates = [],[]

for i,v in data.items():
    # iterates throughthe dict using the key as a value 
    if i == "hashtags":

        # if the key matches the hashtag print that part of the data 
        for hashTag in v:

            # the word variable is processed as an entire string not a list 
            words = v[hashTag]

            # taking the [] placheholders out as in this they do not signify a list type 
            words = words.replace('[','')
            words = words.replace(']','')
            hashtags.append([words])

    if i == "date":
        for date in v:
            # find the current date 
            current_date = v[date]
            dates.append(current_date)


# combine both of these list into one 
combinedList = list(zip(dates,hashtags))

# sort that list by most recent date first 
combinedList = sorted(combinedList, key = lambda x:x[0], reverse=True) 

#Include the list into dictionary 
data["HashtagsByDate"] = combinedList

#Append the updated column into original JSON file 
with open('output.json','a') as file_df:
    data = json.dump(data,file_df)
    file_df.close()