from pathlib import Path
import csv

# Create a file path to the CSV file

def coh_differences():
    """Computes the difference in Cash-on-Hand if the current day is lower than the previous day.


    Returns:
    A list of tuples, where each tuple contains the Day and Cash-on-Hand in Cash-on-Hand for a single day.
    """
    difference_in_cash_on_hand = []

    difference_in_cash_on_hand = []

    # Create a file path to the CSV file
    fp = Path.cwd() / "csv_report" / "cash_on_hand.csv"

    # Open CSV file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # Initialize the previous_cash_on_hand
        previous_cash_on_hand = 0

        for row in reader:
            day = int(row[0])
            cash_on_hand = int(row[1])

            if cash_on_hand < previous_cash_on_hand:
                difference = previous_cash_on_hand - cash_on_hand
                difference_in_cash_on_hand.append((day, difference))
           
        previous_cash_on_hand = cash_on_hand # Update the previous_cash_on_hand for the next iteration  
            
    return difference_in_cash_on_hand

cash_differences = coh_differences()

    # Create a path object for the summary_report.txt in the home directory
output_file_path = Path("teamc_grp/summary_report.txt")

    # Use mode="a" to append data to the file
with output_file_path.open(mode="a", encoding="UTF-8") as output_file:
    for day, difference in cash_differences:
        output_file.write(f"\n[CASH DEFICIT]Day: {day}, Amount: USD{difference}")



