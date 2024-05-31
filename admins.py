import os
import time
import history_of_changes

current_dir = os.path.dirname(os.path.abspath(__file__))
employees_file_path = os.path.join(current_dir, "Employees.txt")
projects_file_path = os.path.join(current_dir, "dataprojects.txt")

def print_usernames_from_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("employee username:"):
                username = line.split(": ")[1].strip()
                print(username)

def find_project_by_admin(file_path, admin_name):
    project_details = []
    in_project = False

    with open(file_path, 'r') as file:
        for line in file:
            if "Project admin: " + admin_name in line:
                in_project = True
            if in_project:
                project_details.append(line.strip())
            if "Budget:" in line:
                in_project = False
                if "Project admin: " + admin_name in project_details:
                    for detail in project_details:
                        print(detail)
                    return
                project_details = []

def remove_employee(username):
    with open(employees_file_path, "r") as file:
        lines = file.readlines()

    with open(employees_file_path, "w") as file:
        for line in lines:
            if "employee username: " + username not in line:
                file.write(line)
            else:
                next(file)  

    print(f"Employee {username} removed successfully.")

def display_admin_to_do_list(username):
    
    with open(projects_file_path, "r") as file:
        file_contents = file.read()
    if "asked" in file_contents:
        print("you had no works yet if you want just check the program details and your employees.")
    else:
        display_admin_to_do_list.asked = True
        with open(projects_file_path, "r") as file:
            project_name = None
            start_date = None
            end_date = None
            tasks = None
            for line in file:
                if "Project admin: " + username in line:
                    project_name = line.split(": ")[1].strip()
                elif line.startswith("Project Name:"):
                    project_name = line.split(": ")[1].strip()
                elif line.startswith("Start Date:"):
                    start_date = line.split(": ")[1].strip()
                elif line.startswith("End Date/Deadline:"):
                    end_date = line.split(": ")[1].strip()
                elif line.startswith("Tasks:"):
                    tasks = line.split(": ")[1].strip().split(", ")
                    break

        if project_name and start_date and end_date and tasks:
            print("You are an admin. Here are the details of the project:\n")
            find_project_by_admin(projects_file_path, username)
            print("-" * 50)
            print(f"{'Your Task':<25} {'Assigned Employees':<25} {'Priority':<10} {'Deadline':<10}")
            print("-" * 50)
            print("Here are all of the employees' usernames (+your username), please choose:")
            print_usernames_from_file(employees_file_path)
            
            task_assignments = []
            for task in tasks:
                assigned_employees = input(f"Enter employees for {task} (comma separated): ").strip()
                priority = input("Enter the priority for this task (critical, medium, high, low): ").strip().lower()
                while priority not in ["critical", "medium", "high", "low"]:
                    print("Invalid priority level. Please choose from critical, medium, high, low.")
                    priority = input("Enter the priority for this task (critical, medium, high, low): ").strip().lower()
                deadline = input(f"Enter the deadline for {task} (YYYY-MM-DD): ").strip()
                task_assignments.append((task, assigned_employees, priority, deadline))
        
            print("-" * 50)
            for task, employees, priority, deadline in task_assignments:
                print(f"{task:<25} {employees:<25} {priority:<10} {deadline:<10}")
            print("-" * 50)

            with open(projects_file_path, "a") as file:
                file.write("\nasked\n")
                file.write("\nemployees:\n")
                for task, employees, priority, deadline in task_assignments:
                    file.write(f"{employees} - {task} - {priority} - {deadline}\n")

def list_user_projects(username):
    print(f"Projects for {username}:")
    with open(projects_file_path, "r") as file:
        in_project = False
        project_details = []
        for line in file:
            if "Project Name:" in line:
                project_details = [line.strip()]
                in_project = True
            elif in_project:
                project_details.append(line.strip())
                if "Budget:" in line:
                    in_project = False
                    if f"Project admin: {username}" in project_details or any(f"{username}" in task for task in project_details if "Tasks:" in task):
                        for detail in project_details:
                            print(detail)
                        print("-" * 50)
                    project_details = []

def check_username(username):
    with open(employees_file_path, "r") as file:
        for line in file:
            if line.strip().startswith("employee username: " + username):
                if "admin" in line:
                    display_admin_to_do_list(username)
                    return

def main(username):
    while True:
        choice1 = int(input("What do you want to do admin:\n1. check my to do list\n2. check my projects\n3. history of changes\n4. Editing employees\n5. Exit\n"))
        if choice1 == 1:
            display_admin_to_do_list(username)
        elif choice1 == 2:
            list_user_projects(username)
        elif choice1 == 3:
            history_of_changes.check_folder_changes(history_of_changes.manage_folders())
        elif choice1 == 4:
            None
        elif choice1 == 5:
            print("Exiting...")
            time.sleep(0.5)
            exit()
        else:
            print("Invalid choice. Please try again.")
