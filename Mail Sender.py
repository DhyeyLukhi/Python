import smtplib

email = "dhyeylukhi72@gmail.com"
receiver = ['manta.lukhi@gmail.com']

subject1 = "Go to the top and start reading from there"

message = [
           "If you had started reading these emails from here, so i request you to go to the top and start reading from there, because there is a special message and special order to reading these emails, And if this is last in reading then No Worry  ",
           "Who had too much interest in PYTHON and he had his own Desktop Assistant",
           "There is only one Friend in you Friends' list...",
           "And if you are looking for that guy who send this emails...",
           "Now, you can reply me in mails or WhatsApp and if you like this, take some time and call me, I am waiting your call/message/mail",
           "Yes, i remembered it! so i just want to say that all the previous emails including this are sent to you by using Python Scirpt",
           "You please carry on your work sorry for disturbing you",
           "Sorry to say but i forgot what i want to say",
           "Wait I forgot what i want to say",
           "So i just want to say that...",
           "Don't feel special by previous email, it is just formality",
           "This is only for you",
           "We are not hacking your account, so feel free and please continue reading...",
           "And we are happy that you are reading our emails",
           "Hello, this is Prime"
           ]


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "iaoxsfvssornxebn")

for i in range(0, len(message)):
    if i == 0:
        text = f"Subject: {subject1} \n\n{message[i]}"

        server.sendmail(email, receiver, text)

        print(f"Email Sent no. {i+1} to {receiver}")
    else:
        text = f" {message[i]}"
        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.starttls()
        #
        # server.login(email, "iaoxsfvssornxebn")

        server.sendmail(email, receiver, text)

        print(f"Email Sent no. {i+1} to {receiver}")
