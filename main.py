import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


tasks=[]
while True:
    clear()
    print("1 - Add Tasks")
    print("2 - List Tasks")
    print("0 - Exit")

    op = input("Choose: ")

    if op=="1":
        task=input("\nTask: ")
        tasks.append(task)
        print("Task added!")
        input("\nPress Enter to continue...")


    elif op=="2":
        clear()
        print("--- Task List ---")
        for i in range(len(tasks)):
            print(i+1, "-", tasks[i])
        input("\nPress Enter to continue...")

    elif op=="0":
        break
    else:
        print("\nInvalid command.")
        input("Press Enter to continue...")