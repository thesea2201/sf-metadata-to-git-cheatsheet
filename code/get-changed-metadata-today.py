# # Import the subprocess, csv, json and datetime modules
# import subprocess
# import csv
# import json
# import datetime

# org_username = "bien-org"
# metadata_types_file = "metadata-types.csv"
# output_file = "./data/metadata-types.csv"

# # Read the metadata types from the csv file and store them in a list
# metadata_types = []
# with open(metadata_types_file, "r") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         metadata_types.append(row[0]) # Assume the metadata type is in the first column

# # Create a list to store the full names of the metadata
# full_names = []

# # Get the current date as a string in YYYY-MM-DD format
# today = datetime.date.today().strftime("%Y-%m-%d")

# # Loop through the metadata types and execute the sfdx command for each one
# for metadata_type in metadata_types:
#     # Define the sfdx command to get the metadata with last modified date as today
#     sfdx_command = f"sfdx force:mdapi:listmetadata -o {org_username} -m {metadata_type} --json"

#     # Execute the command and capture the output as a JSON object
#     output = subprocess.check_output(sfdx_command, shell=True)
#     output_json = json.loads(output)

#     # Loop through the output and append the full names to the list if the last modified date is today
#     for item in output_json["result"]:
#         if item["lastModifiedDate"].startswith(today): # Check if the date matches
#             full_names.append(item["fullName"])

# # Create a csv file and write the full names to it
# with open(output_file, "w") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Full Name"]) # Write the header row
#     for name in full_names:
#         writer.writerow([name]) # Write each full name as a row
#     print('Done!')


# Import the modules
import subprocess
import csv
import datetime
import json
from tqdm import tqdm

import user_config as config

org_username = config.org_username
metadata_types_file = config.metadata_types_file
changed_metadata_file = config.changed_metadata_file



# Open the metadata_types_file file for reading
with open(metadata_types_file, "r") as f:
    # Create a csv reader object
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    # Loop through each row
    for row in tqdm(reader):
        # Get the metadata type from the first column
        metadata_type = row[0]

        # Define the command to execute sfdx for each metadata type
        command = f"sfdx force:mdapi:listmetadata -u {org_username} -m {metadata_type} -a 52.0 --json"
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True)
        # Parse the output as json
        output_json = json.loads(output)
        # Check if the output has any result
        if output_json["result"]:
            # Open the changed_metadata_file file for rewrite
            with open(changed_metadata_file, "a") as f:
                # Create a csv writer object
                writer = csv.writer(f)
                # Write the header row if the file is empty
                if f.tell() == 0:
                    writer.writerow(["metadata_type", "fullName"])
                # Loop through each result
                for result in output_json["result"]:
                    # Get the fullName and lastModifiedDate from the result
                    fullName = result["fullName"]
                    lastModifiedDate = result["lastModifiedDate"]
                    # Convert the lastModifiedDate to a datetime object
                    lastModifiedDate = datetime.datetime.strptime(lastModifiedDate, "%Y-%m-%dT%H:%M:%S.%fZ")
                    # Get today's date as a datetime object
                    today = datetime.datetime.now().date()
                    # Check if the lastModifiedDate is today
                    if lastModifiedDate.date() == today:
                        # Write the metadata type and fullName to the csv file
                        writer.writerow([metadata_type, fullName])
    
    print("Done!")
