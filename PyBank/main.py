#import modules 
import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#open the file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)






    

