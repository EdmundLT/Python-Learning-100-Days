import os
from twilio.rest import Client


def send_message(content):
    account_sid = os.environ.get("AC_SID")
    auth_token = os.environ.get("AUTH_TOKEN")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"content: {content}",
            from_='+19036647114',
            to='+14379894416'
        )
    return message.status
