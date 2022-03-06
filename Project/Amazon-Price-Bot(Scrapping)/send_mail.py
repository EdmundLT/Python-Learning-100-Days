import smtplib


def send_email(contents):
    my_email = "abc@gmail.com"
    password = "123"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs="abc@gmail.com", msg=contents)

    connection.close()
