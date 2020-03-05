import pandas as pd
import numpy as np
import datetime
import re
import matplotlib

finance = pd.read_csv("///Users/mac/Desktop/tdp_finance_test_data_takehome.csv")
pd.set_option('display.max_columns', None)

# convert strings to dates
finance['birthdate'] = finance['birthdate'].astype('datetime64[ns]')
finance['donation_date'] = finance['donation_date'].astype('datetime64[ns]')

# convert strings to integers and remove $
finance['donation_amount'] = finance['donation_amount'].str.replace(r'\D', '').astype(int)

# max donation : $300
print(finance.describe())

# three largest donations, however there are 24 donations for $300 in total
# Samuel Sanabria on 01/01/19
# Jeffery Tong on 10/16/29
# Josephine Hardison on 04/27/19
print(finance.nlargest(3, ['donation_amount']))
print(finance[finance['donation_amount'] > 299])

# repeat donors
# proportion of donors that donated more than once: 1418/12378 = 11.46%
# proportion of donors that donated more than twice: 196/12378 = 1.58%
pd.set_option('display.max_rows', None)
re_donor = finance.pivot_table(index=['birthdate','last_name', 'first_name','county'], aggfunc='size')
print(re_donor)

# 5 donors who've given the most, cumulatively
# need to combine donor records/contribution amounts
high_donor = finance.pivot_table(index="county",values=["donation_amount"],aggfunc = 'sum')
print(high_donor.nlargest(5, ['donation_amount']))

# highest total donations per county
# HARRIS            $138,655
# DALLAS             $78,355
# TARRANT            $74,244
high_county = finance.pivot_table(index="county",values=["donation_amount"],aggfunc = 'sum')
print(high_county.nlargest(3, ['donation_amount']))


# largest average donations per county
# GARZA             $171.00
# CLAY              $129.63
# CRANE             $125.33
# SAN SABA          $120.00
# SHACKELFORD       $119.00

# smallest average donations per county

# TERRELL               $4.00
# HEMPHILL              $8.00
# EDWARDS              $10.00
# FISHER               $24.50
# ARCHER               $27.50

avg_county = finance.pivot_table(index="county",values=["donation_amount"],aggfunc = 'mean')
print(avg_county.nlargest(5, ['donation_amount']))
print(avg_county.nsmallest(5, ['donation_amount']))

## Email String Cleaning & Proportions
# proportion of emails missing: 23.83%
print(finance.info())

# email domains- top 2: gmail and yahoo
finance['domain'] = finance['email'].str.split('@').str[1]
domain_count = finance.pivot_table(index=['domain'], aggfunc='size')
print(domain_count)

## Date Manipulation & Analysis
# dates with most donations: 02/27/2019
mode_date = finance['donation_date'].value_counts()[0:5]
print(mode_date)

#seasonal effects


#donor age

