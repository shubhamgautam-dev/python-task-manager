print("========================")
print("PYTHON TASK MANAGER")
print("========================")

print("\nWelcome to To-Do-List !")

try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file]

except FileNotFoundError:
    tasks = []

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter Your Choice (1-5): ")

    if choice == "1":
        new_task = input("Enter a Task: ")
        new_task = new_task.strip()
        if new_task.strip() == "":
            print("Task Cannot Be Empty!")
        else:
            tasks.append(new_task)

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")


    elif choice == "2":

        if tasks:

            print("Your Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(i, task)

        else:

            print("No Tasks Found!")

    elif choice == "3":
        if not tasks:
            print("No Tasks Found!")
            continue

        print("Your Tasks: ")
        for i, task in enumerate(tasks, start=1):
            print(i, task)

        if not tasks:
            print("No Tasks Found!")
        try:
            selection = int(input("Which task do you want to complete?: "))
            if 1 <= selection <=len(tasks):
                index = selection - 1
                if tasks[index].endswith("[Completed]"):
                    print("Task Already Completed")
                else:
                    print(tasks[index])
                    tasks[index] = tasks[index] + " [Completed]"
                    with open("tasks.txt", "w") as file:
                        for task in tasks:
                            file.write(task + "\n")
                    print("Task marked as completed!")

            else:
                 print("Invalid Task Number")

        except ValueError:
            print("please Enter a Valid Number.")

    elif choice == "4":
        if not tasks:
            print("No Tasks Found!")
            continue
        else:
            print("Your Tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
            try:
                selection = int(input("Which Task You Want to Delete?: "))
                if 1 <= selection <= len(tasks):
                    index = selection - 1
                    print(tasks[index])
                    removed_task = tasks.pop(index)
                    print("Task Deleted Successfully!")
                    with open("tasks.txt","w")as file:
                        for task in tasks:
                            file.write(task+ "\n")


                else:
                    print("Invalid Task Number")
            except ValueError:
                print("Enter Valid Number")

    elif choice == "5":
        print("Exiting Task Manager...")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid Choice! Select (1-5)")