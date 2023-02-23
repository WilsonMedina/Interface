from tkinter import *
from tkinter import messagebox
import sqlite3
from conection import conetion_database

#========================================Funtions=================================================================

#========================================Funtion exit app=========================================================

def exit():

    value = messagebox.askquestion('Exit', 'Do you want to exit to the aplication?')

    if value == 'yes':
        root.destroy()

#========================================Funtion clean screen========================================================

def clean_screen():

    id_string.set('')
    first_name_string.set('')
    last_name_string.set('')
    password_string.set('')
    email_string.set('')
    text_box.delete(1.0, END)

#=======================================Funtion license==================================================================

def license():

    messagebox.showinfo('Database', 'Licensed under the authority of Wilson Medina 2023')

#========================================Funtion about===========================================================

def about():

    messagebox.showinfo('Database', 'Program developed in february 2023 by Wilson Medina with the great tutorship of juan de españa')

#========================================Funtions CRUD===========================================================

#========================================Funtion create========================================================

def create():

    database = sqlite3.connect('users_database')
    pointer = database.cursor()

    try:

        many_insert = [
        (first_name.get(), last_name.get(), password.get(), email.get(), text_box.get('1.0', END))
        ]
        pointer.executemany('insert into Users values(null,?,?,?,?,?)', many_insert)
        database.commit()

        clean_screen()

        messagebox.showinfo('Database', 'successfully added' )

    except:

        messagebox.showwarning('Database', 'email already exists in another user')

        email_string.set('')

    database.close()

#========================================Funtion read========================================================  

def read():

    database = sqlite3.connect('users_database')
    pointer = database.cursor()

    try:

        pointer.execute("select * from Users where id= " + id_string.get())

        user_show = pointer.fetchall()

        for user in user_show:

            id_string.set(user[0])
            first_name_string.set(user[1])
            last_name_string.set(user[2])
            password_string.set(user[3])
            email_string.set(user[4])
            text_box.insert(1.0, user[5])

        database.commit()

    except:

        messagebox.showwarning('Database', 'User does not exist yet')

    database.close()

#========================================Funtion update========================================================

def update():

    database = sqlite3.connect('users_database')
    pointer = database.cursor()

    try:

        many_insert = first_name_string.get(), last_name_string.get(), password_string.get(), email_string.get(), text_box.get('1.0', END)
    

        pointer.execute("update Users set first_name = ?, last_name = ?, password = ?, email = ?, text_box = ?" +
                    "where id = " + id_string.get(), many_insert)
        database.commit()

        clean_screen()

        messagebox.showinfo('Database', 'successfully updated' )

    except:

        messagebox.showwarning('Database', 'User does not exist yet')

    database.close()

#========================================Funtion delete========================================================

def delete():

    try:

        database = sqlite3.connect('users_database')
        pointer = database.cursor()

        pointer.execute('delete from Users where id = ' + id_string.get())
        database.commit()

        clean_screen()

        messagebox.showinfo('Database', 'successfully deleted' )

    except:
        
        messagebox.showwarning('Database', 'User does not exist yet')

    database.close()

#=======================================Menu and submenu=====================================================================

root = Tk()

menu_bar = Menu(root)
root.config(menu=menu_bar, width=300, height=300)

database_menu = Menu(menu_bar, tearoff=0)
database_menu.add_command(label='Connect', command= conetion_database)
database_menu.add_command(label='Exit', command= exit)

crud_menu = Menu(menu_bar, tearoff=0)
crud_menu.add_command(label='Create', command=create)
crud_menu.add_command(label='Read', command=read)
crud_menu.add_command(label='Update', command=update)
crud_menu.add_command(label='Delete', command=delete)

clean_screen_menu = Menu(menu_bar, tearoff=0)
clean_screen_menu.add_command(label='Clean Screen', command=clean_screen)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='License', command=license)
help_menu.add_command(label='About', command=about)

menu_bar.add_cascade(label='DataBase', menu=database_menu)
menu_bar.add_cascade(label='CRUD', menu=crud_menu)
menu_bar.add_cascade(label='Clean screen', menu=clean_screen_menu)
menu_bar.add_cascade(label='Help', menu=help_menu)

#=======================================Identifiers and input fields=========================================================

first_frame = Frame(root)
first_frame.pack()

id_string = StringVar()
first_name_string = StringVar()
last_name_string = StringVar()
password_string = StringVar()
email_string = StringVar()

id_label = Label(first_frame, text='ID')
id_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)

first_name_label = Label(first_frame, text='First name')
first_name_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

last_name_label = Label(first_frame, text='Last name')
last_name_label.grid(row=2, column=0, sticky='e', padx=10, pady=10)

password_label = Label(first_frame, text='Password')
password_label.grid(row=3, column=0, sticky='e', padx=10, pady=10)

email_label = Label(first_frame, text='Email')
email_label.grid(row=4, column=0, sticky='e', padx=10, pady=10)

text_box_label = Label(first_frame, text='Write something')
text_box_label.grid(row=5, column=0, sticky='e', padx=10, pady=10)

id = Entry(first_frame, textvariable= id_string)
id.grid(row=0, column=1, padx=10, pady=10)

first_name = Entry(first_frame, textvariable= first_name_string)
first_name.grid(row=1, column=1, padx=10, pady=10)
first_name.config(fg='blue', justify='left')

last_name = Entry(first_frame, textvariable=last_name_string)
last_name.grid(row=2, column=1, padx=10, pady=10)
last_name.config(fg='blue', justify='left')

password = Entry(first_frame, textvariable= password_string)
password.grid(row=3, column=1, padx=10, pady=10)
password.config(show='*')

email = Entry(first_frame, textvariable= email_string)
email.grid(row=4, column=1, padx=10, pady=10)

text_box = Text(first_frame, width=16, height=5)
text_box.grid(row=5, column=1, padx=10, pady=10)
Scrollvert = Scrollbar(first_frame, command=text_box.yview)
Scrollvert.grid(row=5, column=2, sticky='nsew')
text_box.config(yscrollcommand=Scrollvert.set)

#=====================================Lower buttons======================================================

second_frame = Frame(root)
second_frame.pack()

button_create = Button(second_frame, text='Create', command=create)
button_create.grid(row=1, column=0, sticky='e', padx=10, pady=10)

button_read = Button(second_frame, text='Read', command=read)
button_read.grid(row=1, column=1, sticky='e', padx=10, pady=10)

button_update = Button(second_frame, text='Update', command=update)
button_update.grid(row=1, column=2, sticky='e', padx=10, pady=10)

button_delete = Button(second_frame, text='Delete', command=delete)
button_delete.grid(row=1, column=3, sticky='e', padx=10, pady=10)

#======================================Root mainloop====================================================

root.mainloop()




