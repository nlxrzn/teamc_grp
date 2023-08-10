from pathlib import Path
import csv


def netprofit_difference():
    """
    Calculates the differences in net Profit if the current day is lower than the previous day. 
    No parameter needed.
    Function reiterates data to calculate incremental profit deficit.

    """
    net_profit_diff = []

    # Create file path to the csv file 
    file_path = Path.cwd() / "csv_reports" / "ProfitAndLoss.csv"

    with file_path.open(mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        next(csv_reader)  
        previous_net_profit = 0
        
        # Reiterate through data to determine profit deficit
        for row in csv_reader:
            day = int(row[0])
            current_net_profit = int(row[4])
            if current_net_profit < previous_net_profit:
                difference =previous_net_profit - current_net_profit
                net_profit_diff.append((day, difference))  # Append as a tuple
                
            previous_net_profit = current_net_profit   # Move this line within the loop
            
    return net_profit_diff


difference_list = netprofit_difference()

# Use mode="a" to append data to the file
with open(Path("summary_report.txt"), 'a') as f:
    for day, difference in difference_list:
        f.write(f"\n[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{difference}")

