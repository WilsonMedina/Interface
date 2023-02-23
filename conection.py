from tkinter import messagebox
import sqlite3

#========================================Funtion create database========================================================

def conetion_database():

    database = sqlite3.connect('users_database')
    pointer = database.cursor()

    try:

        pointer.execute('''create table Users
                (id integer primary key autoincrement,
                first_name varchar(50),
                last_name varchar(50),
                password varchar(50), 
                email varchar(50) unique,
                text_box varchar(1000))
                ''')
        messagebox.showinfo('Database', 'successfully created' )
    
    except:

        messagebox.showwarning('Warning', 'Database already exists')

    database.close()
        