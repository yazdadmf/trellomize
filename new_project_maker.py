import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
employees_file_path = os.path.join(current_dir, "Employees.txt")
projects_file_path = os.path.join(current_dir, "dataprojects.txt")

def add_admin_to_username(username, project_name, file_path):
    with open(file_path, "r+") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            if lines[i].strip() == "employee username: " + username:
                lines[i] = "employee username: " + username + " admin: " + project_name
        file.seek(0)
        file.writelines(lines)
        file.truncate()

def print_usernames_from_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("employee username:"):
                username = line.split(": ")[1].strip()
                print(username)

def get_project_details():
    project_details = {}
    project_details["Project Manager"] = input("Enter the Project Manager's Name: ").strip() + "\n"
    project_details["Project Name"] = input("Enter the Project Name: ").strip() + "\n"
    project_details["Project Description"] = input("Enter the Project Description: ").strip() + "\n"
    print("Enter the Project admin's username (You can see all employees usernames In the list below):")
    print_usernames_from_file(employees_file_path)
    project_admin = input().strip()
    project_details["Project admin"] = project_admin + "\n"
    add_admin_to_username(project_admin, project_details["Project Name"], employees_file_path)
    project_details["Start Date"] = input("Enter the Start Date (YYYY-MM-DD): ").strip() + "\n"
    project_details["End Date/Deadline"] = input("Enter the End Date/Deadline (YYYY-MM-DD): ").strip() + "\n"
    project_details["Tasks"] = input("Enter the Tasks (separated by commas): ").strip() + "\n"
    project_details["Budget"] = input("Enter the Budget: ").strip() + "\n"
    project_details["(condition: BACKLOG)"] = "\n"

    return project_details

def save_project_details(project_details):
    project_name = project_details["Project Name"].strip()
    project_folder_path = os.path.join("C:\\Users\\A_S\\OneDrive\\Desktop\\projects", project_name)
    os.makedirs(project_folder_path, exist_ok=True)

    with open(os.path.join(project_folder_path, "project_details.txt"), "w") as file:
        for key, value in project_details.items():
            file.write(f"{key}: {value.strip()}\n")
    
    with open(os.path.join(project_folder_path, "project_details.txt"), "w") as file:
        file.write(f"\n")

    with open(os.path.join(projects_file_path), "w") as file:
        for key, value in project_details.items():
            file.write(f"{key}: {value.strip()}\n")

    tasks = project_details["Tasks"].strip().split(", ")
    for task in tasks:
        with open(os.path.join(project_folder_path, f"{task.strip()}.txt"), "w") as file:
            file.write(f"Task: {task.strip()}\n")
            file.write("(condition: BACKLOG)\n")

    with open(os.path.join(project_folder_path, "tasks.txt"), "a") as tasks_file:
        tasks_file.write("comments:\n")
        tasks_file.write("(please provide your idea about this project and the admin)\n")

    with open(projects_file_path, "a") as projects_file:
        for key, value in project_details.items():
            if key != "Tasks":
                projects_file.write(f"{key}: {value.strip()}\n")
        projects_file.write("(condition: BACKLOG)\n")
        projects_file.write("\n")

    time.sleep(0.5)

def main():
    print("You have chosen to create a new project.\n")
    time.sleep(0.5)
    project_details = get_project_details()
    save_project_details(project_details)
    print("Project details have been saved.\n")
    time.sleep(0.5)

if __name__ == "__main__":
    main()
