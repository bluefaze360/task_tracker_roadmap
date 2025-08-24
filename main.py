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

    
    #print("task: ", desc)

    if comm_list[0] == "add":
        desc = " ".join(comm_list[1:])
        task = {
            "id": 1,
            "description": desc, 
            "status": "to-do", 
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        

        print("Adding a task...")

        try:
            with open("tasks.json", "r+") as f:
                tasks = json.load(f)


                task["id"] = len(tasks["tasks"]) + 1  # Auto-increment ID
                
                tasks["tasks"].append(task)  # Add the new task to the list
                #tasks["tasks"].append(task)
                f.seek(0)  # Move the cursor to the beginning of the file

                json.dump(tasks, f, indent=4)
        except FileNotFoundError:
            with open("tasks.json", "w") as f:
                data = {"tasks": [task]}
                json.dump(data, f, indent=4)
            

        print("Task added successfully.")
        return
    
    elif comm_list[0] == "update":
        id = int(comm_list[1])
        desc = " ".join(comm_list[2:])
        with open("tasks.json", "r+") as f:
            tasks = json.load(f)

            for t in tasks["tasks"]:
                if t["id"] == id:
                    t["description"] = desc
                    t["updated_at"] = datetime.now().isoformat()
                    break

            f.seek(0)
            json.dump(tasks, f, indent=4)

        print("Updating a task...")
        return
    
    elif comm_list[0] == "delete":
        id = int(comm_list[1])
        with open("tasks.json", "r+") as f:
            tasks = json.load(f)

            tasks["tasks"] = [t for t in tasks["tasks"] if t["id"] != id]

            f.seek(0)
            f.truncate()
            json.dump(tasks, f, indent=4)

        print("Deleting a task...")

        with open("tasks.json", "r+") as f:
            tasks = json.load(f)

            for t in tasks["tasks"]:
                t["id"] = tasks["tasks"].index(t) + 1  # Reassign IDs

            f.seek(0)

            json.dump(tasks, f, indent=4)
        return
    
    elif comm_list[0] == "mark-in-progress":
        id = int(comm_list[1])

        with open("tasks.json", "r+") as f:
            tasks = json.load(f)

            for t in tasks["tasks"]:
                if t["id"] == id:
                    t["status"] = "in-progress"
                    t["updated_at"] = datetime.now().isoformat()
                    break

            f.seek(0)
            json.dump(tasks, f, indent=4)

        print("Marking task as in-progress...")
        return
    
    elif comm_list[0] == "mark-done":
        id = int(comm_list[1])

        with open("tasks.json", "r+") as f:
            tasks = json.load(f)

            for t in tasks["tasks"]:
                if t["id"] == id:
                    t["status"] = "done"
                    t["updated_at"] = datetime.now().isoformat()
                    break

            f.seek(0)
            json.dump(tasks, f, indent=4)

        print("Marking task as done...")
        return
    
    elif comm_list[0] == "list":
        print("Listing all tasks...")

        with open("tasks.json") as f:
            tasks = json.load(f)

            for i in tasks['tasks']:
                print(i)

        return
    
    elif comm_list[0] == "list-done":
        print("Listing all done tasks...")

        f = open("tasks.json", "r")
        data = json.load(f)
        print(*[t for t in data["tasks"] if t["status"] == "done"], sep="\n")

        f.close()

        return
    
    elif comm_list[0] == "list-in-progress":
        print("Listing all in-progress tasks...")

        f = open("tasks.json", "r")
        data = json.load(f)
        print(*[t for t in data["tasks"] if t["status"] == "in-progress"], sep="\n")

        f.close()

        return
    
    elif comm_list[0] == "list-todo":
        print("Listing all to-do tasks...")

        f = open("tasks.json", "r")
        data = json.load(f)
        print(*[t for t in data["tasks"] if t["status"] == "to-do"], sep="\n")

        f.close()
        

        
        return
      


if __name__ == "__main__":
    main()


# Function to append new data to JSON file
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'emp_details' list
        file_data["emp_details"].append(new_data)
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)
