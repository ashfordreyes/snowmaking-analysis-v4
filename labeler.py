import tkinter as tk
from tkinter import Label, filedialog, Button, Frame, Text, Scrollbar, RIGHT, Y, LEFT, BOTH, TOP, BOTTOM

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.txt*"),
                                                         ("all files",
                                                            "*.*")))
    

    label_file_explorer.configure(text="File Opened: "+filename)

window = tk.Tk()

window.title("Labeler")
window.minsize(400, 300)
window.configure(background="white")
mycolor = '#f2f2f2'  # or use hex if you prefer 
window.configure(bg=mycolor)
textcolor = "#181A18"

######################3

top = Frame(window)
bottom = Frame(window)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

# create the widgets for the top part of the GUI,
# and lay them out
label_file_explorer = Label(window, 
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4, 
                            fg = textcolor)

button_explore = Button(window, 
                        text = "Browse Files",
                        command = browseFiles) 
 
button_exit = Button(window, 
                     text = "Exit",
                     command = exit) 

button_no_snowmaking = Button(window,
                              text = "No Snowmaking",
                              command = lambda: print("No Snowmaking")
                              )

button_snowmaking = Button(window,
                           text = "Snowmaking",
                           command = lambda: print("Snowmaking")
                           )

label_file_explorer.pack(in_=bottom, side=LEFT)
button_explore.pack(in_=bottom, side=LEFT)
button_exit.pack(in_=bottom, side=LEFT)
button_no_snowmaking.pack(in_=bottom, side=LEFT)
button_snowmaking.pack(in_=bottom, side=LEFT)

# create the widgets for the bottom part of the GUI,
# and lay them out
text = Text(window, width=35, height=15)
scrollbar = Scrollbar(window)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(in_=bottom, side=RIGHT, fill=Y)
text.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)

###########################



window.mainloop()