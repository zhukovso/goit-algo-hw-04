pip install virtualenv
python -m venv .task3
call .\.task3\Scripts\activate
pip install -r requirements.txt
python.exe task_3.py .\TEMP
call deactivate
rmdir /s .\.task3\ 
rem start rm -Recurse -Force .\.task3\ 
