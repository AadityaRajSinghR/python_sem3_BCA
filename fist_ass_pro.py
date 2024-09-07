def calculate_average(assignments, exams, projects):

    # Assignments: 40%, Exams: 50%, Projects: 10%

    weight_assignments = 0.40
    weight_exams = 0.50
    weight_projects = 0.10
    
    average = (assignments * weight_assignments +
               exams * weight_exams +
               projects * weight_projects)
    return average

def final_grade_fun(average_grade):
   
    #Determine the final grade based on the weighted average.
   
    if 90 <= average_grade <= 100:
        return 'A'
    elif 80 <= average_grade < 90:
        return 'B'
    elif 65 <= average_grade < 80:
        return 'C'
    elif 50 <= average_grade < 65:
        return 'D'
    else:
        return 'F'

def main():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                print("The number of students must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    for _ in range(num_students):
        student_name = input("Enter Student Name : ")
        print(f"\nEntering data for student {student_name}:")

        while True:
            try:
                assignments = float(input("Enter the score for assignments (0-100): "))
                exams = float(input("Enter the score for exams (0-100): "))
                projects = float(input("Enter the score for projects (0-100): "))

                if not (0 <= assignments <= 100) or not (0 <= exams <= 100) or not (0 <= projects <= 100):
                    print("Scores must be between 0 and 100. Please enter again.")
                    continue
                
                break
            except ValueError:
                print("Invalid input. Please enter numerical values.")

        average_grade = calculate_average(assignments, exams, projects)
        final_grade = final_grade_fun(average_grade)

        print(f"\nStudent {student_name}:")
        print(f"Weighted Average: {average_grade:.2f}")
        print(f"Final Grade: {final_grade}")

if __name__ == "__main__":
    main()
