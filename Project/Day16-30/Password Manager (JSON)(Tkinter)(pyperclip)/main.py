from email import message
from tkinter import messagebox
from tkinter import *
from pwgen import generating_random_password
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pw():
    password.delete(0, END)
    genpw = generating_random_password()
    password.insert(0, genpw)
    pyperclip.copy(genpw)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    websites = website.get()
    username = email_or_username.get()
    passwords = password.get()
    new_data = {
        websites: {
            "email": username,
            "password": passwords,
        }
    }
    if len(websites) == 0 or len(username) == 0 or len(passwords) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


def search():
    search_website = website.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(
            title="Oops", message="No data file found")
    else:
        if search_website in data:
            email = data[search_website]["email"]
            pw = data[search_website]["password"]
            messagebox.showinfo(title="search_website",
                                message=f"Email: {email}\nPassword: {pw} ")
        else:
            messagebox.showwarning(
                title="Oops", message=f"No details for {search_website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50,)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)
# Label
label_1 = Label(text="Website:", highlightthickness=0)
label_1.grid(row=1, column=0)
label_2 = Label(text="Email/Username:", highlightthickness=0)
label_2.grid(row=2, column=0)
label_3 = Label(text="Password:", highlightthickness=0)
label_3.grid(row=3, column=0)
# Entries
website = Entry(width=21)
website.grid(row=1, column=1, columnspan=1)
website.focus()
email_or_username = Entry(width=35)
email_or_username.grid(row=2, column=1, columnspan=2)
email_or_username.insert(0, "contact@edmund-tang.com")
password = Entry(width=21)
password.grid(row=3, column=1)

# Button


generate_button = Button(text="Generate Password",
                         command=generate_pw, highlightthickness=0)
generate_button.grid(row=3, column=2)
search_button = Button(width=14, text="Search",
                       command=search, highlightthickness=0)
search_button.grid(row=1, column=2)
add = Button(width="36", text="Add",
             command=save, highlightthickness=0)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
