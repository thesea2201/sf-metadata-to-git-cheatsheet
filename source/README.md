## Get modified metadata from the specified time 

### Requisition:

Python 3, pip3 and virtualenv
<details>
<summary>
Installation (click to expand)
</summary>

#### Install python 3:
Unix/macOS included python3, check it by command `python3 --version`

Windows: access [https://www.python.org/downloads/](https://www.python.org/downloads/) or install directly from Microsoft Store

#### Install virtual environment
```bash
python3 -m pip install --user virtualenv
```
</details>

### Clone source:
```bash
git clone https://github.com/thesea2201/sf-metadata-to-git-cheatsheet.git
cd sf-metadata-to-git-cheatsheet/source
```

### Create a virtual environment
```bash
python3 -m venv venv
```

### Activating a virtual environment:
```bash
source env/bin/activate # Unix/Macos
.\env\Scripts\activate # Windows
```

### Install required library
```bash
pip install -r requirements.txt
```

### Copy .env file
```bash
cp .env.example .env
```

### Complete setting in `.env` file
```bash
ORG_USERNAME="<your_org_username>" # using command "sfdx org list" to see list of org username
DATA_BASE_FOLDER="" # (optional) default: "data-<your_org_username>"
API_VERSION='55.0' # (Default(55.0)) Depend on your project
MODIFIED_FILTER_DURATION='today'
# (Default 'today') 'today', 'yesterday', '2023-07-22', '2023-07-22T08'
# get all metadata has lastModifiedDate since modified_filter_duration, Todo: 
PACKAGE_XML_FILE="<package.xml_file_path>" 
# (Default ./data/package.xml) can direct to your project manifest/package.xml, 
# it will override your file
```

### Get all metadata types from org
```bash
python3 get-all-metadata-types.py
```
Result will be stored in `source/<DATA_BASE_FOLDER>/metadata-types.csv` file

### Get all changed metadata
```bash
python3 get-changed-metadata.py
```
Result will be stored in `source/<DATA_BASE_FOLDER>/changed_metadata.csv` file

(Optional) If you want to ignore some metadata, just add them into `source\<DATA_BASE_FOLDER>\ignore_changed_metadata.csv` file like this:

```
metadata_type,fullName
Profile,StandardAul
Profile,ServiceCloud
Profile,Standard
```

### Update your package.xml file
```bash
python3 update-package-file.py
```
Result will be stored in `source/<DATA_BASE_FOLDER>/package.xml` file
