
"""
Created on Fri Dec 16 13:01:27 2016

Author: Lama Hamadeh
Software: I use Spyder 3.0.2 (Python 3.5) to write the following code
The aim: Analyse the data and look for the behavioural differences between investors and non-investors
The Question:
We have attached a small subset of data from our front end events database. Dataset focuses on behavioural activity before 
user makes their first investment. Each of the lines is a distinct user's behaviour before making the first investment. 
You will note that not everyone from this dataset made the first investment. What we would like you to do is to analyse 
the data and look for the behavioural differences between investors and non-investors.
"""


#Import the necessary modules and packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


#Import the dataset from the csv file
df=pd.read_csv('/Users/lamahamadeh/Downloads/user_to_1st_time_investor.csv')
df.dropna(axis = 0, how = 'any', inplace = True)
df.sort_values('investor_status', axis=0, ascending=True, inplace=True)
#print(df) #take a look at the dataset
# The dataset focuses on behavioural activity before users make their first investment
print(df.dtypes) #check the types of the dataset features

print(len(df))

#Create a slice called df_investor that filters to only include the investors dataset records 
df_investor = df[(df.investor_status == 'investor')]
print(len(df_investor)) #The dataset contains 1359 investors
print(df_investor.head())
#df_investor.plot.scatter(x='distinct_days_visited_website', y='distinct_properties_viewed', c='Blue')
#plt.show()
df_investor.drop(['investor_status'],inplace=True,axis=1)
print(df_investor.describe())
#print(df_investor.plot.hist())




# Create a list of the mean scores for each variable
mean_values = [df_investor['distinct_days_visited_website'].mean(), df_investor['distinct_properties_viewed'].mean(), df_investor['time_on_properties'].mean(),df_investor['interactions_on_property_page'].mean(),df_investor['times_marketplace_filter_used'].mean(),df_investor['dashboard_interactions'].mean(),df_investor['time_on_howitworks'].mean(),df_investor['time_on_faqs'].mean(),df_investor['time_on_aboutus'].mean(),df_investor['time_on_team'].mean(),df_investor['time_on_homepage'].mean(),df_investor['time_on_marketplace'].mean()]

# Create a list of variances, which are set at .25 above and below the score
variance = [df_investor['distinct_days_visited_website'].mean() * 0.25, df_investor['distinct_properties_viewed'].mean() * 0.25, df_investor['time_on_properties'].mean() * 0.25, df_investor['interactions_on_property_page'].mean() * 0.25, df_investor['times_marketplace_filter_used'].mean() * 0.25, df_investor['dashboard_interactions'].mean() * 0.25, df_investor['time_on_howitworks'].mean() * 0.25, df_investor['time_on_faqs'].mean() * 0.25, df_investor['time_on_aboutus'].mean() * 0.25, df_investor['time_on_team'].mean() * 0.25, df_investor['time_on_homepage'].mean() * 0.25, df_investor['time_on_marketplace'].mean() * 0.25]

# Set the bar labels
bar_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

# Create the x position of the bars
x_pos = list(range(len(bar_labels)))

# Create the plot bars
# In x position
plt.bar(x_pos,
        # using the data from the mean_values
        mean_values, 
        # with a y-error lines set at variance
        yerr=variance, 
        # aligned in the center
        align='center',
        # with color
        color='blue',
        # alpha 0.5
        alpha=0.5,
        linewidth =0)



# set height of the y-axis
max_y = max(zip(mean_values, variance)) # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])

# set axes labels and title
plt.ylabel('Behaviour')
plt.xticks(x_pos, bar_labels)
plt.title('Investors')
plt.show()


#--------------------------------

#Create another slice called df_non_investor that filters to only include the non-investors dataset records 
df_non_investor = df[(df.investor_status == 'non-investor')] 
print(len(df_non_investor)) #The dataset contains 262142 non-investors
print(df_non_investor.head())
#df_non_investor.plot.scatter(x='distinct_days_visited_website', y='distinct_properties_viewed', c='red')
#plt.show()
df_non_investor.drop(['investor_status'],inplace=True,axis=1)
print(df_non_investor.describe())
#print(df_non_investor.plot.hist())


# Create a list of the mean scores for each variable
mean_values = [df_non_investor['distinct_days_visited_website'].mean(), df_non_investor['distinct_properties_viewed'].mean(), df_non_investor['time_on_properties'].mean(),df_non_investor['interactions_on_property_page'].mean(),df_non_investor['times_marketplace_filter_used'].mean(),df_non_investor['dashboard_interactions'].mean(),df_non_investor['time_on_howitworks'].mean(),df_non_investor['time_on_faqs'].mean(),df_non_investor['time_on_aboutus'].mean(),df_non_investor['time_on_team'].mean(),df_non_investor['time_on_homepage'].mean(),df_non_investor['time_on_marketplace'].mean()]

# Create a list of variances, which are set at .25 above and below the score
variance = [df_non_investor['distinct_days_visited_website'].mean() * 0.25, df_non_investor['distinct_properties_viewed'].mean() * 0.25, df_non_investor['time_on_properties'].mean() * 0.25, df_non_investor['interactions_on_property_page'].mean() * 0.25, df_non_investor['times_marketplace_filter_used'].mean() * 0.25, df_non_investor['dashboard_interactions'].mean() * 0.25, df_non_investor['time_on_howitworks'].mean() * 0.25, df_non_investor['time_on_faqs'].mean() * 0.25, df_non_investor['time_on_aboutus'].mean() * 0.25, df_non_investor['time_on_team'].mean() * 0.25, df_non_investor['time_on_homepage'].mean() * 0.25, df_investor['time_on_marketplace'].mean() * 0.25]

# Set the bar labels
bar_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

# Create the x position of the bars
x_pos = list(range(len(bar_labels)))

# Create the plot bars
# In x position
plt.bar(x_pos,
        # using the data from the mean_values
        mean_values, 
        # with a y-error lines set at variance
        yerr=variance, 
        # aligned in the center
        align='center',
        # with color
        color='Red',
        # alpha 0.5
        alpha=0.5,
        linewidth =0)



# set height of the y-axis
max_y = max(zip(mean_values, variance)) # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])

# set axes labels and title
plt.ylabel('Behaviour')
plt.xticks(x_pos, bar_labels)
plt.title('Non-Investors')
plt.show()


#--------------------------------

'''

#to plot the relationship between two features and compare between both investor status
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(df_investor.distinct_days_visited_website,df_investor.interactions_on_property_page, c='Blue')
ax.scatter(df_non_investor.distinct_days_visited_website,df_non_investor.interactions_on_property_page, c='red')
plt.xlabel('distinct_days_visited_website')
plt.ylabel('interactions_on_property_page')

plt.show()
'''
