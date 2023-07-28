# Import pandas library
import pandas as pd

import user_config as config

PACKAGE_XML_FILE = config.PACKAGE_XML_FILE
changed_metadata_file = config.changed_metadata_file
API_VERSION = config.API_VERSION

# Read the changed_metadata_file file into a dataframe
df = pd.read_csv(changed_metadata_file)

# Create an empty list to store the xml elements
xml_list = []
start_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Package xmlns="http://soap.sforce.com/2006/04/metadata">'
end_xml = f'<version>{API_VERSION}</version></Package>'
xml_list.append(start_xml)

# Loop through each row of the dataframe
for index, row in df.iterrows():
    # Get the name and members values from the row
    name = row["metadata_type"]
    members = row["fullName"]

    # Split the members value by comma into a list
    members_list = members.split(",")

    # Create an xml element for the name value
    xml_name = f"<name>{name}</name>"

    # Create an xml element for each member value
    xml_members = ""
    for member in members_list:
        xml_member = f"<members>{member}</members>"
        xml_members += xml_member

    # Combine the xml elements into one string
    xml_string = f"<types>{xml_name}{xml_members}</types>"

    # Append the xml string to the xml list
    xml_list.append(xml_string)

# Append the end of xml format
xml_list.append(end_xml)

# Join the xml list elements by newline into one string
xml_content = "\n".join(xml_list)

# Write the xml content to the package.xml file
with open(PACKAGE_XML_FILE, "w") as f:
    f.write(xml_content)