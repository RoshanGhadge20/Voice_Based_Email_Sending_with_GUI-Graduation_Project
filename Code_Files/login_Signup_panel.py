from tkinter import *
import tkinter as tk
import PIL
from PIL import Image

from tkinter import messagebox
from PIL import ImageTk
from tkinter import PhotoImage
import mysql.connector

import Email_Send_gif as obj2
import voicebased_emailsend as obj3


mydatabase = mysql.connector.connect(host="localhost", user="root", password="sshubhamg", port="3306", database="project")
cursor = mydatabase.cursor()
# query="create database project"
# query1="create table sample_project1(username varchar(30),password varchar(30));"
# query2='insert into  sample_project1(username,password) values("Roshan1","roshan@1234");'

# query="create table login(username varchar(30),password varchar(30));"
# query="create table signup(firstname varchar(30),middlename varchar(30),lastname varchar(30),username varchar(30),password varchar(30));"




class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        self.bg_icon = ImageTk.PhotoImage(file="background .jpg")
        self.user_icon = ImageTk.PhotoImage(file="man user.png")
        self.pass_icon = ImageTk.PhotoImage(file="lock.png")
        self.Logo_icon = PhotoImage(file="logo.png")
        self.uname = StringVar()
        self.pass_ = StringVar()
        bg_lb1 = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="yellow", fg="red",bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=90)

        logolbl = Label(Login_Frame, image=self.Logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="white").grid(row=1, column=0, padx=1, pady=1)
        txtuser = Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15)).grid(row=1, column=1,padx=20)
        lblpass = Label(Login_Frame, text="password", image=self.pass_icon, compound=LEFT,font=("times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=2, pady=1)
        txtpass = Entry(Login_Frame, show="*", bd=5, relief=GROOVE, textvariable=self.pass_, font=("", 15)).grid(row=2,column=1,padx=20)
        btn_log = Button(Login_Frame, text="Login", command=self.login, width=15, font=("times new roman", 14, "bold"),bg="light blue", fg="black").grid(row=3, column=1, pady=10)
        btn_log1 = Button(Login_Frame, text="Signup", command=self.Signup, width=15,font=("times new roman", 14, "bold"), bg="light blue", fg="black").grid(row=3, column=2,pady=10)

    def login(self):
        query2 = "select * from signup";
        cursor.execute(query2)
        user_info = cursor.fetchall()
        check_username = self.uname.get()
        print(check_username)
        check_password = self.pass_.get()
        print(check_password)
        print(user_info)
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required!!")


        for (firstname, middlename, lastname, username, password) in user_info:
            fst = firstname

            # query4='select * from login where username="check_username";'
            # cursor.execute(query4)

            if (username == check_username and password == check_password):
                print("data match through databases")
                messagebox.showinfo("successful", f"welcome {fst}")
                root.destroy()
                obj3.sendmail()
                obj2.Mail_send_gif()
                break

            elif (username != check_username and password == check_password):
                messagebox.showerror("Invalid username")
                break
            elif (username == check_username and password != check_password):
                messagebox.showerror("Invalid Password")
                break



    def Signup(self):
        root.destroy()
        win = Tk()
        win.geometry("750x426")
        win.title("SIGNUP WINDOW")
        load = PIL.Image.open('bg1 .jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(win, image=render)
        img.place(x=0, y=0)
        lab1 = Label(win, text="Enter your firstname:", font=("times new roman", 12,))
        lab1.grid(row=0, column=1, padx=5, pady=5)
        fnameE = Entry(win, font=("", 15), bd=2)
        fnameE.grid(row=0, column=2)
        lab2 = Label(win, text="Enter your middlename:", font=("times new roman", 12,))
        lab2.grid(row=1, column=1, padx=5, pady=5)
        mnameE = Entry(win, font=("", 15), bd=2)
        mnameE.grid(row=1, column=2)

        lab3 = Label(win, text="Enter your lastname:", font=("times new roman", 12,))
        lab3.grid(row=2, column=1, padx=5, pady=5)
        lnameE = Entry(win, font=("", 15), bd=2)
        lnameE.grid(row=2, column=2)

        lab4 = Label(win, text="Enter your username:", font=("times new roman", 10, "bold"))
        lab4.grid(row=3, column=1, padx=5, pady=5)
        usernameE = Entry(win, font=("", 15), bd=2)
        usernameE.grid(row=3, column=2)

        lab5 = Label(win, text="Enter your password:", font=("times new roman", 12,))
        lab5.grid(row=4, column=1, padx=5, pady=5)
        passE = Entry(win, show="*", font=("", 15), bd=2)
        passE.grid(row=4, column=2)

        lab6 = Label(win, text="Retype your password:", font=("times new roman", 12,))
        lab6.grid(row=5, column=1, padx=5, pady=5)
        passrE = Entry(win, show="*", font=("", 15), bd=2)
        passrE.grid(row=5, column=2)

        # btn1 = Button(win, text="Submit", command=lp.Submit, font=("times new roman", 15, "bold"), fg="red")
        # btn1.grid(row=6, column=2)

        #dm.signup_page()

        # window = Tk()
        # window.title("SIGNUP WINDOW")
        # window.geometry("1350x700+0+0")
        # load=Image.open('background .jpg')
        # # render=ImageTk.PhotoImage(load)
        # # img=Label(window,image=render)
        # # img.place(x=0,y=0)
        # # bg_icon2 = ImageTk.PhotoImage(file="background .jpg")
        # # bg_lb2 = Label(window, image=bg_icon2).pack()
        #
        #
        # lab1 = Label(window, text="Enter your firstname:", font=("times new roman", 12,))
        # lab1.grid(row=0, column=1, padx=5, pady=5)
        # fnameE = Entry(window, font=("", 15), bd=2)
        # fnameE.grid(row=0, column=2)
        # lab2 = Label(window, text="Enter your middlename:", font=("times new roman", 12,))
        # lab2.grid(row=1, column=1, padx=5, pady=5)
        # mnameE = Entry(window, font=("", 15), bd=2)
        # mnameE.grid(row=1, column=2)
        #
        # lab3 = Label(window, text="Enter your lastname:", font=("times new roman", 12,))
        # lab3.grid(row=2, column=1, padx=5, pady=5)
        # lnameE = Entry(window, font=("", 15), bd=2)
        # lnameE.grid(row=2, column=2)
        #
        # lab4 = Label(window, text="Enter your username:", font=("times new roman", 10, "bold"))
        # lab4.grid(row=3, column=1, padx=5, pady=5)
        # usernameE = Entry(window, font=("", 15), bd=2)
        # usernameE.grid(row=3, column=2)
        #
        # lab5 = Label(window, text="Enter your password:", font=("times new roman", 12,))
        # lab5.grid(row=4, column=1, padx=5, pady=5)
        # passE = Entry(window, show="*", font=("", 15), bd=2)
        # passE.grid(row=4, column=2)
        #
        # lab6 = Label(window, text="Retype your password:", font=("times new roman", 12,))
        # lab6.grid(row=5, column=1, padx=5, pady=5)
        # passrE = Entry(window, show="*", font=("", 15), bd=2)
        # passrE.grid(row=5, column=2)

        def Submit():
            fname = fnameE.get()
            mname = mnameE.get()
            lname = lnameE.get()
            username1 = usernameE.get()
            password = passE.get()
            password1 = passrE.get()

            if (password == password1):
                print("Password is match successfully")
                lab7 = Label(win, text="PASSWORD IS MATCH SUCCESSFULLY")
                lab7.grid(row=7, column=2)
                # messagebox.showinfo("NEW REGISTRATION IS SUCESSFUL")
                lab9 = Label(win, text="NEW REGISTRATION IS COMPLETED")
                lab9.grid(row=8, column=2)
            else:
                print("Password is not match correctly")
                lab8 = Label(win, text="PASSWORD IS NOT MATCH CORRECTLY")
                lab8.grid(row=7, column=2)
                lab10 = Label(win, text="PLEASE ENTER VALID PASSWORD")
                lab10.grid(row=8, column=2)
                # messagebox.showinfo("PASSWORD IS NOT MATCH PLEASE ENTER VALID PASSWORD")
            query1 = 'insert into signup(firstname,middlename,lastname,username,password) values("{}","{}","{}","{}","{}");'.format(
                fname, mname, lname, username1, password1)
            # query2='insert into login(username,password) values("{}","{}");'.format(username1,password1)
            print(fname)
            print(mname)
            print(lname)
            print(username1)

            cursor.execute(query1)
            mydatabase.commit()

        btn1 = Button(win, text="Submit", command=Submit, font=("times new roman", 15, "bold"), fg="Black", bg="light blue")
        btn1.grid(row=6, column=2)
        win.mainloop()

root = Tk()
obj = Login_System(root)
root.mainloop()
