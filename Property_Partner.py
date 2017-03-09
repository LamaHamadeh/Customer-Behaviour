# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:58:32 2016

@author: ADB3HAMADL
"""

"""
Created on Fri Dec 16 13:01:27 2016
Author: Lama Hamadeh
Software: I use Spyder (Python 2.7) to write the following code
The aim: Analyse the data and look for the behavioural differences between investors and non-investors
The Question:
We have attached a small subset of data from our front end events database. Dataset focuses on behavioural activity before 
user makes their first investment. Each of the lines is a distinct user's behaviour before making the first investment. 
You will note that not everyone from this dataset made the first investment. What we would like you to do is to analyse 
the data and look for the behavioural differences between investors and non-investors.
"""

#---------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 14:11:11 2017

@author: ADB3HAMADL
"""

#importing pandas
#----------------
import pandas as pd


#reading the dataframe from .csv file
#-------------------------------------
Behaviour = pd.read_csv('/Users/ADB3HAMADL/Desktop/user to 1st time investor.csv')


#print the length of thr dataframe
#-----------------------------------
#print(len(Behaviour)) # the whole dataframe contains 263501 customers


#print the first 5 lines fo the datset to take a quick look at it
#------------------------------------------------------------------
#print Behaviour.head(5)


#checking the types of the dataset features
#-----------------------------------------
print Behaviour.dtypes
# it can be seen form the types that 'time_to_sign_up_from_first_visit_days' and 'first_visit_to_first_investment_days' have type object
#they have to be converted to numeri values in order to be compatible with the other features when plotted.
Behaviour['time_to_sign_up_from_first_visit_days'] = pd.to_numeric(Behaviour['time_to_sign_up_from_first_visit_days'], errors='coerce')
Behaviour['first_visit_to_first_investment_days'] = pd.to_numeric(Behaviour['first_visit_to_first_investment_days'], errors='coerce')
print Behaviour.dtypes #it can be seen that the last two features have been converted to 'float'


#identify nans
#-------------
def num_missing(x):
  return sum(x.isnull())
#Applying per column:
#print ("Missing values per column:")
print (Behaviour.apply(num_missing, axis=0)) #no Nans in the dataframe
#

#Create a slice called investor that filters to only include the investors dataset records 
#-----------------------------------------------------------------------------------------
investor = Behaviour[(Behaviour.investor_status == 'investor')]
#print len(investor) #1359 investor customers


#Create a slice called non_investor that filters to only include the investors dataset records 
#----------------------------------------------------------------------------------------------
non_investor = Behaviour[(Behaviour.investor_status == 'non-investor')]
#print len(non_investor) #262142 non-investor customers


#plotting data
#--------------

import numpy as np
import matplotlib.pyplot as plt

#Each dataset has 14 features:
#------------------------------
#distinct days visited website --> A
#distinct_properties_viewed --> B            
#time on properties --> C                       
#interactions on property page --> D            
#times marketplace filter used --> E            
#dashboard interactions --> F                   
#time on howitworks --> G                       
#time on faqs --> H                             
#time on aboutus --> I                          
#time on team --> J                            
#time on homepage --> K                         
#time on marketplace --> L                      
#time to sign up from first visit days --> M    
#first visit to first investment days --> N 


#investors subdata
#-----------------

# Create a list of the mean value for each feature
mean_values1 = [investor['distinct_days_visited_website'].mean(), investor['distinct_properties_viewed'].mean(), investor['time_on_properties'].mean(),
               investor['interactions_on_property_page'].mean(),investor['times_marketplace_filter_used'].mean(),
               investor['dashboard_interactions'].mean(),investor['time_on_howitworks'].mean(),investor['time_on_faqs'].mean(),
               investor['time_on_aboutus'].mean(),investor['time_on_team'].mean(),investor['time_on_homepage'].mean(),
               investor['time_on_marketplace'].mean(),investor['time_to_sign_up_from_first_visit_days'].mean(),investor['first_visit_to_first_investment_days'].mean()]

# Create a list of variances, which are set at .25 above and below the values
variance1 = [investor['distinct_days_visited_website'].mean()* 0.25, investor['distinct_properties_viewed'].mean()* 0.25, investor['time_on_properties'].mean()* 0.25,
            investor['interactions_on_property_page'].mean()*0.25,investor['times_marketplace_filter_used'].mean()* 0.25,
               investor['dashboard_interactions'].mean()* 0.25,investor['time_on_howitworks'].mean()* 0.25,investor['time_on_faqs'].mean()* 0.25,
               investor['time_on_aboutus'].mean()* 0.25,investor['time_on_team'].mean()* 0.25,investor['time_on_homepage'].mean()* 0.25,
               investor['time_on_marketplace'].mean()* 0.25,investor['time_to_sign_up_from_first_visit_days'].mean()* 0.25,investor['first_visit_to_first_investment_days'].mean()* 0.25]


# Set the bar labels
bar_labels1 = ['A', 'B', 'C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

# Create the x position of the bars
x_pos = list(range(len(bar_labels1)))

# Create the plot bars in x position
plt.bar(x_pos,
        # using the data from the mean_values
        mean_values1,
        # with a y-error lines set at variance
        yerr=variance1,
        # aligned in the center
        align='center',
        # with color
        color='blue',
        # alpha 0.5
        alpha=0.5)

# add a grid
plt.grid()

# set height of the y-axis
max_y = max(zip(mean_values1, variance1)) # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])


# set axes labels and title
plt.ylabel('Investors Behaviour')
plt.xticks(x_pos, bar_labels1)
plt.title('Mean Behaviour For Investors')

plt.show()


#non-investors subdata
#----------------------

# Create a list of the mean value for each feature
mean_values2 = [non_investor['distinct_days_visited_website'].mean(), non_investor['distinct_properties_viewed'].mean(), non_investor['time_on_properties'].mean(),
               non_investor['interactions_on_property_page'].mean(),non_investor['times_marketplace_filter_used'].mean(),
               non_investor['dashboard_interactions'].mean(),non_investor['time_on_howitworks'].mean(),non_investor['time_on_faqs'].mean(),
               non_investor['time_on_aboutus'].mean(),non_investor['time_on_team'].mean(),non_investor['time_on_homepage'].mean(),
               non_investor['time_on_marketplace'].mean(),non_investor['time_to_sign_up_from_first_visit_days'].mean(),non_investor['first_visit_to_first_investment_days'].mean()]

# Create a list of variances, which are set at .25 above and below the values
variance2 = [non_investor['distinct_days_visited_website'].mean()* 0.25, non_investor['distinct_properties_viewed'].mean()* 0.25, non_investor['time_on_properties'].mean()* 0.25,
            non_investor['interactions_on_property_page'].mean()*0.25,non_investor['times_marketplace_filter_used'].mean()* 0.25,
               non_investor['dashboard_interactions'].mean()* 0.25,non_investor['time_on_howitworks'].mean()* 0.25,non_investor['time_on_faqs'].mean()* 0.25,
               non_investor['time_on_aboutus'].mean()* 0.25,non_investor['time_on_team'].mean()* 0.25,non_investor['time_on_homepage'].mean()* 0.25,
               non_investor['time_on_marketplace'].mean()* 0.25,non_investor['time_to_sign_up_from_first_visit_days'].mean()* 0.25,non_investor['first_visit_to_first_investment_days'].mean()* 0.25]


# Set the bar labels
bar_labels2 = ['A', 'B', 'C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

# Create the x position of the bars
x_pos = list(range(len(bar_labels2)))

# Create the plot bars in x position
plt.bar(x_pos,
        # using the data from the mean_values
        mean_values2,
        # with a y-error lines set at variance
        yerr=variance2,
        # aligned in the center
        align='center',
        # with color
        color='red',
        # alpha 0.5
        alpha=0.5)

# add a grid
plt.grid()

# set height of the y-axis
max_y = max(zip(mean_values2, variance2)) # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])


# set axes labels and title
plt.ylabel('Non-investors Behaviour')
plt.xticks(x_pos, bar_labels2)
plt.title('Mean Behaviour For Non-investors')

plt.show()

#------------------------------------------------------------------------------




