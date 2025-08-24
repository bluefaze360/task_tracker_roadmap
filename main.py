"""
Task Tracker CLI Application
Copyright (c) 2025 Lance Wilson. All rights reserved.


This application allows users to manage their tasks via command-line interface.

"""









import json

def main():
    comm = input("Enter a task: ")
    comm_list = comm.split(" ")
    if comm_list[0] == "add":
        print("Adding a task...")
        return
    elif comm_list[0] == "update":
        print("Updating a task...")
        return
    elif comm_list[0] == "delete":
        print("Deleting a task...")
        return
    

if __name__ == "__main__":
    main()



