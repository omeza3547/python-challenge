# import modules
import os
import csv

# Read in CSV
file_path = os.path.join("Resources", "budget_data.csv")


months_count = []
total_months = 0
total_rev = []
row_index_revenue_loss = 1
rev_change = []

# Open the cvs file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader) 
    
# Loop csv
    for row in csvreader:
# Count months
        total_months += 1
        months_count.append(row[0])
        
# Net total of "profit/loss" over entire period and total rev
        total_rev.append(int(row[1]))

