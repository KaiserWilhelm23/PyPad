import os


os.system("pip3 install -r requirements.txt")
os.system("pip install -r requirements.txt")

print('Setting Up EXE')
os.system('pyinstaller --onefile --windowed --icon=text.ico PyPAD_Docs.py')
print('Complete')
