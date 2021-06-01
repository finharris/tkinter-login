from tkinter import *
from tkinter import Button, Tk, HORIZONTAL
from tkinter.messagebox import showinfo


def login():
  usernameValue = username.get()
  passwordValue = password.get()
  
  if len(usernameValue) < 1 or len(passwordValue) < 1:
    # SHOW POPUP
    showinfo("Error", "Please ensure all fields are filled out.")
    return
  
  # FIND VALID USERNAME AND PASSWORD IN CSV AND CHECK AGAINST THEM


# DEFINE ROOT
root = Tk()
root.title("Test Tkinter App")
root.geometry("600x320")

# TITLE
title = Label(text='Sign Up and Login')
title.pack()

# OPEN CONTAINER
container = Frame(relief=RAISED, borderwidth=4)

# USERNAME
usernameLabel = Label(text='Username:', master=container)
username = Entry(master=container)
usernameLabel.pack()
username.pack()

# PASSWORD
passwordLabel = Label(text='Password:', master=container)
password = Entry(master=container)
passwordLabel.pack()
password.pack()

# CLOSE CONTAINER
container.pack(padx=10,pady=10)

# SUBMIT BUTTON
submitButton = Button(root, command=login, text='Login')
submitButton.pack()

# MAIN LOOP
root.mainloop()