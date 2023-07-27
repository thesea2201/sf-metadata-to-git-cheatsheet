# Salesforce metadate to git cheatsheet

## Context
   
I a new Salesforce developer. I started to work with the Salesforce project and using git I am a developer and join in new projects in Salesforce. I have a problem when coding with Salesforce is saving the latest code from Salesforce server. It's not a save operation, but I often miss metadata when committing git (maybe not a big problem if I have more experience + better memory 😂). So I decided to create this cheat sheet to help newcomers like me. Very welcome and appreciate your contributions.


## NEW: has a tool 

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

### Complete setting in `user_config.py` file
```
org_username = "<your_org_username>" # using command "sfdx org list" to see list of org username
api_version = '55.0' # Depend on your project
modified_filter_duration = 'today' # 'today', 'yesterday', '2023-07-22', '2023-07-22T08'
# get all metadata has lastModifiedDate since modified_filter_duration, Todo: 
package_xml_file = f"{data_base_folder}/package.xml" # can direct to your project manifest/package.xml, it will override your file
```

### Get all metadata types from org
```bash
python3 get-all-metadata-types.py
```
Result will be stored in [source/data/metadata-types.csv](sourcedatametadata-types.csv) file(Unix/macOS) or [source\data\metadata-types.csv](source\data\metadata-types.csv) file(Windows)

### Get all changed metadata
```bash
python3 get-changed-metadata.py
```

### Update your package.xml file
```bash
python3 update-package-file.py
```




## How to use this cheatsheet

We have some type:

### Must
If you edit this section, you must to retrieve the following metadata from the Salesforce organization.

### Should
Maybe this metadata is required, we prefer to retrieve and save it in the repository. It depends on your project.

### Optional
This metadata is not required, but should be included in the git repository. Just take a look!

## Go to the file
[Cheat Sheet](Cheat-Sheet.md)

## In coming features.
Vscode/chrome extension will be added. If you know any extensions like this, please let me know.