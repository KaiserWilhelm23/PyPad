import os


os.system("pip install pyinstaller")
print('Setting Up EXE')
os.system('pyinstaller --onefile --windowed --icon=text.ico PyPAD_Docs.py')
print('Complete')
