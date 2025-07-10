import time
import webbrowser
import pyautogui


def whatsapp_send_to_multiple(text, numbers_list, times):
    text = text.replace('\n', '%0A')
    time.sleep(3)
    for phone_numbers in range(0, len(numbers_list)):
        for i in range(0, times):
            webbrowser.open(f"whatsapp://send?text=" + text + f'{text}' + "&phone=" + numbers_list[phone_numbers])
            time.sleep(0.2)
            pyautogui.hotkey('enter')
            pyautogui.hotkey('enter')

    return True


def whatsapp_send_unlimited(text, numbers_list, times):
    text = text.replace('\n', '%0A')
    time.sleep(3)
    if times == 0 and len(numbers_list) == 1:
        for phone_numbers in range(0, len(numbers_list)):
            while True:
                webbrowser.open(f"whatsapp://send?text=" + text + f'{text}' + "&phone=" + numbers_list[phone_numbers])
                pyautogui.hotkey('enter')

        return True

    elif times != 0 and len(numbers_list) == 1:
        for phone_numbers in range(0, len(numbers_list)):
            for i in range(0, times):
                webbrowser.open(f"whatsapp://send?text=" + text + f'{text}' + "&phone=" + numbers_list[phone_numbers])
                time.sleep(0.2)
                pyautogui.hotkey('enter')
                pyautogui.hotkey('enter')

        return True


if __name__ == '__main__':

    while True:
        times = 0
        message = ''
        try:
            numbers = []
            print("Leave the field empty when done")
            while True:
                number = numbercheck = input("Number(country code required): ")
                # Check if the number is valid or not
                if number:
                    numbercheck = numbercheck.removeprefix('+')
                    if number.count('+') == 1 and numbercheck.isnumeric():
                        numbers.append(number)

                    else:
                        print("try again.")
                    # If there is more than 1 number, exeute this
                elif len(numbers) > 1 and not number:
                    print(numbers)
                    times = int(input("Number of times: "))
                    message = str(input("Message: "))

                    if times and message:
                        whatsapp_send_to_multiple(text=message, numbers_list=numbers, times=times)
                        break

                    elif not times:
                        print("Please enter the number of times")

                    elif not message:
                        print("Please enter the number of message")

                    else:
                        pass

                # If there is only one number, execute this
                elif len(numbers) == 1 and not number:
                    print(numbers)
                    print("Leave blank for infinity")
                    times = input("Number of times: ")
                    message = str(input("Message: "))

                    # If user want to send limited number of messages
                    if times and message:
                        times = int(times)
                        whatsapp_send_to_multiple(text=message, numbers_list=numbers, times=times)
                        break

                    # If user want to send unlimited messages
                    elif not times and message:
                        print("!!! Be careful !!!")
                        print("Sending WhatsApp message unlimited times may harm your computer")
                        print("You may put in trouble to stop it")

                        # Ask user to confirm their response for unlimited messages
                        while True:
                            ask = input("Type 'yes' if you are sure: ")
                            if ask == 'yes':
                                times = 0
                                whatsapp_send_unlimited(text=message, numbers_list=numbers, times=times)
                                break

                            elif ask == 'no':
                                print("Stopping the execution...")
                                break

                    elif not message:
                        print("Please enter the number of message")

                    else:
                        pass

                elif not number and not numbers:
                    print("Nothing stored and entered")

        except Exception as e:
            print(e)
