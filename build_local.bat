@echo off
echo Building PassGuard Locally...
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile --name pass passguard/app.py
echo Build Complete. Check the 'dist' folder.
pause