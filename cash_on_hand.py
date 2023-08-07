from pathlib import Path
import csv

# Create a file path to the CSV file
fp = Path("csv_report/cash_on_hand.csv")

def coh_differences(fp):
    """Computes the difference in Cash-on-Hand if the current day is lower than the previous day.

    1 parameter:
    fp: A Path object pointing to the CSV file.

    Returns:
    A list of tuples, where each tuple contains the Day and Cash-on-Hand in Cash-on-Hand for a single day.
    """
    difference_in_cash_on_hand = []

    #Open CSV file
    with fp.open(mode ="r", encoding = "UTF-8", newline = "") as file:
     reader = csv.reader(file)
     next(reader) #skip header

     # Initialize the previous_cash_on_hand
     previous_cash_on_hand = 0
    
     for row in reader:
        day = int(row[0])
        cash_on_hand = int(row[1])
            
         
        if cash_on_hand < previous_cash_on_hand:
            difference_in_cash_on_hand.append((day, cash_on_hand))
           
        previous_cash_on_hand = cash_on_hand # Update the previous_cash_on_hand for the next iteration  
            
    return difference_in_cash_on_hand

differences = coh_differences(fp)

    # Create a path object for the summary_report.txt in the home directory
output_file_path = Path("summary_report.txt")


    # Use mode="a" to append data to the file
with open(output_file_path, "a") as f:
    for day, cash_on_hand in differences:
        f.write(f"\n[CASH DEFICIT]Day: {day}, Amount: USD{cash_on_hand}")



