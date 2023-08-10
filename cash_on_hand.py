from pathlib import Path
import csv

def coh_differences():
    """
    Function calculates incremental difference in cash deficit
    No parameters needed
    Function reiterates through data to determine cash deifict 

    """
    difference_in_cash_on_hand = []

    # Create a file path to the CSV file
    file_path = Path.cwd() / "csv_reports" / "cash_on_hand.csv"

    # Open CSV file
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # Initialise the previous_cash_on_hand
        previous_cash_on_hand = 0.0  # Change this to a floating-point number

        for row in reader:
            day = int(row[0])
            cash_on_hand = int(row[1])  # Parse the cash on hand as an integer

            if cash_on_hand < previous_cash_on_hand:
                difference = previous_cash_on_hand - cash_on_hand
                difference_in_cash_on_hand.append((day, difference))
            
            previous_cash_on_hand = cash_on_hand  # Move this line within the loop

    return difference_in_cash_on_hand

cash_differences = coh_differences()

# Use mode="a" to append data to the file
with open(Path("summary_report.txt"), 'a') as f:
    for day, difference in cash_differences:
        f.write(f"\n[CASH DEFICIT] DAY: {day}, AMOUNT: USD{difference}")  # Format the difference as a float with 2 decimal places