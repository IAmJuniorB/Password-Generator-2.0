
from tkinter import *
import string
import secrets
import pyperclip
import random
from tkinter import ttk

root = Tk()

photo = PhotoImage(file=r'C:\Users\joseph.bonfantijr_sc\Desktop\Python\PWGen\Junior.png')
root.iconphoto(False, photo)

root.title('PW Gen - Joe')

root.geometry("500x300")    # x small case here

passstr = StringVar()
passlen = IntVar()
passlen.set(0)
progress = ttk.Progressbar(root, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
progress.pack()

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

copy_button = Button(root, text="Copy to clipboard", command=copytoclipboard, state='disabled')

def validate_password_length(P):
    P = str(passlen.get())
    if not P.isdigit():
        return False
    elif int(P) < 4 or int(P) > 30:
        return False
    else:
        return True

def generate_password():
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


def clear():
    passlen.set(0)
    passstr.set("")

Label(root, text="Password Generator", font="calibri 25 bold").pack()
Label(root, text="Enter password length").pack(pady=3)

validation = (root.register(validate_password_length), '%P')
Entry(root, textvariable=passlen, validate="key", validatecommand=validation).pack(pady=3)

Button(root, text="Generate Password", command=generate_password).pack(pady=7)
Label(root, text="Password Generated").pack(pady=3)
Entry(root, textvariable=passstr).pack(pady=3)


Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()


root.mainloop()

"""
Feel free to commment/critique anything here
Would also love to gain some understanding as to why PhotoImage() does not work for me
Thanks
"""