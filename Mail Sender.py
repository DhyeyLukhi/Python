import smtplib

email = "dhyeylukhi72@gmail.com"
receiver = ['dhyeylukhi95@gmail.com']

subject1 = "Go to the top and start reading from there"

message = "here is the"


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "iaoxsfvssornxebn", initial_response_ok=True)

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
