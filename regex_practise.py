import re 


working_list=[]
with open("demonetization_tweets.txt",'r') as file:
    iter_file = file.readlines()
    line_counter = 0 
    for line in iter_file:
        line_counter += 1
        working_list.append(line)
    


