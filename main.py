import manager
import Employees
import time

while True:
    choice = int(input("1.Managers\n2.Employees\n"))
    time.sleep(0.5)
    if choice == 1:
        manager.manage_managers()
        break
    elif choice == 2:
        Employees.manage_employees()
        break
    else:
        print("\nInvalid choice. Please try again.\n")
        time.sleep(0.5)