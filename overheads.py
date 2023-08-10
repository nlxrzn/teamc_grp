from pathlib import Path
import csv

# Function to find highest overhead category and 
# its corresponding expense
def find_highest_overhead_category():
    """
    Find the highest overhead category and its corresponding expense.
    0 parameter required 
    The parameter represents the path to the CSV file. It is passed to the function when calling it.
    """
    # Path to the CSV file 
    fp = Path.cwd() / "csv_report" / "overheadsfilecsv.csv"
    overhead_data = []
    # Open and read the CSV file
    with fp.open(mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        next(csv_reader)  
        for row in csv_reader:
            category = row[0]
            expense = float(row[1])
            overhead_data.append((category, expense))

    # Initialise variables to track highest overhead
    max_expense = 0
    highest_overhead_category = ""

    # Iterate through overhead data to find the 
    # highest expense category
    for category, expense in overhead_data:
        if expense > max_expense:
            max_expense = expense
            highest_overhead_category = category
    
    return highest_overhead_category, max_expense
    
highest_category, max_expense = find_highest_overhead_category()

# Write the summary to a text file
with open(Path("teamc_grp"), 'w') as f:
    f.write(f"[HIGHEST OVERHEAD]: {highest_category.upper()}: {max_expense:.2f}%")