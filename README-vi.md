# Salesforce metadate to git cheatsheet

## Ngữ cảnh
   
Tôi là 1 developer và mới tham gia vào một số dự án Salesforce. Tôi gặp vấn đề khi code với Salesforce là lưu code mới nhất từ Salesforce server. Đó không phải là thao tác lưu mà là tôi thường bị thiếu metadata khi commit git (có lẽ không phải là vấn đề lớn nếu tôi có nhiều kinh nghiệm + trí nhớ tốt hơn 😂). Vì vậy tôi quyết định tạo cheat sheet này để giúp những người mới như tôi. Rất hoan nghênh và trân trọng những đóng góp của bạn.


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

### Copy .env file
```bash
cp .env.example .env
```

### Complete setting in `.env` file
```bash
ORG_USERNAME="<your_org_username>" # using command "sfdx org list" to see list of org username
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

Result will be stored in [source\data\metadata-types.csv](source\data\metadata-types.csv) file

### Get all changed metadata
```bash
python3 get-changed-metadata.py
```


### Update your package.xml file
```bash
python3 update-package-file.py
```


## Cách sử dụng

Chúng ta có một số kiểu

### Must
Nếu bạn sửa những phần này thì phải retrieve những metadata dưới đây từ SF org của bạn.

### Should
Tuỳ thuộc vào dự án của bạn, có lẽ metadata này không cần retrieve. Nhưng chúng tôi vẫn khuyến khích là nên retrieve nó về và lưu vào repo.

### Optional
Có thể metadata này không yêu cầu nhưng có thể bạn sẽ cần retrieve, tuỳ thuộc và code của bạn có chỉnh sửa nó hay không, cứ check lại nhé, không thừa đâu.

##  