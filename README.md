# PyPAD Docs

PyPAD Docs is a free to use text editor that is open source. With many features and more to come in future updates.

Only PyPAD Docs name is copyright. 

# Version 3.0---Features

New features includ: changing all color of text, changing color of selected text, changing color of the background (page color): Warning these colors will not be saved.  The ability to make text BOLD or Italic. undo and redo butons in the tools bar which is just below the File, Edit Visuals, Help, bar. Visuals  allows the user to change all text color and background color. 

There is aslo a right click function in the program. You can undo, redo, cut, copy, paste. Save and exit! When you save or save as. A little pop up screen will also appear. saying "your file saved!". If you all do not like this features I can remove it in the next update. 



I have added a .txt2.pdf converter to PyPAD
You can now take screenshots with it 


# Downloading On RPI-4 (Rasberry Pi 4)

getting required Modules
This will automatically install the following:

1. Pillow 

2. pyautogui

3. fpdf

4. pyinstaller
```
pip3 install -U requirments.txt
```
Open Desktop in terminal
```
cd /home/pi/Desktop
```
Clone into the PyPAD Docs repository
```
git clone https://github.com/blaze005/PyPAD-Docs.git
```
Going into the file "PyPAD Docs" located on the desktop. Using the terminal
```
cd /home/pi/Desktop/PyPAD-Docs
```
Turn into EXE pyinstaller required (This is optional) 
```
python3 setup.py
```
After setup.py is finished go into the "dist" folder and run PyPAD_Docs or copy and paste it to 
your desktop



# Download on Windows

Click on the green button to download the .zip extract it in the desktop.

Open CMD

If you do not have pyinstaller do this other wise skip ```pip install pyinstaller```

```
cd C:\Users\User\Desktop\PyPAD-Docs-main\PyPAD-Docs-main
```
```
python setup.py
```
Open the "dist" folder to run PyPAD_Docs or copy it to your desktop for easy use!!
