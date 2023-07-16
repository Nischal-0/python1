import os


class Assignment:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False


class AssignmentManager:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def list_assignments(self):
        for index, assignment in enumerate(self.assignments):
            status = "Completed" if assignment.completed else "Pending"
            print(f"{index + 1}. {assignment.name} (Due: {assignment.due_date}) - {status}")

    def complete_assignment(self, index):
        if index >= 1 and index <= len(self.assignments):
            assignment = self.assignments[index - 1]
            assignment.completed = True
            print(f"Assignment '{assignment.name}' marked as completed.")
        else:
            print("Invalid assignment index.")

    def save_assignments(self, filename):
        with open(filename, "w") as file:
            for assignment in self.assignments:
                file.write(f"{assignment.name},{assignment.due_date},{assignment.completed}\n")

    def load_assignments(self, filename):
        if not os.path.exists(filename):
            print("File does not exist.")
            return

        self.assignments.clear()
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                name = parts[0]
                due_date = parts[1]
                completed = parts[2] == "True"
                assignment = Assignment(name, due_date)
                assignment.completed = completed
                self.assignments.append(assignment)


def main():
    assignment_manager = AssignmentManager()

    while True:
        print("\nAssignment Management System")
        print("1. Add assignment")
        print("2. List assignments")
        print("3. Complete assignment")
        print("4. Save assignments to file")
        print("5. Load assignments from file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter assignment name: ")
            due_date = input("Enter due date: ")
            assignment = Assignment(name, due_date)
            assignment_manager.add_assignment(assignment)
            print("Assignment added successfully.")

        elif choice == "2":
            print("\nAssignments:")
            assignment_manager.list_assignments()

        elif choice == "3":
            index = int(input("Enter the index of the assignment to complete: "))
            assignment_manager.complete_assignment(index)
            
        elif choice == "4":
            filename = input("Enter the filename to save assignments: ")
            assignment_manager.save_assignments(filename)
            print("Assignments saved successfully.")
            
        elif choice == "5":
            filename = input("Enter the filename to load assignments: ")
            assignment_manager.load_assignments(filename)
            print("Assignments loaded successfully.")

        elif choice == "6":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
