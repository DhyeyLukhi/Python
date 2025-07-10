from tempmail import EMail
import os
from faker import Faker

fake = Faker()


def show_mails(message):
    print(f"New E-Mail Subject: {message.subject}")
    while True:
        if email.get_inbox():
            with open("Mail.html", 'w') as file:
                file.write(message.body)

            os.startfile("Mail.html")
            break


def clear_mail():
    with open("Mail.html", 'w') as file:
        file.write("")
    return


try:
    clear_mail()
    email = EMail()
    print(f"Name: {fake.name()}")
    print(f"Mail: {email.address}")
    print(f"Address: {fake.address()}")
    print(f"Text: {fake.text()}")
    print(f"Country: {fake.country()}")
    print(f"Latitude Longitude:{fake.latitude()}, {fake.longitude()}")
    print(f"URL: {fake.url()}")
    id_2 = None

    while True:
        message = email.wait_for_message(timeout=600)
        msg_id = message.id
        if id_2 != msg_id:
            show_mails(message)
            id_2 = msg_id

        else:
            pass


except Exception as e:
    print(e)
