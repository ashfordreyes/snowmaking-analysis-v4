from curses import window
import tkinter as tk
from tkinter import Button, Label, filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
     
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

root = tk.Tk()

root.title("Labeler")
root.minsize(400, 300)
root.configure(background="white")
mycolor = '#f2f2f2'  # or use hex if you prefer 
root.configure(bg=mycolor)

# Create a File Explorer label
label_file_explorer = Label(window, 
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4, 
                            fg = "blue")
 
     
button_explore = Button(window, 
                        text = "Browse Files",
                        command = browseFiles) 
 
button_exit = Button(window, 
                     text = "Exit",
                     command = exit) 
 
# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
 
button_explore.grid(column = 1, row = 2)
 
button_exit.grid(column = 1,row = 3)

root.mainloop()