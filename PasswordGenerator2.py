
from tkinter import *
import string
import secrets

# use to copy our generated pw to clipboard
import pyperclip

# for generating random pw
import random

from tkinter import ttk

# initializing tkinter
root = Tk()

# Set icon photo
photo = PhotoImage(file=r'C:\Users\joseph.bonfantijr_sc\Desktop\Python\PWGen\Junior.png')
root.iconphoto(False, photo)

# set title
root.title('PW Gen - Joe')

# setting the width and height of the gui
root.geometry("500x300")    # x small case here

# declaring variable of str type. Variable will be used to store pw generated
passstr = StringVar()

# declaring variable of int type which will be used to store length of pw entered by user
passlen = IntVar()

# setting the length of pw to zero
passlen.set(0)

# progress bar for executing pw
progress = ttk.Progressbar(root, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
progress.pack()

# function to copy password to clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# disable copy button until pw generated
copy_button = Button(root, text="Copy to clipboard", command=copytoclipboard, state='disabled')

# validate pw is correct length
def validate_password_length(P):
    P = str(passlen.get())
    if not P.isdigit():
        return False
    elif int(P) < 4 or int(P) > 30:
        return False
    else:
        return True

# function to generate password
def generate():
    if not validate_password_length(passlen.get()):
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    progress["value"] = 0
    progress["maximum"] = passlen.get()
    for i in range(passlen.get()):
        password += secrets.choice(characters)
        progress["value"] += 1
        progress.update()
    passstr.set(password)
    copy_button.config(state='normal')


# function to clear fields
def clear():
    passlen.set(0)
    passstr.set("")

# Creating text label widget
Label(root, text="Password Generator", font="calibri 25 bold").pack()

# Creating text label widget
Label(root, text="Enter password length").pack(pady=3)

validation = (root.register(validate_password_length), '%P')
Entry(root, textvariable=passlen, validate="key", validatecommand=validation).pack(pady=3)

# button to call generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# Creating text label widget
Label(root, text="Password Generated").pack(pady=3)

# entry widget to show generated pw
Entry(root, textvariable=passstr).pack(pady=3)

# button to call copytoclipboard function
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

# Create a clear button and add it to the UI
clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()

# mainloop() - infinite loop to run application when in ready state 
root.mainloop()

"""
Feel free to commment/critique anything here
Would also love to gain some understanding as to why PhotoImage() does not work for me
Thanks
"""