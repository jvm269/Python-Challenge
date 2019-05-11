#import modules 
import csv
csvpath = ('budget_data.csv')
total_months = 0
#open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    #check that it reads
    print(csvreader)
    #run loop to find sum
    for row in csvreader:
        total_months = total_months + 1
print(total_months)



    

    








    