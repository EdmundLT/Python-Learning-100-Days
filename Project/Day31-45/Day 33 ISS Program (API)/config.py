import smtplib


def send_email():
    my_email = "123@gmail.com"
    password = 12345678"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email, msg="Subject:Look Up! \n\n The ISS is over your head!")

    connection.close()
