from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import webbrowser
import os


class Notepad_Application:
    def __init__(self, master, h, w):
        self.master = master
        master.title("Notepad")
        self.height = h
        self.width = w
        self.__file = None
        self.notepad_interface()

    def notepad_interface(self):
        self.input_area = Text(self.master, height = self.height, width = self.width)
        self.input_area.pack()
        self.notepad_menu = Menu(self.master)
        self.master.config(menu = self.notepad_menu)
        self.filemenu = Menu(self.notepad_menu) 
        self.notepad_menu.add_cascade(label = 'File', menu = self.filemenu) 
        self.filemenu.add_command(label = 'New', command = self.new_file) 
        self.filemenu.add_command(label = 'Open...', command = self.open_file)
        self.filemenu.add_command(label = 'Save', command = self.save_file)
        self.filemenu.add_command(label = 'Print')
        self.filemenu.add_separator() 
        self.filemenu.add_command(label = 'Exit', command = self.master.quit)
        self.editmenu = Menu(self.notepad_menu)
        self.notepad_menu.add_cascade(label = 'Edit', menu = self.editmenu)
        self.editmenu.add_command(label = 'Cut', command = self.cut_from_file)
        self.editmenu.add_command(label = 'Copy', command = self.copy_from_file)
        self.editmenu.add_command(label = 'Paste', command = self.paste_to_file)
        self.editmenu.add_command(label = 'Delete')
        self.formatmenu = Menu(self.notepad_menu)
        self.notepad_menu.add_cascade(label = 'Format', menu = self.formatmenu)
        self.viewmenu = Menu(self.notepad_menu)
        self.notepad_menu.add_cascade(label = 'View', menu = self.viewmenu)
        self.helpmenu = Menu(self.notepad_menu) 
        self.notepad_menu.add_cascade(label = 'Help', menu = self.helpmenu)
        self.helpmenu.add_command(label = 'View Help', command = self.view_help)
        self.helpmenu.add_command(label = 'About Notepad', command = self.about_notepad)

    def new_file(self):
        self.master.title("Untitled - Notepad") 
        self.__file = None
        self.input_area.delete(1.0,END)

    def open_file(self):
        self.__file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")]) 
        if self.__file == "":
            self.__file = None
        else:  
            self.master.title(os.path.basename(self.__file) + " - Notepad") 
            self.input_area.delete(1.0,END) 
            file = open(self.__file, "r") 
            self.input_area.insert(1.0, file.read()) 
            file.close()

    def save_file(self):
        if self.__file == None: 
            self.__file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])  
            if self.__file == "": 
                self.__file = None
            else:
                file = open(self.__file, "w") 
                file.write(self.input_area.get(1.0,END)) 
                file.close() 
                self.master.title(os.path.basename(self.__file) + " - Notepad")
        else: 
            file = open(self.__file, "w") 
            file.write(self.input_area.get(1.0,END)) 
            file.close()

    def cut_from_file(self):
        self.input_area.event_generate("<<Cut>>")
        return

    def copy_from_file(self):
        self.input_area.event_generate("<<Copy>>")
        return

    def paste_to_file(self):
        self.input_area.event_generate("<<Paste>>")
        return

    def view_help(self):
        webbrowser.open("https://www.google.com/search?client=ubuntu&channel=fs&q=notepad+help&ie=utf-8&oe=utf-8")
        return

    def about_notepad(self):
        showinfo("Notepad", "Created By Swarnadip Pramanik") 
        return


root = Tk()
my_notepad = Notepad_Application(root, 70, 150)
root.mainloop()
