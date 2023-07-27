# Salesforce metadate to git cheatsheet

## Ngữ cảnh
   
Tôi là 1 developer và mới tham gia vào một số dự án Salesforce. Tôi gặp vấn đề khi code với Salesforce là lưu code mới nhất từ Salesforce server. Đó không phải là thao tác lưu mà là tôi thường bị thiếu metadata khi commit git (có lẽ không phải là vấn đề lớn nếu tôi có nhiều kinh nghiệm + trí nhớ tốt hơn 😂). Vì vậy tôi quyết định tạo cheat sheet này để giúp những người mới như tôi. Rất hoan nghênh và trân trọng những đóng góp của bạn.


## NEW: has a tool 

### Requisition:

Python 3, pip3 and virtualenv

See how to install and create virtualenv at here: [https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

### After clone/download source, then:
```bash
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