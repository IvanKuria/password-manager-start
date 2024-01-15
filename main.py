from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    user_password = "".join(password_list)
    password_entry.insert(0, user_password)

    # Copies the generate password to your clipboard. Pretty cool!
    pyperclip.copy(user_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_value = website_entry.get()
    email = email_username_entry.get()
    password_value = password_entry.get()

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields blank")
    else:
        is_ok = messagebox.askokcancel(title=website_value,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: {password_value}\nIs it ok to save")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_value} | {email} | {password_value}\n")
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_lock_image)
canvas.grid(column=1, row=0)

# Website label
website = Label(text="Website:")
website.grid(column=0, row=1)

# Website entry widget
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username label
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

# Email/Username entry
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "ivankuria7@gmail.com")

# Password label
password = Label(text="Password:")
password.grid(column=0, row=3)

# Password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate Password button
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

# Add button
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
