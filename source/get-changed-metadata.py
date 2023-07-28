# Import the modules
import subprocess
import csv
import datetime
import json
from tqdm import tqdm

import user_config as config

ORG_USERNAME = config.ORG_USERNAME
metadata_types_file = config.metadata_types_file
changed_metadata_file = config.changed_metadata_file
MODIFIED_FILTER_DURATION = config.MODIFIED_FILTER_DURATION

today = datetime.datetime.now().date()

def get_date(input):
    print(input)
    # check if input is a valid date string
    try:
        return datetime.datetime.strptime(input, "%Y-%m-%d")
    except ValueError:
        # check if input is a valid date and hour string
        try:
            return datetime.datetime.strptime(input, "%Y-%m-%dT%H")
        except ValueError:
            # return an error message if input is invalid
            return "Invalid input. Please enter a date in YYYY-MM-DD or YYYY-MM-DDTHH format."
                    

def get_date_from_type():
    # Causes match/case was introduced in 3.10 version, so comebacks to the old-school
    if MODIFIED_FILTER_DURATION == "today":
        filtered_date = today
    elif MODIFIED_FILTER_DURATION == "yesterday":
        filtered_date = today - datetime.timedelta (days=1)
    else:
        filtered_date = get_date(MODIFIED_FILTER_DURATION)

    # match MODIFIED_FILTER_DURATION:
    #     case "today":
    #         filtered_date = today
    #     case "yesterday":
    #         filtered_date = today - datetime.timedelta (days=1)
    #     case default:
    #         filtered_date = get_date(MODIFIED_FILTER_DURATION)

    return filtered_date.strftime("%Y-%m-%dT%H")
 
filtered_date = get_date_from_type()

print(filtered_date)

with open(changed_metadata_file, "w", newline='') as f:
    # Create a csv writer object
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(["metadata_type", "fullName"])

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
        command = f"sfdx force:mdapi:listmetadata -u {ORG_USERNAME} -m {metadata_type} -a 52.0 --json"
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True)
        # Parse the output as json
        output_json = json.loads(output)
        # Check if the output has any result
        if output_json["result"]:
            # Open the changed_metadata_file file for rewrite
            with open(changed_metadata_file, "a", newline='') as f:
                # Create a csv writer object
                writer = csv.writer(f)
                # Loop through each result
                for result in output_json["result"]:
                    # Get the fullName and lastModifiedDate from the result
                    fullName = result["fullName"]
                    lastModifiedDate = result["lastModifiedDate"]
                    
                    # Check if the lastModifiedDate greater than filtered_date
                    if lastModifiedDate >= filtered_date:
                        # Write the metadata type and fullName to the csv file
                        writer.writerow([metadata_type, fullName])
    
    print("Done!")
