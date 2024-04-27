'''This python file contains commands to be executed in the command line'''

import argparse
from todo import tasks

task_manager = tasks.TaskManager()

def add(task_name):
    task_manager.add(task_name)
    print(f"Added task: {task_name}")

def done(task_name):
    task_manager.done(task_name)
    print(f"Marked task '{task_name}' as completed.")

def main():
    parser = argparse.ArgumentParser(description="Todo CLI")
    parser.add_argument("command", choices=["add", "done", "display","reboot"])
    parser.add_argument("task_name", nargs="?", default=None)

    args = parser.parse_args()

    if args.command == "add":
        add(args.task_name)
    elif args.command == "done":
        done(args.task_name)
    elif args.command == "display":
        task_manager.load_from_json()
        task_manager.display()
    elif args.command == "reboot":
        task_manager.reboot()

if __name__ == "__main__":
    main()

