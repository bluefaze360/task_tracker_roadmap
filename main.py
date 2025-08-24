"""
Task Tracker CLI Application
Copyright (c) 2025 Lance Wilson. All rights reserved.


This application allows users to manage their tasks via command-line interface.

"""









import json
from datetime import datetime

def main():


    comm = input("Enter a task: ")

    comm_list = comm.split(" ")
    #print("debug: ", comm_list)

    desc = " ".join(comm_list[1:])
    #print("task: ", desc)

    if comm_list[0] == "add":
        task = {
            "id": 1,
            "description": desc, 
            "status": "to-do", 
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()}
        
        

        print("Adding a task...")

        tasks = add_json(task)

        print("Task added successfully with ID ", tasks["id"])
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

        print("All tasks info", tasks)
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
    
    
def add_json(task):
    try:
        with open("tasks.json") as f:
            tasks = json.load(f)

            tasks["tasks"].append(task)

            tasks["tasks"]["id"] = len(tasks["tasks"]) + 1

            json.dump(tasks, f, indent=4)
            
            return tasks
    except FileNotFoundError:
        task_list = {"tasks": [task]}

        return task_list
    except json.JSONDecodeError:
        return []
    


if __name__ == "__main__":
    main()


# Function to append new data to JSON file
def write_json(new_data, filename='data.json'):
    with open(filename, 'w') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'emp_details' list
        file_data["emp_details"].append(new_data)

        file_data["emp_details"]["id"] = len(file_data["emp_details"]) + 1
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)
