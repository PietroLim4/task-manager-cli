import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_tasks():
    print("--- Task List ---")
    for i in range(len(tasks)):
        status = "[X]" if tasks[i][1] else "[ ]"
        print(i+1, "-", tasks[i][0], status)
    if len(tasks) == 0:
        print("No tasks yet.")
tasks=[]

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            text, status = line.strip().split("|")
            tasks.append([text, status == "True"])

while True:
    clear()
    print("--- Task Manager ---")
    print("1 - Add Tasks")
    print("2 - List Tasks")
    print("3 - Toggle Task")
    print("4 - Remove Task")
    print("0 - Exit")

    op = input("\nChoose: ")

    if op=="1":
        task=input("\nTask: ")
        tasks.append([task, False])
        print("Task added!")
        input("\nPress Enter to continue...")


    elif op=="2":
        clear()
        show_tasks()
        input("\nPress Enter to continue...")

    elif op=="3":
        clear()
        show_tasks()
        try:
            cho = int(input("Choose a task to mark/desmark: "))

            if 1 <= cho <= len(tasks):
                tasks[cho-1][1] = not tasks[cho-1][1]
                print("\nChange done.")
            else:
                print("\nTask does not exist")

        except:
            print("\nInvalid input")
        input("\nPress Enter to continue...")

    elif op=="4":
        clear()
        show_tasks()
        try:
            cho = int(input("Choose a task to remove: "))

            if 1 <= cho <= len(tasks):
                removed = tasks.pop(cho-1)
                print(f"\nRemoved: {removed[0]}")
            else:
                print("\nTask does not exist")

        except:
            print("\nInvalid input")
        input("\nPress Enter to continue...")
       

    elif op=="0":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task[0] + "|" + str(task[1]) + "\n")
        break
    else:
        print("\nInvalid command.")
        input("Press Enter to continue...")