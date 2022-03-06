import smtplib


def send_mail(data_list):
    data = data_list
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    user_message = data["message"]

    message = f"Subject:Hello\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {user_message}"
    my_email = "ptesting977@gmail.com"
    password = "Qpzm9099099"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs="tledmund0921@gmail.com", msg=message)

    connection.close()
