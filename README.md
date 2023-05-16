# Download Korean Textbooks

## Web (requires Google account)

1. Copy [this](https://github.com/coughingmouse/Download-Korean-Textbooks/raw/main/download_korean_textbooks.py) into a cell and run it.

## iPython/Jupyter Notebook

1. Run this.
```
%load https://github.com/coughingmouse/Download-Korean-Textbooks/raw/main/download_korean_textbooks.py
```

## Unix-like

You need to have Python3, its pip and venv module, and curl installed.


1. Download source
```
curl -fsSL https://github.com/coughingmouse/Download-Korean-Textbooks/raw/main/download_korean_textbooks.py --output download_korean_textbooks.py
```

2. Run to initiate
```
python3 download_korean_textbooks.py
```

3. Enter Python virtual environment
```
source 'Korean Textbooks/bin/activate'
```

4. Run 2. again to download files
5. run ```deactivate``` or exit shell to get out of the virtual environment
