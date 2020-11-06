from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser
from fpdf import FPDF
from PIL import Image
from tkinter import messagebox
from tkinter import ttk
import pyautogui
import time
import os

root = Tk()

root.title("PyPAD")
root.geometry('500x500')

# Creating a photoimage object to use image 
file = PhotoImage(file =r"") 
edit = PhotoImage(file = r"")
color = PhotoImage(file = r"")
help = PhotoImage(file = r"") 
# Resizing image to fit on button 
photoimage1 = file.subsample(40, 40)
photoimage2 = edit.subsample(15, 15)
photoimage3 = color.subsample(70, 70)
photoimage4 = help.subsample(40, 40)



global open_status_name
open_status_name = False

global selected
selected = False 

# Creat new file
def new_file():
    my_text.delete('1.0',END)
    root.title('New Pad - PyPAD')

    global open_status_name
    open_status_name = False

#open file
def open_file():
    #delete previouse text
    my_text.delete('1.0',END)

    text_file = filedialog.askopenfilename(title='Open File')

    if text_file:
        #check if file name
        global open_status_name
        open_status_name =  text_file
        
    
    root.title(f'{text_file} - PyPAD')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

#save file as
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*',title='Save As')

    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))
    text_file.close()

#save file
def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        #pop up box
        messagebox.showinfo('Saved', 'Your File Has Saved')

    else:
        save_as_file()
        messagebox.showinfo('Saved', 'Your File Has Saved')
        
        
#cut text
def cut_text(e):
    global selected

    if my_text.selection_get():
        # Grab selected text from text box
        selected = my_text.selection_get()
        #delete selected text from text box
        my_text.delete('sel.first','sel.last')
            
        

#copy text
def copy_text(e):
    global selected 
    if my_text.selection_get():
        # Grab selected text from text box
        selected = my_text.selection_get()

#paste text
def paste_text(e):
   
   if selected:
        position = my_text.index(INSERT)
        my_text.insert(position, selected)

#bold
def bold_it():
    bold_font = font.Font(my_text, my_text.cget('font'))
    bold_font.configure(weight='bold')

    current_tags= my_text.tag_names('sel.first')


    #config tag
    my_text.tag_configure('bold',font=bold_font)

    if 'bold' in current_tags:
        my_text.tag_remove('bold', 'sel.first','sel.last')
    else:
        my_text.tag_add('bold','sel.first','sel.last' )


#italics
def italics_it():
    italic_font = font.Font(my_text, my_text.cget('font'))
    italic_font.configure(slant='italic')

    current_tags= my_text.tag_names('sel.first')


    #config tag
    my_text.tag_configure('italic',font=italic_font)

    if 'italic' in current_tags:
        my_text.tag_remove('italic', 'sel.first','sel.last')
    else:
        my_text.tag_add('italic','sel.first','sel.last' )


def text_color():
    #colors
    my_color = colorchooser.askcolor()[1]
    if my_color:
        color_font = font.Font(my_text, my_text.cget('font'))
        current_tags= my_text.tag_names('sel.first')


        #config tag
        my_text.tag_configure('colored',font=color_font, foreground=my_color)

        if 'colored' in current_tags:
            my_text.tag_remove('colored', 'sel.first','sel.last')
        else:
            my_text.tag_add('colored','sel.first','sel.last' )
    
def bg_color():
     my_color = colorchooser.askcolor()[1]
     if my_color:
         my_text.config(bg=my_color)

def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
         my_text.config(fg=my_color)

def help():
    pop = Toplevel(root)
    pop.title('INFO')
    pop.geometry('350x200')
    pop_label = Label(pop, text='''
PyPAD Version 2.0 Full Realse:
PyPAD Name is Copyright PyPAD is OpenSource
-------------------------------------------
PyPAD Creator: Will Payne AKA NEO
-------------------------------------------
System Requirements:
200 MB of storage
40 MB RAM''').pack()
    ok = Button(pop, text='Thanks',command=pop.destroy).pack()

def convert_file():
    pop = Toplevel(root)
    pop.title('Convert')
    pop.geometry('250x200')
    def converttxt2pdf():
        pdf = FPDF()
        pdf.add_page()  
        pdf.set_font("Arial", size = 15)
        text_file = filedialog.askopenfilename(title='Get File To Convert')
        f = open(text_file ,"r")
        for x in f:
            pdf.cell(50,5, txt = x, ln = 1, align = 'C')


        text_file = filedialog.asksaveasfilename(defaultextension='.*',title='Save As')

        messagebox.showinfo('Saved as PDF','Your File Has Saveed')
    
        pdf.output(text_file)
    convert = Button(pop, text='Convert .txt to .pdf', command=converttxt2pdf).pack()
    Quit = Button(pop, text='Quit', command=pop.destroy).place(x=109,y=150)


def web():
    import webbrowser
    webbrowser.open('www.google.com')



def pic_view():
   
    pic_file = filedialog.askopenfilename(title='Open File')
    img = Image.open(pic_file)
    #Get basic details about the image
    print(img.format)
    print(img.mode)
    print(img.size)
    #show the image
    img.show()

def exit():
    root.destroy()


def screen():
    import time
    time.sleep(1)

    screenshot = pyautogui.screenshot()

    screenshot_file = filedialog.asksaveasfilename(defaultextension='.*',title='Save Screen Shot As .png')
    screenshot.save(screenshot_file)

def update():
    print(os.system('pip3 install fpdf'))
    print(os.system('pip3 install pillow'))
    print(os.system('pip3 install pyautogui'))
    print(os.system('pip install fpdf'))
    print(os.system('pip install pillow'))
    print(os.system('pip install pyautogui'))
    pop = Toplevel(root)
    pop.title('Complete')
    pop.geometry('250x200')
    l = Label(pop, text='Update Finished').pack()

    

# create a tool bar frame
toolbar_fram = Frame(root)
toolbar_fram.pack(fill=X)


# create main fram
my_frame = Frame(root)
my_frame.pack(pady=2)

# scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


# Text box
my_text = Text(my_frame,width=200, height=50, font=('Helvetica',11),selectbackground="light blue", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# config scrollbar
text_scroll.config(command=my_text.yview)

#Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()

file_menu.add_command(label='Convert',command=convert_file)
file_menu.add_command(label='View A Picture',command=pic_view)

file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy, accelerator="Ctrl+Q")
file_menu.add_separator()
file_menu.add_command(label="Update",command=update)


#add edit menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Edit',menu=edit_menu )
edit_menu.add_command(label="Cut",command=lambda: cut_text(False))
edit_menu.add_command(label="Copy",command=lambda: copy_text(False))
edit_menu.add_command(label="Paste",command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo,accelerator='(Ctrl+z)')
edit_menu.add_command(label="Redo",command=my_text.edit_redo, accelerator='(Ctrl+y)')

#add color menu
colors_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Visuals',menu=colors_menu )
colors_menu.add_command(label="Change Selected Text Color",command=text_color )
colors_menu.add_command(label="Change All Text Color",command=all_text_color)
colors_menu.add_command(label="Background Color",command=bg_color)
colors_menu.add_separator()

colors_menu.add_command(label="BOLD",command=bold_it, font="Bold 10")
colors_menu.add_command(label="Italics",command=italics_it)
 #add help menu
help_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label="help",command=help )



# status Bar to Bottom Of app
#status_bar = Label(root, text='Ready  ',my_menu,anchor=E,)
#status_bar.pack(ipady=10)

#edit bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)
root.bind('<Control-Key-Q>',exit)


#buttons
undo_button = Button(toolbar_fram, text='<--',command=my_text.edit_undo)
undo_button.grid(row=0, column=0,)

redo_button = Button(toolbar_fram, text='-->',command=my_text.edit_redo)
redo_button.grid(row=0, column=1,)

redo_button = Button(toolbar_fram, text='Search The Web',command=web)
redo_button.grid(row=0, column=2,)



#color button

m = Menu(root, tearoff = False)
m.add_command(label ="Undo",command=my_text.edit_undo) 
m.add_command(label ="Redo",command=my_text.edit_redo)

m.add_separator() 
m.add_command(label ="Cut",command=lambda: cut_text(False)) 
m.add_command(label ="Copy",command=lambda: copy_text(False)) 
m.add_command(label ="Paste",command=lambda: paste_text(False)) 
m.add_separator() 
m.add_command(label ="Text Color",command=text_color)
m.add_separator() 

m.add_command(label ="Take Screen Shot",command=screen)

m.add_separator() 
m.add_command(label ="Save",command=save_file) 
m.add_command(label ="Exit",command=root.destroy)

def do_popup(event):
        m.tk_popup(event.x_root, event.y_root) 

root.bind("<Button-3>", do_popup) 


root.mainloop()


