# from pathlib import Path
# import csv
# # Function to find highest overhead category and 
# # its corresponding expense
# def find_highest_overhead_category(fhoc):
#     """
#     Find the highest overhead category and its corresponding expense.
#     Args: file_path (Path): The path to the CSV file containing overhead data.
#     Returns: tuple: A tuple containing the highest overhead category (str) and its corresponding expense (float).
#     """
#     overhead_data = []
#     # Open and read the CSV file
#     with file_path.open(mode="r") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         # Skip the header row
#         next(csv_reader)  
#         for row in csv_reader:
#             category = row[0]
#             expense = float(row[1])
#             overhead_data.append((category, expense))

#     # Initialise variables to track highest overhead
#     max_expense = 0
#     highest_overhead_category = ""

#     # Iterate through overhead data to find the 
#     # highest expense category
#     for category, expense in overhead_data:
#         if expense > max_expense:
#             max_expense = expense
#             highest_overhead_category = category
    
#     return highest_overhead_category, max_expense
    
# # Path to the CSV file 
# file_path = Path("teamc_grp/csv_report/overheadsfilecsv.csv")

# # Find the highest overhead category and expense using the function
# highest_category, max_expense = find_highest_overhead_category(file_path)

# # Write the summary to a text file
# with open('summary_report.txt', 'w') as f:
#     f.write(f"[HIGHEST OVERHEAD]: {highest_category.upper()}: {max_expense:.2f}%")

from pathlib import Path
import csv
file_path = Path.cwd() /"csv_report"/ "overheadsfilecsv.csv"
# Function to find highest overhead category and 
# its corresponding expense

# Open and read the CSV file
with file_path.open(mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
     # Skip the header row
    next(csv_reader)  
    overhead_data = []
    for row in csv_reader:
        category = row[0]
        expense = float(row[1])
        overhead_data.append((category, expense))
def find_highest_overhead_category():
    """
    Find the highest overhead category and its corresponding expense.
    Args: file_path (Path): The path to the CSV file containing overhead data.
    Returns: tuple: A tuple containing the highest overhead category (str) and its corresponding expense (float).
    """
    # overhead_data = []
    # # Open and read the CSV file
    # with file_path.open(mode="r") as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     # Skip the header row
    #     next(csv_reader)  
    #     for row in csv_reader:
    #         category = row[0]
    #         expense = float(row[1])
    #         overhead_data.append((category, expense))

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
    
# # Path to the CSV file 
# file_path = Path.cwd() / "overheadsfilecsv.csv"

# Find the highest overhead category and expense using the function
highest_category, max_expense = find_highest_overhead_category()

# Write the summary to a text file
with open('summary_report.txt', 'w') as f:
    f.write(f"[HIGHEST OVERHEAD]: {highest_category.upper()}: {max_expense:.2f}%")