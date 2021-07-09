import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
all_data = wood.merge(steel,how="left")

rcs = pd.read_csv("roller_coasters.csv")
rcs['status'] = rcs.status.apply(lambda row:True if row == "status.operating" else False)
#print(wood.head())

# write function to plot rankings over time for 1 roller coaster here:
def show_rank(name,parkname,df):
    matching_creteria = df[(df.Name == name) & (df.Park == parkname)]
    plt.plot(matching_creteria.Points,matching_creteria["Year of Rank"], marker = 'o', color='b')
    plt.title("haha over time")
    plt.xlabel("Ranking")
    plt.ylabel("Year")
    plt.show()
# show_rank("El Toro","Six Flags Great Adventure",all_data)
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def two_coasters(a_name, a_park, b_name, b_park, dataf):
    c_1 = dataf[(dataf.Name == a_name) & (dataf.Park == a_park)]
    c_2 = dataf[(dataf.Name == b_name) & (dataf.Park == b_park)]
    plt.figure(figsize=(18,12))
    ax = plt.subplot()
    ax.plot(c_1['Year of Rank'],c_1['Points'],marker='o',color='b',label=a_name)
    ax.plot(c_2['Year of Rank'],c_2['Points'],marker='o',color='r',label=b_name)
    plt.legend([a_name,b_name])
    plt.title('Rank over year')
    plt.xlabel('Years')
    plt.ylabel('Ranking')
    plt.show()

plt.clf()

# write function to plot top n rankings over time here:

def top_ranks(dataf,n):
    data_points = dataf[dataf.Points <= n]
    top_points = sorted(list(set(zip(data_points['Year of Rank'],data_points['Points']))),reverse=True)
    years = [i[0] for i in top_points]
    ranking = [i[1] for i in top_points]
    plt.plot(years,ranking,marker='o',color='b')
    plt.show()


# print(top_ranks(all_data,150))

plt.clf()

# write function to plot histogram of column values here:
def teo_numeric_vals(dataf,columnName):
    import numpy as np 
    data_to_compare = dataf[columnName].dropna()  
    plt.hist(data_to_compare,density=False,bins=np.arange(0,20))
    plt.title("comprasion of {} ".format(columnName))
    plt.xlabel(columnName)
    plt.ylabel("Frequency")
    plt.show()

    
# print(teo_numeric_vals(rcs,"height"))

plt.clf()

# write function to plot inversions by coaster at a park here:

def inversions(dataf,park):
    park_data = dataf[(dataf.park == park)]
    n_inversions = park_data.num_inversions
    len_coaster_name = range(len(park_data.name))
    plt.bar(len_coaster_name,n_inversions)
    plt.title("Number of inversation in {} park".format(park))
    plt.xlabel("Inversions")
    plt.ylabel("No of coasters")
    ax = plt.subplot()
    ax.set_xticks(len_coaster_name)
    ax.set_xticklabels(park_data.name,rotation=90)
    plt.show()


plt.clf()

# write function to plot pie chart of operating status here:

def amount_of_oper(dataf,park_name):
 
    total_coasters = len(dataf.park == park_name)
    dataf = dataf[dataf.park == park_name]
    # need to compare amount of closures in each park 
    count_dict = dict()
    for row1,row2  in list(zip(dataf.park,dataf.status)):
        if row2 == False: continue
        elif row1 not in count_dict and row2 == True:
            count_dict[row1] = 1
        elif row1 in count_dict and row2 == True:
            count_dict[row1] += 1
    park_names = []
    operating =[]
    for x,y in count_dict.items(): park_names.append(x),operating.append(y)
    
    plt.pie(operating,labels=park_names)
    plt.show()
        


def total_amonut(dataf):
    total_operating = len(dataf.status == True)
    not_operating = len(dataf.status == False)
    plt.pie([total_operating,not_operating],autopct="%1d%%")
    plt.axis("equal")
    plt.title("Current Running Condition for Roller Coasters")
    plt.legend(["Operating", "Closed Definitely"])
    plt.show()



plt.clf()

# write function to create scatter plot of any two numeric columns here:


def two_nemeric(dataf,colmnName1,columnName2):
    plt.scatter(dataf[colmnName1],dataf[columnName2])
    plt.title("The realasionship between {} and {}".format(colmnName1,columnName2))
    plt.ylabel(colmnName1)
    plt.xlabel(columnName2)
    plt.show()







plt.clf()
