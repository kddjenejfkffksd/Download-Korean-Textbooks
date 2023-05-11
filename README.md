# Download Korean Textbooks

## Unix-like

You need to have Python3, its venv module, and curl installed.

1. Make and open directory to install code and books into (first time only)
```
mkdir "Korean Textbooks"
cd "Korean Textbooks"
```

2. Set Python Virtual  (first time only)

```
venv -m python3 .
```

3. Enter Python Virtual Environment

```
source ./bin/activate
```

4. Install prerequisites (first time only)

```
pip install fpdf
pip install pick
pip install requests
```

5. Download source (first time only)

https://github.com/coughingmouse/Download-Korean-Textbooks/raw/main/download-korean-textbooks.py

```
curl https://github.com/coughingmouse/Download-Korean-Textbooks/raw/main/download-korean-textbooks.py --output download-korean-textbooks.py
```

6. Run to install in the directory to download files


```
python3 download-korean-textbooks.py
```

7. Deactivate venv or close shell (not necessary)

```
deactivate
```
