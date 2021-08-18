# Importing modules
import tkinter
from tkinter import font
from tkinter.constants import BOTTOM
from tkinter import END 
from tkinter import ANCHOR

# Define window
win = tkinter.Tk()
win.title("To-do List")
win.iconbitmap("checked.ico")
win.geometry("400x600")
win.resizable(0,0)

# Define fonts and colors
gui_font = ("Helvetica", 11)
win_color = "#61B329"
win.config(bg=win_color)

# Define functions 
def add_task():
    listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)

def remove_task():
    listbox.delete(ANCHOR)

def clear_task():
    listbox.delete(0, END)

def save_task():
    with open("to-do.txt", "w") as f:
        tuple_list = listbox.get(0, END)
        for item in tuple_list:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item + "\n")

def open_file():
    try:
        with open("to-do.txt", "r") as f:
            for line in f:
                listbox.insert(END, line)
    except:
        return


# Define Frames
input_frame = tkinter.Frame(win, bg=win_color)
output_frame = tkinter.Frame(win, bg=win_color)
button_frame = tkinter.Frame(win, bg=win_color)
input_frame.pack(padx=3, pady=2)
output_frame.pack(pady=3)
button_frame.pack(pady=4)

# Input frame layout
list_entry = tkinter.Entry(input_frame, width=36, borderwidth=3, font=gui_font)
list_add_button = tkinter.Button(input_frame, text="Add task", borderwidth=2, font=gui_font, command=add_task)
list_entry.grid(row=0, column=0, padx=3, pady=3)
list_add_button.grid(row=0, column=1, padx=3, pady=3)

# Ouput frame layout 
scrollbar = tkinter.Scrollbar(output_frame)
listbox = tkinter.Listbox(output_frame, height=28, width=45, borderwidth=3, font=gui_font, yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1,sticky="NS")
# Link scrollbar to listbox
scrollbar.config(command=listbox.yview)
listbox.grid(row=0, column=0)

# Button Frame layout 
remove_btn = tkinter.Button(button_frame, text="Remove Task", font=gui_font, command=remove_task)
clear_btn = tkinter.Button(button_frame, text="Clear Task", font=gui_font, command=clear_task)
save_btn = tkinter.Button(button_frame, text="Save List", font=gui_font, command=save_task)
quit_btn = tkinter.Button(button_frame, text="Quit", font=gui_font, command=win.destroy)

remove_btn.grid(row=0, column=0)
clear_btn.grid(row=0, column=1)
save_btn.grid(row=0, column=2)
quit_btn.grid(row=0, column=3)

# Open a saved list
open_file()

# Main Loop
win.mainloop()