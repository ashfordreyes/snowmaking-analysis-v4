import tkinter as tk
from tkinter import Label, filedialog, Button

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.txt*"),
                                                         ("all files",
                                                            "*.*")))
    

    label_file_explorer.configure(text="File Opened: "+filename)

root = tk.Tk()

root.title("Labeler")
root.minsize(400, 300)
root.configure(background="white")
mycolor = '#f2f2f2'  # or use hex if you prefer 
root.configure(bg=mycolor)
textcolor = "#181A18"

label_file_explorer = Label(root, 
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4, 
                            fg = textcolor)

button_explore = Button(root, 
                        text = "Browse Files",
                        command = browseFiles) 
 
button_exit = Button(root, 
                     text = "Exit",
                     command = exit) 

label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1,row = 3)

root.mainloop()