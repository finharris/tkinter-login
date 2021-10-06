from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import ctypes
import hashlib
import csv

ctypes.windll.shcore.SetProcessDpiAwareness(1)

valid_users = []


with open('users.csv', 'r') as f:
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
