import os

def load_tasks():
    if os.path.exists("task.txt"):
        with open("task.txt", "r") as f:
            tasks = f.readlines()
        tasks = [t.strip() for t in tasks]
        return tasks
    return []

def save_tasks(tasks):
    with open("task.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    save_tasks(tasks)
def view_task(tasks):
    if len(tasks) == 0:
        print("No Task Found.")
    else: 
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}") 
def delete_task(tasks):
    view_task(tasks)
    num = int(input("Konsa task delete karna hai? (number likho): "))
    removed = tasks.pop(num - 1)  # list 0 se shuru hoti hai
    save_tasks(tasks)
    print(f"'{removed}' delete ho gaya!")
def main():
    tasks = load_tasks()  # start mein tasks load karo
    
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Task Add karo")
        print("2. Tasks Dekho")
        print("3. Task Delete karo")
        print("4. Bahar jao")
        
        choice = input("Option chuno (1-4): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Khuda Hafiz! 👋")
            break
        else:
            print("Galat option! Dobara try karo.")

main()
     