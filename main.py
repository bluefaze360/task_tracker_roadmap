"""
Task Tracker CLI Application
Copyright (c) 2025 Lance Wilson. All rights reserved.


This application allows users to manage their tasks via command-line interface.

"""









import json
from datetime import datetime

def main():

    tasks = init_tracker()


    comm = input("Enter a task: ")

    comm_list = comm.split(" ")
    #print("debug: ", comm_list)

    desc = " ".join(comm_list[1:])
    #print("task: ", desc)

    if comm_list[0] == "add":
        tasks.append({
            "id": len(tasks) + 1,
            "description": desc, 
            "status": "to-do", 
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()})

        print("Adding a task...")
        print("Task info", tasks)
        return
    
    elif comm_list[0] == "update":
        tasks[len(tasks) - 1]["description"] = desc
        tasks[len(tasks) - 1]["updated_at"] = datetime.now().isoformat()
        print("Updating a task...")
        return
    
    elif comm_list[0] == "delete":
        print("Deleting a task...")
        return
    
    elif comm_list[0] == "mark-in-progress":
        print("Marking task as in-progress...")
        return
    
    elif comm_list[0] == "mark-done":
        print("Marking task as done...")
        return
    
    elif comm_list[0] == "list":
        print("Listing all tasks...")
        return
    
    elif comm_list[0] == "list-done":
        print("Listing all done tasks...")
        return
    
    elif comm_list[0] == "list-in-progress":
        print("Listing all in-progress tasks...")
        return
    
    elif comm_list[0] == "list-todo":
        print("Listing all to-do tasks...")
        return
    
    
def init_tracker():
    tasks = []

    return tasks

if __name__ == "__main__":
    main()


