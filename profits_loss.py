from pathlib import Path
import csv

# file_path = Path("csv_report/ProfitAndLoss.csv")
def netprofit_difference():
    net_profit_diff = []

    file_path = Path.cwd()/"csv_report"/"ProfitAndLoss.csv"

    with file_path.open(mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        next(csv_reader)  
        previous_net_profit = 0
        
        for row in csv_reader:
            day = int(row[0])
            current_net_profit = int(row[4])
            if current_net_profit < previous_net_profit:
                difference =previous_net_profit - current_net_profit
                net_profit_diff.append((day, difference))  # Append as a tuple
                
            previous_net_profit = current_net_profit
            
    return net_profit_diff


difference_list = netprofit_difference()

# Writing to the output file
output_file_path = Path("summary_report.txt")

# Use mode="a" to append data to the file
with output_file_path.open(mode="a", encoding="UTF-8") as output_file:
    for day, difference in difference_list:
        output_file.write(f"\n[PROFIT DEFICIT] Day: {day}, Amount: USD {difference}")
