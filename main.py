import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


tasks=[]
while True:
    clear()
    print("--- Task Manager ---")
    print("1 - Add Tasks")
    print("2 - List Tasks")
    print("3 - Mark As Done")
    print("0 - Exit")

    op = input("\nChoose: ")

    if op=="1":
        task=input("\nTask: ")
        tasks.append([task, False])
        print("Task added!")
        input("\nPress Enter to continue...")


    elif op=="2":
        clear()
        print("--- Task List ---")
        for i in range(len(tasks)):
            if tasks[i][1] == True:
                status = "[X]"
            else:
                status = "[ ]"
            print(i+1, "-", tasks[i][0], status)
        input("\nPress Enter to continue...")

    elif op=="3":
        clear()
        print("--- Task List ---")
        for i in range(len(tasks)):
            if tasks[i][1] == True:
                status = "[X]"
            else:
                status = "[ ]"
            print(i+1, "-", tasks[i][0], status)
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
       

    elif op=="0":
        break
    else:
        print("\nInvalid command.")
        input("Press Enter to continue...")