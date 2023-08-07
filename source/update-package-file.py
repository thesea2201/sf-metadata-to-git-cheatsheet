import pandas as pd

import user_config as config

PACKAGE_XML_FILE = config.PACKAGE_XML_FILE
CHANGED_METADATA_FILE = config.CHANGED_METADATA_FILE
IGNORE_CHANGED_METADATA_FILE = config.IGNORE_CHANGED_METADATA_FILE
API_VERSION = config.API_VERSION

# Load the CSV files into DataFrames
try:
    df1 = pd.read_csv(CHANGED_METADATA_FILE)
except pd.errors.EmptyDataError:
    exit(0)

try:
    df2 = pd.read_csv(IGNORE_CHANGED_METADATA_FILE)
except pd.errors.EmptyDataError:
    df2 = pd.DataFrame()

if df2.empty:
    diff_df = df1
else:
    # Find the differences between the two DataFrames
    diff_df = pd.concat([df1, df2]).drop_duplicates(keep=False)

# Group the differences by 'metadata_type'
grouped_diff = diff_df.groupby('metadata_type')['fullName'].apply(list).reset_index()

def format_to_xml(row):
    members = ''.join(f"<members>{member}</members> " for member in row['fullName'])
    metdata_name = row['metadata_type']
    return f"<types>{members}<name>{metdata_name}</name></types>"

if grouped_diff.empty:
    print('No differences found')
    exit(0)
else:
    # Apply the XML-like formatting to each row and wrap all content in 'xml_format'
    end_line = "\n"
    grouped_diff['xml_format'] = grouped_diff.apply(format_to_xml, axis=1)
    result_xml = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Package xmlns="http://soap.sforce.com/2006/04/metadata">{end_line}{end_line.join(grouped_diff["xml_format"])}{end_line}<version>{API_VERSION}</version>{end_line}</Package>'

    # Save the results to a new file
    with open(PACKAGE_XML_FILE, 'w', encoding='utf-8') as file:
        file.write(result_xml)
