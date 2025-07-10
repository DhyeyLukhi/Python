import datetime
import re


class TODO:
    def __init__(self):
        pass

    def complete_task(self):  # I will further add a feature which will save the date and time when the task if completed
        name_of_task = input("Name of task: ")
        tasks = []
        with open("TODO_LIST", 'r') as file:
            for lines in file:
                lines.strip()
                key, value = lines.split(':', 1)
                key, value = key.strip(), value.strip()
                hour = datetime.datetime.now().strftime("%I")
                minute = datetime.datetime.now().strftime("%M")
                time = datetime.datetime.now().strftime("%p")
                if name_of_task == key:
                    value = True
                    tasks.append(f"{key} : {value} ({hour} : {minute} {time})  \n")
                    print("Task Completed")
                else:
                    tasks.append(f"{key} : {value} \n")

        with open("TODO_LIST", 'w') as file:
            file.writelines(tasks)


    def show_task(self):
        with (open("TODO_LIST", 'r') as file):

            for lines in file:
                lines.strip()
                key, value = lines.split(':', 1)
                key, value = key.strip(), value.strip()

                if value == "False":
                    print(f"{key}: Not Done")

                else:
                    formate = re.search(r'True(.+)', value)
                    time = formate.group(1)
                    time = time.replace('(', '').replace(')', '').strip()
                    print(f"{key}: Done at {time}")

    def add_task(self, task):

        with open("TODO_LIST", 'a') as file:
            file.write(f"{task} : {False} \n")
        print("Task Added")

    def show_task_run(self):
        with (open("TODO_LIST", 'r') as file):
            for lines in file:
                lines.strip()
                key, value = lines.split(':', 1)  # It was getting error because it is asigning the \n in the value of the variable
                key, value = key.strip(), value.strip()  # By using the strip function it can remove the trailing spaces and other things from the string variable
                if value != "False" and value != "True":
                    store_key = key
                    tasks = []
                    with open("TODO_LIST", 'r') as file:
                        for lines2 in file:
                            lines2.strip()
                            key, value = lines2.split(':', 1)
                            key, value = key.strip(), value.strip()
                            if store_key == key:
                                pass
                            else:
                                tasks.append(f"{key} : {value} \n")

                    with open("TODO_LIST", 'w') as file:
                        file.writelines(tasks)

                elif value == "False":
                    print(f"{key}: Not Done")
                elif value == "True":
                    print(f"{key}: {value}")


if __name__ == '__main__':
    tasks = TODO()
    tasks.show_task_run()

    while True:
        try:
            print("1. Show Task")
            print("2. Add Task")
            print("3. Complete Task")

            choice = int(input("Choice: "))
            if choice == 1:
                tasks.show_task()

            elif choice == 2:
                taskname = input("Task: ")
                tasks.add_task(task=taskname)

            elif choice == 3:
                tasks.complete_task()

            else:
                pass

        except Exception as e:
            print(e)
