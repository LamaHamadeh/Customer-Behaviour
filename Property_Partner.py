# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 14:11:11 2017
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

#importing libraries
#-------------------
import pandas as pd #pandas
import numpy as np #numpy
import matplotlib.pyplot as plt #matplotlib
from matplotlib import style #style
style.use("ggplot") #look pretty
from sklearn import preprocessing 

#reading the dataframe from .csv file
#-------------------------------------
Behaviour = pd.read_csv('/Users/lamahamadeh/Downloads/Real_Estate/user_to_1st_time_investor.csv')


#take a look at the dataset
#---------------------------
print (Behaviour.shape) #(263501, 16)
print (Behaviour.head(4))
print (Behaviour.describe())


#checking the types of the dataset features
#-----------------------------------------
print (Behaviour.dtypes)
# We need to change 'time_to_sign_up_from_first_visit_days' and 'first_visit_to_first_investment_days'
# to numeri values in order to be compatible with the other features when plotted.
Behaviour['time_to_sign_up_from_first_visit_days'] = pd.to_numeric(Behaviour['time_to_sign_up_from_first_visit_days'], errors='coerce')
Behaviour['first_visit_to_first_investment_days'] = pd.to_numeric(Behaviour['first_visit_to_first_investment_days'], errors='coerce')
print (Behaviour.dtypes) #it can be seen that the last two features have been converted to 'float'


#identify nans
#-------------
def num_missing(x):
  return sum(x.isnull())
#Applying per column:
print ("Missing values per column:")
print (Behaviour.apply(num_missing, axis=0)) #251338 nans in the 'time to sign up from first visit days ' feature
#and 262142 nans in the 'first visit to first investment days' feature. 


#in the following we are going to analyse the behaviour of the customers, investors and non_investors
#taking in our consideration only the following features:
#Each dataset has 12 features:
#------------------------------
#distinct days visited website
#distinct_properties_viewed           
#time on properties                      
#interactions on property page           
#times marketplace filter used            
#dashboard interactions                  
#time on howitworks                      
#time on faqs                            
#time on aboutus                         
#time on team                            
#time on homepage                        
#time on marketplace                      
#and that is because, the 'guid' feature is irrelevant to our study, and the last two features have 
# a large number of nans.


#drop unnecessary features:
#--------------------------
Behaviour.drop(['guid', 'time_to_sign_up_from_first_visit_days',
                'first_visit_to_first_investment_days'], axis=1)


#Create a slice called investor that includes only the investors records 
#------------------------------------------------------------------------
investor = Behaviour[(Behaviour.investor_status == 'investor')]
print(investor.shape) #(1359, 16) the dataset has 1359 investors

#normalise data
columns = ['distinct_days_visited_website', 'distinct_properties_viewed', 
           'time_on_properties', 'interactions_on_property_page', 
           'times_marketplace_filter_used', 'dashboard_interactions', 
           'time_on_howitworks', 'time_on_faqs', 'time_on_aboutus', 
           'time_on_team', 'time_on_homepage', 'time_on_marketplace']
X_investor = np.array(investor[columns].values) #convert the dataset from a dataframe to an nd.numpy array
X_investor = preprocessing.normalize(X_investor, axis=0, norm= 'max')

#plotting data


#Create a slice called non_investor that includes only the non_investors records 
#--------------------------------------------------------------------------------
non_investor = Behaviour[(Behaviour.investor_status == 'non-investor')]
print(non_investor.shape) #(262142, 16) the dataset has 262142 non_investors

#normalise data
columns = ['distinct_days_visited_website', 'distinct_properties_viewed', 
           'time_on_properties', 'interactions_on_property_page', 
           'times_marketplace_filter_used', 'dashboard_interactions', 
           'time_on_howitworks', 'time_on_faqs', 'time_on_aboutus', 
           'time_on_team', 'time_on_homepage', 'time_on_marketplace']
X_non_investor = np.array(non_investor[columns].values) #convert the dataset from a dataframe to an nd.numpy array
X_non_investor = preprocessing.normalize(X_non_investor, axis=0, norm= 'max')

#plotting data




#------------------------------------------------------------------------------
