import smtplib
import time
import keyboard
from pynput import keyboard
# from docx import Document


try:
    email = "dhyeylukhi72@gmail.com"
    customer_care = "+91 82388 63322"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    with open("F:\\Tendoze\\apppassword.txt", 'r') as file:
        password = file.read()
        server.login(email, password)
    file.close()

except Exception as e:
    print(f"\n{e}")


def SendMail(mailID, subject, message):
    text = f"Subject: {MailDetails.subject} \n\n{MailDetails.message}"
    try:
        server.sendmail(email, CustomerDetails.email, text)
        print("\nMail Sent successfully")
        return False

        # let's add the name, mobile number, email-id of the curstomer in the Excel Sheets

    except Exception as e:
        print(f"\n{e}")
        print("Mail Cannot be Sent")
        return False


def procedder(key):
    """The issue is that it can't get the confirmation after the first time"""

    if key.char == 'y':
        time.sleep(1)
        SendMail(CustomerDetails.email, MailDetails.subject, MailDetails.message)
        return False

    elif key.char == 'n':
        time.sleep(1)
        print("\nN is pressed, So Mail is not Send")
        return False

    else:
        time.sleep(1)
        print("\nWrong Input, Try Again.")
        return True


def confirmation():
    try:
        print("\n")
        print("Would you like to continue ?")
        print("[Y] Yes  [N] NO     :", end=" ")

        with keyboard.Listener(on_press=procedder) as listener:
            listener.join()

    except Exception as e:
        print(f"\n{e}")


class Customer:
    def __init__(self, name, number, mail_id):
        self.name = name
        self.number = number
        self.email = mail_id


class Mail:
    def __init__(self):
        self.subject = "Tendoze Food"
        self.message = (
            f"Hello {CustomerDetails.name},\n\t You had recently ordered food products from Tendoze Food. You will receive any kind of OTP regarding this on {CustomerDetails.number}.\n\nYour Order:\n")
        while True:
            try:
                Ginger = str(input("Ginger: "))
                if Ginger:
                    Ginger = int(Ginger)
                    break
                else:
                    Ginger = 0
                    break

            except Exception as e:
                print(e)

        while True:
            try:
                Haldi = str(input("Haldi: "))
                if Haldi:
                    Haldi = int(Haldi)
                    break
                else:
                    Haldi = 0
                    break

            except Exception as e:
                print(e)

        while True:
            try:
                Bit = str(input("Bit: "))
                if Bit:
                    Bit = int(Bit)
                    break
                else:
                    Bit = 0
                    break
            except Exception as e:
                print(e)

        if Ginger == 0 and Haldi == 0 and Bit == 0:
            print("This is not a valid order, Please re-enter the amount")

        else:
            if Ginger != 0:
                self.message += f"           Ginger: {Ginger} Boxes ({Ginger*15} Packets)\n"
            if Haldi != 0:
                self.message += f"           Haldi: {Haldi} Boxes ({Haldi*15} Packets)\n"
            if Bit != 0:
                self.message += f"           Bit: {Bit} Boxes ({Bit*15} Packets)\n"

            self.message += f"\nIf you had ordered this then kidnly ignore this mail. \nOtherwise you can contact to our customer care number {customer_care} \n\nDo not reply to this E-Mail. \n\n\nThank You, \nTendoze Food"


while True:
    try:
        print("\n")
        customer_name = input("Enter the Customer Name: ")
        customer_number = input("Enter the Customer Number: ")
        while True:
            customer_mail_id = input("Enter the Customer Mail ID: ")
            if '@' in customer_mail_id:
                break
            else:
                print("Wrong Mail ID")
        customer_name = customer_name.title()
        CustomerDetails = Customer(customer_name, customer_number, customer_mail_id)
        if "+" in CustomerDetails.number:
            pass
        else:
            CustomerDetails.number = "+91 " + CustomerDetails.number
        MailDetails = Mail()
        print("\n")
        print(f"Customer name: {CustomerDetails.name}")
        print(f"Customer number: {CustomerDetails.number}")
        print(f"Customer Mail ID: {CustomerDetails.email}")
        print()
        print(f"Mail Subject: {MailDetails.subject}")
        print(f"Mail Message: ")
        print(f"{MailDetails.message}")
        confirmation()

        # 1. at the mail id it wll not accept the mail with double '@' and without '@' --> Task completed
        # 2. while getting numbers in Ginger, Haldi and Bit it does not accept the character, I will put the try and except block at there, and if mistankenly the character is added, then it will also give you a chance to reenter value --> Task Completed
        # 3. I will also add the default value as 0, so you can enter it without entering value --> Task Completed
        # 4. app password will be got from the txt file which is at the Tendoze folder of the F drive --> Task Completed
        # 5. it will also add the data of the customer in the Excel file
        # 6. if you press the wrong key, then it will give you a chance to enter the correct key while confirming to send the mail or not --> Task Completed
        # 7. I will add the try block at every possible error code --> Task Completed
        # 8. I will enter the code which will check that if either Ginger, Haldi or Bit has order is not equal to 0, and if this is, then it will cancel the order --> Task Compeleted
    except Exception as e:
        print(e)
