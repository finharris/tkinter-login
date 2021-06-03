import csv
import hashlib
import datetime
from tkinter import *
from tkinter import Button, Tk
from tkinter.messagebox import showinfo


userData = []
with open('users.csv', 'r') as f:
  file = csv.DictReader(f)
  for elem in file:
    userData.append(elem)


def fetchUser(username):
  for elem in userData:
    if elem['username'] == username:
      return elem
  return None


def hashPassword(password):
  return hashlib.sha256(str.encode(password)).hexdigest()


def login():
  usernameValue = username.get()
  passwordValue = password.get()
  
  if len(usernameValue) < 1 or len(passwordValue) < 1:
    # show popup
    showinfo("Error", "Please ensure all fields are filled out.")
    return
  
  # find valid username and password in csv and check against them
  user = fetchUser(usernameValue)
  if user and user['password'] == hashPassword(passwordValue):
    showinfo("Sucessful login", f"Welcome, {user['username']}.")
    
  else:
    showinfo('Login failure', 'Please ensure your username and password are valid.')


def signup():
  usernameValue = username.get()
  passwordValue = password.get()
  
  if len(usernameValue) < 1 or len(passwordValue) < 1:
    # show popup
    showinfo("Error", "Please ensure all fields are filled out.")
    return

  for elem in userData:
    if elem['username'] == usernameValue:
      showinfo('User already exists', 'A user with that username already exists, try another username.')
      return
  
  userData.append({'username': usernameValue,'password': passwordValue,'lastLogin': datetime.datetime})
  showinfo('Sucess', f'Welcome, {usernameValue}, your account has been created.')


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

# LOGIN BUTTON
loginButton = Button(root, command=login, text='Login')
loginButton.pack()

# SIGNUP BUTTON
signupButton = Button(root, command=signup, text='Signup')
signupButton.pack()

# MAIN LOOP
root.mainloop()

with open('users.csv', 'w', newline='') as f:
  writer = csv.DictWriter(f, fieldnames=['username','password','lastLogin'])
  writer.writeheader()
  for elem in userData:
    writer.writerow(elem)