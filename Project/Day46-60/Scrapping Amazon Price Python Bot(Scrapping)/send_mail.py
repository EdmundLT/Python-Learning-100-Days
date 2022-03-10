import smtplib


def send_email(contents):
    my_email = "ptesting977@gmail.com"
    password = "Qpzm9099099"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs="tledmund0921@gmail.com", msg=contents)

    connection.close()
