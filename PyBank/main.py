# import modules
import os
import csv

# Read in CSV
file_path= os.path.join("Resources", "budget_data.csv")


month_count= []
total_months= 0
revenue_total= []
revenue_loss= 1
revenue_change= []

# Open the cvs file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader) 
    
# Loop csv
    for row in csvreader:
# Count months
        total_months += 1
        month_count.append(row[0])
        
        revenue_total.append(int(row[1]))

    for i in range(len(revenue_total)-1):
        revenue_change.append(revenue_total[i+1]-revenue_total[i])
        
#Define and compare max, min revenue values        
max_increase= max(revenue_change)
max_decrease= min(revenue_change)

max_month_increase= revenue_change.index(max(revenue_change)) + 1
max_month_decrease= revenue_change.index(min(revenue_change)) - 1



print("Financial Summary")
print("---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Net Revenue: $ {sum(revenue_total)}")

print(f"Max Revenue Increase: {month_count[max_month_increase]} (${(str(max_increase))})")

print(f"Max Revenue Decrease: {month_count[max_month_decrease]} (${(str(max_decrease))})")
print(f"Avg Change is: {round(sum(revenue_change)/len(revenue_change),2)}")


output_path= os.path.join("Analysis", "budget_results.txt")
with open(output_path, "w") as csvfile:
    csvwriter= csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Financial Summary"])
    csvwriter.writerow(["-------------------------------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total Net Revenue: $ {sum(revenue_total)}"])
    csvwriter.writerow([f"Max Revenue Increase: {month_count[max_month_increase]} (${(str(max_increase))})"])
    csvwriter.writerow([f"Max Revenue Decrease: {month_count[max_month_decrease]} (${(str(max_decrease))})"])
    csvwriter.writerow([f"Avg Change is: {round(sum(revenue_change)/len(revenue_change),2)}"])