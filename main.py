import csv
import os

# Path to collect data from the Resources folder
mypath = 'C:/Users/remna/Desktop/Python_Assignment/python-challenge-master/python_challenge_pybank/PyBank/Resources'
budgetCSV = os.path.join(mypath, 'budget_data.csv')
output_file = 'C:/Users/remna/Desktop/Python_Assignment/python-challenge-master/python_challenge_pybank/PyBank/Resources/budget_analysis.txt'
# Variables to Track
totalMonths = 0
totalNet = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

# Read Files
with open(budgetCSV) as revenue_data:
    reader = csv.DictReader(revenue_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        totalMonths = totalMonths + 1
        totalNet = totalNet + int(row["Profit/Losses"])
        # print(row)

        # Keep track of changes
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        # print(revenue_change)

        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row["Profit/Losses"])
        # print(prev_revenue)

        # Determining the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        # Add to the revenue_changes list
        revenue_changes.append(int(row["Profit/Losses"]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total Revenue: " + "$" + str(totalNet))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    


# Output Files
with open(output_file, "w") as txt_file:
    txt_file.write("Total Months: " + str(totalMonths))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(totalNet))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")