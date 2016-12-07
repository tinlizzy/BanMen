
# coding: utf-8

# In[1]:

import csv

# set local csv file to read from
csvfile = "/somedir/mytweetFile.csv"
   
# count the num of rows in the csv file
with open(csvfile,"rU") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)

# generate a random number between 1 and the num of rows in the spreadsheet
# i.e. 0 thru row_count-1, since 1st row = row 0
import random
for x in range(1):
    RandNum = random.randint(0,(row_count-1))

# define tweetfile as a dataframe 
import pandas as pd
tweetFile = pd.read_csv(csvfile, header=None, encoding='utf-8')

# extract tweet from the RandNum-th row of the csv tweet column
msg = tweetFile.iloc[RandNum,0]

# Import the relevant Twitter libraries so you can post to Twitter.
import twitter
from twitter import TwitterError

# Set your Twitter API credentials.
api = twitter.Api(consumer_key='pullFromYourTwitterAPI',
                  consumer_secret='pullFromYourTwitterAPI',
                  access_token_key='pullFromYourTwitterAPI',
                  access_token_secret='pullFromYourTwitterAPI')

# try to post the tweet you randomly pulled/set above
try:
    status = api.PostUpdate(msg)
    print(status.text)

# if 1st tweet attempt is a dupe tweet, try this block to generate a new random number & tweet msg
except TwitterError:  
    for x in range(1):
        RandNum = random.randint(0,(row_count-1))
    msg = tweetFile.iloc[RandNum,0]
    status = api.PostUpdate(msg)
    print(status.text)


