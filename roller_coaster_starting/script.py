import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
all_data = wood.merge(steel,how="left")

rcs = pd.read_csv("roller_coasters.csv")
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










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
