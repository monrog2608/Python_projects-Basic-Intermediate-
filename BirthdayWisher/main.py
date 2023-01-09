
from datetime import datetime
import pandas
import smtplib
import random


today = datetime.now()
today_tuple = (today.month, today.day)

my_email = "myemail@gmail.com"
my_password = "mypassword"

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:

    birthdays_person = birthdays_dict[today_tuple]


    file_path = f"letter_templates\letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents =letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_person["email"],
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )




