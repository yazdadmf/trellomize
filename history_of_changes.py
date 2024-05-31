import os
import manager_accessablty


current_dir = os.path.dirname(os.path.abspath(__file__))
projects_file_path = os.path.join(current_dir, "dataprojects.txt")

def manage_folders():
    folder_path = r"C:\Users\A_S\OneDrive\Desktop\projects"
    folder_names = get_folder_names(folder_path)

    print("projects:")
    for i, folder_name in enumerate(folder_names):
        print(f"{i+1}. {folder_name}")

    choice = int(input("Enter the number of the folder you want to see changes: "))
    if 1 <= choice <= len(folder_names):
        chosen_folder_name = folder_names[choice - 1]
        chosen_folder_path = os.path.join(folder_path, chosen_folder_name)
        return chosen_folder_path
    else:
        print("Invalid choice.")

def get_folder_names(folder_path):
    return [os.path.basename(folder) for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]


def create_backup(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path + '.bak', 'w') as bak_file:
        bak_file.writelines(lines)

def check_folder_changes(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    modified_files = []
    unmodified_files = []
    reported_files = set()  # Set to store files that have been reported as modified

    for file in txt_files:
        file_path = os.path.join(folder_path, file)
        if os.path.exists(file_path + '.bak'):
            with open(file_path, 'r') as file, open(file_path + '.bak', 'r') as bak_file:
                lines = file.readlines()
                bak_lines = bak_file.readlines()
                num_lines = len(lines)
                bak_num_lines = len(bak_lines)

            if num_lines != bak_num_lines and file not in reported_files:
                modified_files.append(f"{str(file)} {str(file).split('.')[0]} has changed")
                reported_files.add(file)  # Add the file to reported_files
                with open(projects_file_path, "r") as file:
                    lines = file.readlines()
                    manager_accessablty.update_condition(projects_file_path,"DOING")
            else:
                unmodified_files.append(f"{str(file)} hasn't changed yet")
        else:
            unmodified_files.append(f"{file} {file.split('.')[0]} hasn't changed yet")
            create_backup(file_path)  # Create a backup for files without a backup

    print("Modified files:")
    for file in modified_files:
        print(file)

    print("\nUnmodified files:")
    for file in unmodified_files:
        print(file)

    choice = input("\nDo you want to check a specific text file? (y/n) ")
    if choice.lower() == 'y':
        txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        print("Available text files:")
        for i, file in enumerate(txt_files):
            print(f"{i+1}. {file}")
        choice = int(input("Enter the number of the text file you want to choose: "))
        chosen_file = txt_files[choice - 1]

        with open(os.path.join(folder_path, chosen_file), 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)

        if os.path.exists(os.path.join(folder_path, chosen_file) + '.bak'):
            with open(os.path.join(folder_path, chosen_file) + '.bak', 'r') as bak_file:
                bak_lines = bak_file.readlines()
                bak_num_lines = len(bak_lines)

            if num_lines != bak_num_lines:
                print(f"The file {chosen_file} has changed from {bak_num_lines} lines to {num_lines} lines. If you want to see the details of this program changes you can hold shift and click on that file path.")
                if f"{str(chosen_file)} {str(chosen_file).split('.')[0]} has changed" in modified_files:
                    modified_files.remove(f"{str(chosen_file)} {str(chosen_file).split('.')[0]} has changed")  # Remove the file from modified_files
                    unmodified_files.append(f"{str(chosen_file)} hasn't changed yet")  # Add the file to unmodified_files
            else:
                print(f"The file {chosen_file} hasn't changed.")

        else:
            print(f"The file {chosen_file} has no backup, so it's not possible to check for changes.")