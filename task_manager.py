import json
def load_tasks():
    try:
        with open("tasks.json","r") as f:
            return json.load(f)
    except:
        return []
def save_tasks(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f)
def add_tasks(tasks):
    task_name=input("Enter your Task Name: ")
    tasks.append({
            "task":task_name,
            "status":"pending"
            })
def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for i,task in enumerate(tasks,start=1):
            print(i,".",f"{task['task']} [{task['status']}]")
def mark_complete(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for i,task in enumerate(tasks,start=1):
            print(i,".",task["task"])
        try:
            index=int(input("Enter task number to complete:"))
        except:
            print("Invalid input!")
            return 
        if 1<=index<=len(tasks):
            tasks[index-1]["status"]="completed"
            print("Task marked as completed")
        else:
            print("Invalid task number")
def delete_task(tasks):
    if not tasks:
        print("No tasks are available to delete")
    else:
        for i,task in enumerate(tasks,start=1):
            print(i,".",task["task"])
        try:
            index=int(input("Enter task number to delete:"))
        except:
            print("Invalid input!")
            return
        if 1<=index<=len(tasks):
            tasks.pop(index-1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number")
def main_task():
    tasks=load_tasks()
    while True:
        print("1.Add Task")
        print("2.View Tasks")
        print("3.Mark Task Complete")
        print("4.Delete Task")
        print("5.Save & Exit")
        choice=input("Enter your choice: ")
        if choice=="5":
            save_tasks(tasks)
            print("Saving and Exiting...")
            break
        if choice in ["1","2","3","4"]:
            if choice=="1":
                add_tasks(tasks)
            elif choice=="2":
                view_tasks(tasks)
            elif choice=="3":
                mark_complete(tasks)
            elif choice=="4":
                delete_task(tasks)
        else:
            print("Invalid choice")
main_task()