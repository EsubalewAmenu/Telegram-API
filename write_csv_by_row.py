import csv

# Define the row number to update
target_row_number = 4  # Replace with the desired row number

# Open the CSV file for reading and writing
with open(r'scraped group/Catalyst Community Reviewers, Moderators, Advisors_updated.csv', 'r') as file_read_obj, \
     open(r'scraped group/Catalyst Community Reviewers, Moderators, Advisors_updated.csv', 'w', newline='') as file_write_obj:

    # Create reader and writer objects
    reader_obj = csv.reader(file_read_obj)
    writer_obj = csv.writer(file_write_obj)

    # Iterate over each row in the CSV file
    for row_number, row in enumerate(reader_obj, 1):
        # Check if it's the target row
        if row_number == target_row_number:
           
            while len(row) < 7:
                row.append('')  # Add empty values for missing columns

            # Update the value in the G column (assuming G is the 7th column, 0-based indexing)
            row[7 - 1] = 'New Value'  # Replace 'New Value' with the desired value

        # Write the updated or unchanged row to the new CSV file
        writer_obj.writerow(row)

print(f'Value in the G column for row {target_row_number} updated successfully.')
