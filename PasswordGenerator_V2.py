from tkinter import *
from tkinter import ttk, messagebox
import string
import secrets
import pyperclip
import sqlite3

# Initialize the main application window
root = Tk()
root.title('PW Gen - Joe')
root.geometry("500x400")

# Load the application icon
try:
    photo = PhotoImage(file=r'C:\Users\jbonfanti\Documents\Python\Fixed\Password-Generator-2.0-main\Junior.png')
    root.iconphoto(False, photo)
except Exception as e:
    print(f"Error loading image: {e}")

# Variables for password generation
passstr = StringVar()
passlen = IntVar()

# Create progress bar and save button
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
progress.pack(pady=10)

copy_button = Button(root, text="Copy to clipboard", command=lambda: copytoclipboard(), state='disabled')
copy_button.pack(pady=3)

save_button = Button(root, text="Save to Database", command=lambda: save_password(passstr.get()), state='disabled')
save_button.pack(pady=3)

def copytoclipboard():
    """Copy the generated password to clipboard."""
    random_password = passstr.get()
    if random_password:
        pyperclip.copy(random_password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

def validate_password_length(P):
    """Validate the password length input."""
    if P.isdigit():
        length = int(P)
        return 4 <= length <= 30
    return False

def generate_password():
    """Generate a secure password based on user-defined length."""
    if not validate_password_length(str(passlen.get())):
        messagebox.showerror("Error", "Please enter a valid length (4-30).")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    progress["value"] = 0
    progress["maximum"] = passlen.get()

    for _ in range(passlen.get()):
        password += secrets.choice(characters)
        progress["value"] += 1
        progress.update()

    passstr.set(password)
    copy_button.config(state='normal')  # Enable the copy button
    save_button.config(state='normal')   # Enable the save button

def clear():
    """Clear the generated password and reset the input."""
    passlen.set(0)
    passstr.set("")
    copy_button.config(state='disabled')
    save_button.config(state='disabled')  # Also disable the save button
    progress["value"] = 0

def save_password(password):
    """Save the generated password to the SQLite database."""
    if not password:
        messagebox.showwarning("Warning", "No password to save.")
        return

    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL
        )
    ''')
    # Insert the password into the table
    cursor.execute('INSERT INTO passwords (password) VALUES (?)', (password,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Saved", "Password saved to database!")

# Create the application interface
Label(root, text="Password Generator", font="calibri 25 bold").pack(pady=10)
Label(root, text="Enter password length (4-30)").pack(pady=3)

# Input entry for password length
validation = (root.register(validate_password_length), '%P')
Entry(root, textvariable=passlen, validate="key", validatecommand=validation).pack(pady=3)

# Generate Password button
Button(root, text="Generate Password", command=generate_password).pack(pady=7)
Label(root, text="Password Generated").pack(pady=3)
Entry(root, textvariable=passstr, state='readonly').pack(pady=3)  # Make read-only for better UX

# Start the main event loop
root.mainloop()
