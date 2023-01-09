from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               ' v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols +password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)


def save():

    website=website_input.get()
    email=email_input.get()
    password=password_input.get()


    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any fields empty.")
    else:

        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                  f"\nEmail: {email} \nPassword: {password} \n It it ok to save?")
    if is_ok:

        with open("data.txt","a") as data_file:
            data_file.write(f"{website}| {email}|{password}\n")

            website_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width= 200, height=200)
logo_ing=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_ing)
canvas.grid(row=0, column =1)


website_label=Label(text="Website:")
website_label.grid(row=1, column =0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column =0)
password_label=Label(text="Password:")
password_label.grid(row=3, column =0)

website_input=Entry(width=35)
website_input.grid(column =1, row =1, columnspan=2)
website_input.focus()
email_input=Entry(width=35)
email_input.grid(column =1, row =2, columnspan=2)
email_input.insert(0, "myemail@gmail.com")
password_input=Entry(width=21)
password_input.grid(column =1, row =3)


generate_password_button=Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button=Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4,columnspan=2)







window.mainloop()