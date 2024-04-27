import os
import json
from datetime import datetime

class TaskManager:
    def __init__(self):
        directory = "logs"
        self.filename = directory + "/" + datetime.today().strftime("%Y-%m-%d") + "-log.json"
        self.tasks = []

        # setting up the directory
        if not os.path.isdir(directory):
            os.makedirs(directory)
            
        # setting up the log file
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                file.write("")

        # if log file exists
        self.load_from_json()

    def add(self,name):
        task = {"name": name, "is_completed": False}
        self.tasks.append(task)
        self.save_to_json()

    def done(self,name):
        for task in self.tasks:
            if task["name"] == name:
                task["is_completed"] = True

        self.save_to_json()

    def display(self):
        total_tasks = len(self.tasks)
        print("\nTotal tasks : \t",total_tasks)
        completed_tasks = sum(1 for task in self.tasks if task["is_completed"])
        if total_tasks  != 0:
            progress = int((completed_tasks / total_tasks) * 100)
        else:
            progress = 100

        # Display progress bar
        print("\nProgress : ")
        print(f"[{'=' * (progress // 10):<10}] {progress}%")

        # Print incomplete tasks
        print("\nIncomplete Tasks:")
        for task in self.tasks:
            if not task["is_completed"]:
                name = task["name"]
                print(f"[ ] {name}")

        # Print completed tasks
        print("\nCompleted Tasks:")
        for task in self.tasks:
            if task["is_completed"]:
                name = task["name"]
                print(f"[x] {name}")


    def save_to_json(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)

    def load_from_json(self):
        try:
            with open(self.filename,"r",encoding="utf-8") as file:
                    try:
                        data = json.load(file)
                        self.tasks = [task for task in data if isinstance(task, dict)]
                    except json.JSONDecodeError:
                        self.tasks = []
        except FileNotFoundError:
            print("The todo is empty")

    def reboot(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
