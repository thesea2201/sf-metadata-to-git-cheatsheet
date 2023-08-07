import os
from dotenv import load_dotenv

load_dotenv()

ORG_USERNAME = os.getenv('ORG_USERNAME')
API_VERSION = os.getenv('API_VERSION') if os.getenv('API_VERSION') else '55.0'
MODIFIED_FILTER_DURATION = os.getenv('MODIFIED_FILTER_DURATION').lower() if os.getenv('MODIFIED_FILTER_DURATION') else 'today' # 'today', 'yesterday', '2023-07-22', '2023-07-22T08'

DATA_BASE_FOLDER = os.getenv('DATA_BASE_FOLDER') if os.getenv('DATA_BASE_FOLDER') else f"data-{ORG_USERNAME}"
METADATA_TYPES_FILE = f"{DATA_BASE_FOLDER}/metadata-types.csv"
IGNORE_CHANGED_METADATA_FILE = f"{DATA_BASE_FOLDER}/ignore_changed_metadata.csv"
CHANGED_METADATA_FILE = f"{DATA_BASE_FOLDER}/changed_metadata.csv"
PACKAGE_XML_FILE = os.getenv('PACKAGE_XML_FILE') if os.getenv('PACKAGE_XML_FILE') else f"{DATA_BASE_FOLDER}/package.xml"

try:
    if not ORG_USERNAME:
        raise ValueError('Please fill the config in .env file.')
except ValueError:
    raise

def create_folders(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            # return a success message
            print(f"Folder {path} created successfully")

def create_files(files):
    for file in files:
        if (os.path.exists(file) == False):
            open(file, "w")

create_folders([DATA_BASE_FOLDER])
create_files([IGNORE_CHANGED_METADATA_FILE])