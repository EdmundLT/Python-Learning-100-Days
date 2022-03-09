##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

PLACEHOLDER = "[NAME]"


now = dt.datetime.now()
current_month = now.month
current_day = now.day


def find_letter(name):
    rd_num = random.randint(0, 2)
    with open(f"letter_templates/letter_{rd_num}.txt") as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
    return sending_email(new_letter)


def sending_email(context):
    my_email = "ptesting977@gmail.com"
    password = "Qpzm9099099"
    message = context
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="tledmund0921@gmail.com", msg=f"Subject:Happy Birthday\n\n{message}")

    connection.close()


data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
for key in data_dict:
    if key["month"] == current_month and key["day"] == current_day:
        find_letter(key["name"])
