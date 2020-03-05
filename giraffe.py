import pandas as pd
import numpy as np
from datetime import datetime
import re
import matplotlib



finance = pd.read_csv("///Users/mac/Desktop/tdp_finance_test_data_takehome.csv")
pd.set_option('display.max_columns', None)

#convert strings to dates
finance['birthdate'] = finance['birthdate'].astype('datetime64[ns]')
finance['donation_date'] = finance['donation_date'].astype('datetime64[ns]')

#convert strings to integers and remove $
finance['donation_amount'] = finance['donation_amount'].str.replace(r'\D', '').astype(int)

#max donation
print(finance.describe())

#three largest donations, however there are 24 donations for $300 in total
print(finance.nlargest(3, ['donation_amount']))
print(finance[finance['donation_amount'] > 299])

#repeated donors
pd.set_option('display.max_rows', None)
re_donor = finance.pivot_table(index=['birthdate','last_name', 'first_name','county'], aggfunc='size')
print(re_donor)

#5 donors who've given the most, cumulatively
#need to combine donor records/contribution amounts
high_donor = finance.pivot_table(index="county",values=["donation_amount"],aggfunc = 'sum')
print(high_donor.nlargest(5, ['donation_amount']))

#highest total donations per county
high_county = finance.pivot_table(index="county",values=["donation_amount"],aggfunc = 'sum')
print(high_county.nlargest(3, ['donation_amount']))


#smallest and largest average donations per county
avg_county = finance.pivot_table(index="county",values=["donation_amount"],aggfunc = 'mean')
print(avg_county.nlargest(5, ['donation_amount']))
print(avg_county.nsmallest(5, ['donation_amount']))

##Email String Cleaning & Proportions
#proportion of emails missing
print(finance.info())

#email domains- top 2: gmail and yahoo
finance['domain'] = finance['email'].str.split('@').str[1]
domain_count = finance.pivot_table(index=['domain'], aggfunc='size')
print(domain_count)

##Date Manipulation & Analysis
#Dates with most donations
mode_date = finance['donation_date'].value_counts()[0:5]
print(mode_date)

#seasonal effects


#donor age

