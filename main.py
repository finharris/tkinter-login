import csv
import hashlib
from datetime import datetime
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


def getCurrentDatetime():
  return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


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
    showinfo("Sucessful login", f"Welcome, {user['username']}.\n Last login: {user['lastLogin']}\nAccount Created: {user['accountCreated']}")
    
    for elem in userData:
      if elem['username'] == usernameValue:
        elem['lastLogin'] = getCurrentDatetime()
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
  
  userData.append({'username': usernameValue,'password': hashPassword(passwordValue),'lastLogin': 'N/A', 'accountCreated': getCurrentDatetime()})
  showinfo('Sucess', f'Welcome, {usernameValue}, your account has been created.')
  
  username.delete(0,END)
  password.delete(0,END)


def save():
  with open('users.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['username','password','lastLogin','accountCreated'])
    writer.writeheader()
    for elem in userData:
      writer.writerow(elem)


def printUserData():
  for elem in userData:
    for key, value in elem.items():
      # print(key, ' : ', value)
      print(f"'{key}': '{value}'")
    print('')


def openAdminLogin():
  adminLogin = Tk()
  adminLogin.attributes('-topmost', True)
  adminLogin.title('Admin Panel')
  adminLogin.geometry('600x320')
  
  login = Frame(adminLogin, relief=RAISED, borderwidth=4)
  
  adminPasswordLabel = Label(text='Admin Password:', master=login)
  adminPassword = Entry(master=login)
  adminPasswordLabel.pack()
  adminPassword.pack()
  
  adminLoginButton = Button(master=login, text='Login', command=lambda: openAdminPanel(adminLogin, adminPassword))
  adminLoginButton.pack()
  
  login.pack()
  
  adminLogin.mainloop()
  return


def backToAdminLogin(window):
  window.destroy()
  openAdminLogin()


def openAdminPanel(prevWindow, adminPassword):
  psw = adminPassword.get()
  
  if len(psw) < 1:
    return
  
  if psw == 'admin':
    prevWindow.destroy()
  else:
    showinfo('Incorrect Admin Password', 'The admin password you entered was incorrect.')
    return

  adminPanel = Tk()
  adminPanel.title('Admin Panel')
  adminPanel.geometry('600x320')
  
  printUsers = Button(adminPanel, text='Print User Data', command=printUserData)
  printUsers.pack()
  
  backButton = Button(adminPanel, text='Back', command=lambda: backToAdminLogin(adminPanel))
  backButton.pack(side=BOTTOM)
  
  adminPanel.mainloop()


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

# ADMIN BUTTON
adminbutton = Button(root, command=openAdminLogin, text='Admin Panel')
adminbutton.pack(side=BOTTOM)

# MAIN LOOP
root.mainloop()

# after window close save the data
save()