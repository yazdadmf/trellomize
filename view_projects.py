import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
projects_file_path = os.path.join(current_dir, "dataprojects.txt")

def list_all_projects():
    if not os.path.exists(projects_file_path):
        print("No projects have been saved yet.\n")
        time.sleep(0.5)
        return "empty"
    
    elif os.path.getsize(projects_file_path) == 0:
        print("No projects have been saved yet.\n")
        return "empty"
    
    projects = []
    with open(projects_file_path, "r") as file:
        project = {}
        for line in file:
            if line.strip() == "":
                if project:
                    projects.append(project)
                    project = {}
            else:
                parts = line.strip().split(": ", 1)
                if len(parts) == 2:
                    key, value = parts
                    project[key] = value
                else:
                    print(f"Skipping invalid line: {line.strip()}")
        if project:  
            projects.append(project)
    
    return projects

def display_project_details(project):
    for key, value in project.items():
        print(f"{key}: {value}")
    time.sleep(0.5)

def main():
    projects = list_all_projects()
    if projects != "empty":
        print("List of all projects:\n")
        time.sleep(0.5)
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project['Project Name']}")
        while True:
            project_choice = input("\nEnter the number of the project you want to view: ").strip()
            print("\n")
            if project_choice.isdigit() and 1 <= int(project_choice) <= len(projects):
                display_project_details(projects[int(project_choice) - 1])
                print("\n")
                break
            else:
                print("Invalid choice. Please enter a valid number.\n")
                time.sleep(0.5)

if __name__ == "__main__":
    main()