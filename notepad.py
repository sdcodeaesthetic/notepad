from tkinter import *


class Notepad_Application:
    def __init__(self, master, h, w):
        self.master = master
        master.title("Notepad")
        self.height = h
        self.width = w
        self.notepad_interface()

    def notepad_interface(self):
        self.input_area = Text(self.master, height = self.height, width = self.width)
        self.input_area.pack()
        self.notepad_menu = Menu(self.master)
        self.master.config(menu = self.notepad_menu)
        self.filemenu = Menu(self.notepad_menu) 
        self.notepad_menu.add_cascade(label = 'File', menu = self.filemenu) 
        self.filemenu.add_command(label = 'New') 
        self.filemenu.add_command(label = 'Open...')
        self.filemenu.add_command(label = 'Save')
        self.filemenu.add_command(label = 'Print')
        self.filemenu.add_separator() 
        self.filemenu.add_command(label = 'Exit', command = self.master.quit)
        self.editmenu = Menu(self.notepad_menu)
        self.notepad_menu.add_cascade(label = 'Edit', menu = self.editmenu)
        self.editmenu.add_command(label = 'Undo')
        self.editmenu.add_command(label = 'Redo')
        self.editmenu.add_separator()
        self.editmenu.add_command(label = 'Cut')
        self.editmenu.add_command(label = 'Copy')
        self.editmenu.add_command(label = 'Paste')
        self.editmenu.add_command(label = 'Delete')
        self.formatmenu = Menu(self.notepad_menu)
        self.notepad_menu.add_cascade(label = 'Format', menu = self.formatmenu)
        self.viewmenu = Menu(self.notepad_menu)
        self.notepad_menu.add_cascade(label = 'View', menu = self.viewmenu)
        self.helpmenu = Menu(self.notepad_menu) 
        self.notepad_menu.add_cascade(label = 'Help', menu = self.helpmenu)
        self.helpmenu.add_command(label = 'View Help')
        self.helpmenu.add_command(label = 'About Notepad')
        

root = Tk()
my_notepad = Notepad_Application(root, 70, 150)
root.mainloop()
