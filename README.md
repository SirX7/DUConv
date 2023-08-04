# DUConv  

**A Python3 Module that helps convert digital data units such as Bytes, KB, MB, GB, and TB.**  
**This module can be run from the cli to help make fast data conversion**.  

#  Installation  
### Install with pip:  
To use as a module or a cli application you can create a virtual environment and install  
DUConv via pip (Not recommended to be install systemwide).  

`pip install duconv`  

### Install with pipx:  
If the intended use is only as a cli application, run:  

`pipx install duconv`  

# Usage  
### As a Module  

```python
from duconv import bytesconvert  
from duconv import convert  

bytesconvert.bytes_converter(b)  
bytesconvert.data_to_bytes(d, un)  

convert.to_kb(d, un)  
convert.to_mb(d, un)  
convert.to_gb(d, un)  
convert.to_tb(d, un)  

b:  an integer or a float  
d:  an integer or a float  
un: a string of one character representing a data unit  

```

### As a cli Application
From the cli run:
`duconv -b VAL`  

`duconv -d VAL [k|m|g|t]`  

`duconv [-kmgt] VAL [k|m|g|t]`  



```bash
duconv -b 5000  

duconv -d 5000 k  

duconv -m 5000 k  

```

# License  
This project is licensed under the terms of the MIT license.  