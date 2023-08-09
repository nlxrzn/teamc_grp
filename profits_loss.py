from pathlib import Path
import csv

file_path = Path("teamc_grp\csv_report\ProfitAndLoss.csv")
def netprofit_difference(file_path):
    net_profit_diff = []
    
    with file_path.open(mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        next(csv_reader)  
        previous_net_profit = 0
        
        for row in csv_reader:
            day = int(row[0])
            current_net_profit = int(row[4])
            if current_net_profit < previous_net_profit:
                net_profit_diff.append((day, current_net_profit))  # Append as a tuple
                
            previous_net_profit = current_net_profit
            
    return net_profit_diff

csv_file_path = Path("teamc_grp\csv_report\ProfitAndLoss.csv")
difference_list = netprofit_difference(file_path)

# Writing to the output file
output_file_path = Path("summary_report.txt")

# Use mode="a" to append data to the file
with output_file_path.open(mode="a", encoding="UTF-8") as output_file:
    for day, net_profit in difference_list:
        output_file.write(f"\n[PROFIT DEFICIT] Day: {day}, Amount: USD {net_profit}")
