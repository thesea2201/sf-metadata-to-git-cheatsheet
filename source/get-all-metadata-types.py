# Import the modules
import subprocess
import csv
import json

import user_config as config

ORG_USERNAME = config.ORG_USERNAME

metadata_types_file = config.metadata_types_file

# Define the command to execute sfdx
command = f"sfdx force:mdapi:describemetadata -u {ORG_USERNAME} -a 52.0 --json"

# Run the command and capture the output
output = subprocess.check_output(command, shell=True)

# Parse the output as json
output_json = json.loads(output)
with open(metadata_types_file, "w", newline='') as f:
    # Create a csv writer object
    writer = csv.writer(f)
    writer.writerow(['xmlName'])

    for result in output_json["result"]["metadataObjects"]:
        # Get the xmlName from the result
        xmlName = result["xmlName"]
        writer.writerow([xmlName])