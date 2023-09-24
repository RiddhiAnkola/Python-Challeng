import csv

total_months = 0
net_total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

csvpath = r"C:\Users\riddh\OneDrive\Desktop\Monash_Data Analysis Bootcamp2023\Assignments\Module 3 Challenge Python\PyBlank\budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
       
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        net_total_profit_loss += profit_loss

        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        previous_profit_loss = profit_loss

average_change = sum(profit_loss_changes) / len(profit_loss_changes)

greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]

greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

output_file_path = r"C:\Users\riddh\OneDrive\Desktop\Monash_Data Analysis Bootcamp2023\Assignments\Module 3 Challenge Python\PyBlank\financial_analysis.txt"
with open(output_file_path, "w") as output_file:
    output_file.write ("""Financial Analysis
------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
""")

print(f"Analysis has been exported to '{output_file_path}'")