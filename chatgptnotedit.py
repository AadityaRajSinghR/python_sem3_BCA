class AssessmentComponent:
    def __init__(self, name, weightage, max_marks):
        self.name = name
        self.weightage = weightage
        self.max_marks = max_marks
        self.obtained_marks = 0

    def input_marks(self):
        while True:
            try:
                self.obtained_marks = float(input(f"Enter obtained marks for {self.name} (out of {self.max_marks}): "))
                if 0 <= self.obtained_marks <= self.max_marks:
                    break
                else:
                    print(f"Please enter marks between 0 and {self.max_marks}.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def calculate_weighted_score(self):
        return (self.obtained_marks / self.max_marks) * self.weightage


def get_component_details():
    name = input("Enter the name of the component (e.g., Exam, Jury, Assignments, etc.): ")
    while True:
        try:
            weightage = float(input(f"Enter the weightage for {name} (in %): "))
            max_marks = float(input(f"Enter the maximum marks for {name}: "))
            if weightage >= 0 and max_marks > 0:
                break
            else:
                print("Please enter valid positive values for weightage and marks.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    return AssessmentComponent(name, weightage, max_marks)


def main():
    print("Student Grade Evaluation Program")
    components = []
    total_weightage = 0

    # Input components details
    while True:
        component = get_component_details()
        components.append(component)
        total_weightage += component.weightage
        add_more = input("Do you want to add another component? (yes/no): ").lower()
        if add_more != 'yes':
            break

    # Ensure the total weightage is 100%
    if total_weightage != 100:
        print(f"Total weightage is {total_weightage}%, which is not equal to 100%. Please restart the program and enter correct weightages.")
        return

    # Input obtained marks for each component
    for component in components:
        component.input_marks()

    # Calculate final grade
    final_score = sum([component.calculate_weighted_score() for component in components])

    print(f"\nFinal Grade Evaluation:")
    for component in components:
        print(f"{component.name} -> Obtained Marks: {component.obtained_marks}/{component.max_marks}, Weighted Score: {component.calculate_weighted_score():.2f}%")

    print(f"\nTotal Weighted Score: {final_score:.2f}%")

if __name__ == "__main__":
    main()
