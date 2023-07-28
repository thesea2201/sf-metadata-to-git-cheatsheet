import os
from dotenv import load_dotenv

load_dotenv()

ORG_USERNAME = os.getenv('ORG_USERNAME')
API_VERSION = os.getenv('API_VERSION') if os.getenv('API_VERSION') else '55.0'
MODIFIED_FILTER_DURATION = os.getenv('MODIFIED_FILTER_DURATION').lower() if os.getenv('MODIFIED_FILTER_DURATION') else 'today' # 'today', 'yesterday', '2023-07-22', '2023-07-22T08'

data_base_folder = "data"
metadata_types_file = f"{data_base_folder}/metadata-types.csv"
changed_metadata_file = f"{data_base_folder}/changed_metadata.csv"
PACKAGE_XML_FILE = os.getenv('PACKAGE_XML_FILE') if os.getenv('PACKAGE_XML_FILE') else f"{data_base_folder}/package.xml"

try:
    if not ORG_USERNAME:
        raise ValueError('Please fill the config in .env file.')
except ValueError:
    raise

def create_folder(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            # return a success message
            print(f"Folder {path} created successfully")

create_folder([data_base_folder])