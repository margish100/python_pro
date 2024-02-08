class Employee:
    "employee of the list"
    def __init__(self, employee_id, name, title, department):
        self.employee_id = employee_id
        self.name = name
        self.title = title
        self.department = department

    def show_details(self):
        print(f"ID: {self.employee_id}, Name: {self.name}, Title: {self.title}, Department: {self.department}")

    def __repr__(self):
        return f"{self.name} [ID: {self.employee_id}]"


class Department:
    """Represents a department within the company."""
    def __init__(self, name):
        self.name = name
        self.employees = []  # Corrected from 'self.emloyees' to 'self.employees'

    def add(self, employee):
        """Adds an employee to the department."""
        self.employees.append(employee)

    def remove(self, employee_id):
        """Removes an employee from the department by their ID."""
        
        #original_count = len(self.employees)
        self.employees = [e for e in self.employees if e.employee_id != employee_id]
        
        #if len(self.employees) == original_count:
            #print(f"No employee found with ID {employee_id} in department{self.name}.")
        

    def display(self):
        """Displays all employees within the department."""
        print(f"Department: {self.name}")
        for emp in self.employees:
            emp.show_details()



class CompanyStructure:
    def __init__(self):
        self.depts = {}

    def add_dept(self, name):
        if name in self.depts:
            print('department already exists')
        else:
            self.depts[name] = Department(name)

    def remove_dept(self, name):
        if name in self.depts:
            del self.depts[name]
        else:
            print('department not found')

    def show_depts(self):
        for dept in self.depts.values():
            dept.display()


def menu():
    print("\n--- employe portal list ---")
    print("1: Add an employee")
    print("2: Remove an employee")
    print("3: Show a department's employees")
    print("4: Create a department")
    print("5: Delete a department")
    print("6: Quit")

def run_system():
    system = CompanyStructure()
    while True:
        menu()
        choice = input("select option: ")
        try:

            if choice == "1":
                dept_name = input("department name: ")
                if dept_name in system.depts:
                    employee_id = input("employee ID: ")
                    name = input("employee name: ")
                    title = input("employee title: ")
                    system.depts[dept_name].add(Employee(employee_id, name, title, dept_name))
                else:
                    print("department does not exist.")

            elif choice == "2":
                dept_name = input("department name: ").strip()
                if dept_name in system.depts:
                    employee_id = input("employee ID to remove: ").strip()
                    
                    system.depts[dept_name].remove(employee_id)
                    2

                else:
                    print("department does not exist.")

            elif choice == "3":
                dept_name = input("department name: ")
                if dept_name in system.depts:
                    system.depts[dept_name].display()
                else:
                    print("department does not exist.")

            elif choice == "4":
                dept_name = input("new department name: ")
                system.add_dept(dept_name)

            elif choice == "5":
                dept_name = input("department name is delete: ")

                system.remove_dept(dept_name)
            elif choice == "6":
                print("exiting system.")
                break
            else:
                print("invalid option")
        except Exception as e:
            print(f"error read: {e}")


if __name__ == "__main__":
    run_system()
