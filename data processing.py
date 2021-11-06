
# import libraries
import csv
import pandas as pd
from matplotlib import pyplot as plt
from pprint import pprint
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

file = open("uber_data.csv")
dat = csv.reader(file)
# skip the title
colnames = next(dat)
# create a list of comments
com_list = []

# iterate through the rows
for row in dat:
    # add the comment into the list
    com_list.append(row[3])
    
# print out the list
print(len(com_list))

# create a testing list
test_list = []
for n in range (30):
    print(sia.polarity_scores(com_list[n]), "\n")

print(sia.polarity_scores(com_list[0]))



# open the data file
# with open('uber_data.csv') as csv_file:
 # csv_reader = csv.reader(csv_file)
  

file.close()