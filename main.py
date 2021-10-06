from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import ctypes
import hashlib
import csv

ctypes.windll.shcore.SetProcessDpiAwareness(1)

valid_users = []


with open('users.csv', 'r') as f:
<<<<<<< HEAD
    file = csv.DictReader(f)
    for elem in file:
        valid_users.append(elem)


def hash(string):
    return hashlib.sha256(str.encode(string)).hexdigest()


def quitwindow(root):
    if messagebox.askyesno(title='Are you sure?', message='Are you sure you want to QUIT?'):
        root.destroy()


def back(currentroot, targetroot, quietly=False):
    if quietly:
        currentroot.destroy()
        targetroot()
    else:
        if messagebox.askyesno(title='Are you sure?', message='Are you sure you want to go back?'):
            currentroot.destroy()
            targetroot()
        else:
            return


def valid_user(inp_username, inp_password):
    for user in valid_users:
        if user['username'] == inp_username and user['password'] == hash(inp_password):
            return True
        else:
            pass
    return False


def loginpage():
    def login():
        usn = username.get()
        psw = password.get()
        if valid_user(usn, psw):
            confirmation = messagebox.askyesnocancel(title='Continue?', message=f'Would you like to login as {usn}?')
            if confirmation:
                login_page.destroy()
                controlpanel(usn)
            else:
                return
        else:
            messagebox.showerror(title='Error', message='Invalid credentials.')

    def callback(event):
        login()

    def goto_signup():
        login_page.destroy()
        signuppage()

    def toggle_password(value):
        if value == 0:
            password['show'] = '*'
        else:
            password['show'] = ''

    login_page = Tk()
    login_page.geometry('400x400')
    login_page.title('Login')

    title = Label(login_page, text='Login')
    title.pack(side=TOP, pady=10)
    title.configure(font=('Arial',16, "bold"))

    login_page.bind('<Return>', callback)

    username_label = Label(text='Username: ')
    username_label.pack()
    username = Entry(login_page, width='20')
    username.pack()

    password_label = Label(text='Password: ')
    password_label.pack()
    password = Entry(login_page, width='20', show='*')
    password.pack()

    show_password_i = IntVar()
    show_password = Checkbutton(login_page, text='Show Password', variable=show_password_i, command=lambda: toggle_password(show_password_i.get()))
    show_password.pack()

    submit = Button(login_page, text='Login', command=login)
    submit.pack()

    quitbutton = Button(login_page, text='QUIT', command=lambda: quitwindow(login_page))
    quitbutton.pack(side=BOTTOM, pady=10)

    signup_button = Button(login_page, text='SIGN UP', command=goto_signup)
    signup_button.pack(side=BOTTOM)

    login_page.mainloop()


def signuppage():
    def add_user():
        usn = su_username.get()
        psw = su_password.get()
        for user in valid_users:
            if user['username'] == usn:
                messagebox.showerror(title='User exists', message='User already exists.')
                return

        valid_users.append({'username': usn, 'password': hash(psw)})
        messagebox.showinfo(title='Account created.', message=f'Account, {usn} created.')
        back(signup_page, loginpage, True)
        return

    def callback(event):
        add_user()

    def toggle_password(value):
        if value == 0:
            su_password['show'] = '*'
        else:
            su_password['show'] = ''

    signup_page = Tk()
    signup_page.geometry('400x400')
    signup_page.title('Login')

    signup_page.bind('<Return>', callback)

    title = Label(signup_page, text='Sign Up')
    title.pack(side=TOP, pady=10)
    title.configure(font=('Arial',16, "bold"))

    su_username_label = Label(text='Username: ')
    su_username_label.pack()
    su_username = Entry(signup_page, width='20')
    su_username.pack()

    su_password_label = Label(text='Password: ')
    su_password_label.pack()
    su_password = Entry(signup_page, width='20', show='*')
    su_password.pack()

    show_password_i = IntVar()
    show_password = Checkbutton(signup_page, text='Show Password', variable=show_password_i, command=lambda: toggle_password(show_password_i.get()))
    show_password.pack()

    add_user_b = Button(signup_page, text='Create Account', command=add_user)
    add_user_b.pack()

    quitbutton = Button(signup_page, text='QUIT', command=lambda: quitwindow(signup_page))
    quitbutton.pack(side=BOTTOM, pady=10)

    backbutton = Button(signup_page, text='BACK', command=lambda: back(signup_page, loginpage))
    backbutton.pack(side=BOTTOM)

    signup_page.mainloop()


def controlpanel(usn):
    def delete_account():
        for user in valid_users:
            if user['username'] == usn:
                if hash(simpledialog.askstring(title='Confirm password', prompt='Please confirm your password.', show='*')) == user['password']:
                    # delete user from valid_users
                    valid_users.remove(user)
                    back(control_panel, loginpage, True)
                    return
                else:
                    messagebox.showerror(title='Invalid password', message='Invalid credentials.')
            else:
                pass
        return

    control_panel = Tk()
    control_panel.geometry('800x500')
    control_panel.title(usn)

    welcome = Label(text=f'Welcome, {usn.capitalize()}.')
    welcome.pack(side=TOP, pady=10)
    welcome.configure(font=('Arial', 13, 'italic'))

    deleteaccount = Button(control_panel, text='Delete Account', command=lambda: delete_account())
    deleteaccount.pack()

    quitbutton = Button(control_panel, text='QUIT', command=lambda: quitwindow(control_panel))
    quitbutton.pack(side=BOTTOM, pady=10)

    logout = Button(control_panel, text='LOGOUT', command=lambda: back(control_panel, loginpage))
    logout.pack(side=BOTTOM)

    control_panel.mainloop()


if __name__ == '__main__':
    loginpage()

    with open('users.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['username', 'password'])
        writer.writeheader()
        for elem in valid_users:
            writer.writerow(elem)
=======
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
  
  backButton = Button(adminPanel, text='Logout', command=lambda: backToAdminLogin(adminPanel))
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
>>>>>>> 5d0c81373e69338f119ead62b69a3708c986d9fe
