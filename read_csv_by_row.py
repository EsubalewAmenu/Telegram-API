import csv
from send_message import send_message

# Open file  
with open(r'scraped group/Catalyst Community Reviewers, Moderators, Advisors (copy).csv') as file_obj: 
      
    # Create reader object by passing the file  
    # object to reader method 
    reader_obj = csv.reader(file_obj) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row_number, row in enumerate(reader_obj, 1):
        # print(f"Row {row_number}: {row}")

        # Print A and B column data
        if len(row) >= 5:
            # print(f"Row {row_number}: A: {row[0]}, B: {row[1]}, B: {row[3]}")
            send_message(row_number, row[1], row[3])


print('All rows parsed successfully.')