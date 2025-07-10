import pywhatkit

while True:
    try:
        topic = input("Enter the topic: ")
        pywhatkit.playonyt(topic=str(topic))

        print("Played")

    except Exception as e:
        print(e)
