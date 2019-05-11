#import modules 
import csv
csvpath = 'budget_data.csv'
output_path = "/Users/jihanmckenzie/Desktop/Python-Challenge/PyBank/PyBank.txt"
total_months = 0
total_profits_losses = 0
greatest_increase_date = ""
greatest_decrease_date = ""
greatest_increase = 0
greatest_decrease = 0


change_list =[]
#open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    #check that it reads
    print(csvreader)
    header = next(csvreader)
    first_row = next(csvreader)
    previous_net = int(first_row[1])
    total_months = total_months + 1
    total_profits_losses = total_profits_losses + int(first_row[1])    
    #run loop to find sum
    for row in csvreader:
        total_months = total_months + 1
        #Finding The net total amount of "Profit/Losses" over the entire period
        total_profits_losses = total_profits_losses + int(row[1])
        #The average of the changes in "Profit/Losses" over the entire period
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        change_list = change_list + [net_change]
        #The greatest increase in profits (date and amount) over the entire period
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_date = row[0]
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_date = row[0]


print("Financial Analysis")

print("--------------------")


monthly_average = sum(change_list)/len(change_list)

print(f'Total Months Equals {total_months}')
print(f"Total Profit Loss: ${total_profits_losses}") 
print(f"Monthly Average equals: {monthly_average:.2f}")
print(f"Greatest Decrease equals: ${greatest_decrease} on {greatest_decrease_date}")
print(f"Greatest Inrease equals: ${greatest_increase} on {greatest_increase_date}")


with open(output_path, 'w', newline='') as pybfile: 
    writer= csv.writer(pybfile, delimiter=' ', escapechar=" " , quoting= csv.QUOTE_NONE)
    writer.writerow([f"Total Months Equals {total_months}"])
    writer.writerow([f"Total Profit Loss: ${total_profits_losses}"])
    writer.writerow([f"Monthly Average equals: {monthly_average:.2f}"])
    writer.writerow([f"Greatest Decrease equals: ${greatest_decrease} on {greatest_decrease_date}"])
    writer.writerow([f"Greatest Inrease equals: ${greatest_increase} on {greatest_increase_date}"])





    




    

    








    