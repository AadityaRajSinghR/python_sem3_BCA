# Student Grades Calculator App

from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)  # Automatically reset color to default after each print

# Initialize global variables
criteriadic = {}
TOTAL_WEIGHTAGE = 100
TOTAL_cce_WEIGHTAGE = 100
TOTAL_cce=0
weightage_list = {}

#-------------------------------------------------#
#---------| Add Criteria Function Start |---------#
#-------------------------------------------------#

# Function to confirm user action
def confirm_action(op):
    """Confirm user action."""
    return input(Fore.MAGENTA + f"Do you want to add {op}? Y/N : " + Style.RESET_ALL).upper()

# Function to add weightage to criteria It is main function of add criteria
def add_criteria():
    """Main function to handle user inputs for criteria and weightage."""
    global TOTAL_WEIGHTAGE ,TOTAL_cce_WEIGHTAGE ,TOTAL_WEIGHTAGE, criteriadic
    cont = ""
    while True:
        # Exam Details
        print(Fore.CYAN + "\n--------| Enter Some Exam Details |--------\n")
        if confirm_action("Exam") == "Y":
            add_weightage("Exam")
         
        # Jury Details
        print(Fore.CYAN + "\n--------| Enter Some Jury Details |--------\n")
        if confirm_action("Jury") == "Y":
            add_weightage("Jury")
                
        # Continuous and Comprehensive Evaluation (CCE) Details
        print(Fore.CYAN + "\n--------| Enter Some Continuous and Comprehensive Evaluation (CCE) Details |--------\n")
        handle_cce_details()
        
        display_criteria()
        cont = input(Fore.YELLOW + "Do you want to Update Criteria's? Y/N : ").upper()
        if cont == "N":
            print(Fore.MAGENTA + "Thank you for using the app!")
            break
        elif cont == "Y":
            criteriadic = {}
            TOTAL_WEIGHTAGE = 100
            TOTAL_cce_WEIGHTAGE = 100
        elif cont != "Y" or cont != "N":
            print(Fore.RED + "Please enter a valid option.")

# Function to add weightage and marks for a specific category
def add_weightage(category):
    """Add weightage and marks for a specific category."""
    global TOTAL_WEIGHTAGE
    
    
    while True:
        print("\nTotal Remaining weightage: ", TOTAL_WEIGHTAGE, "%\n")
        try:
            
                
            weightage = float(input(f"How many {category} weightages do you want to add? : "))
            if weightage < 0:
                print(f"Total weightage of {category} cannot be less than 0%")
                continue
            
            if weightage > TOTAL_WEIGHTAGE:
                print(f"Total weightage of {category} cannot be greater than {TOTAL_WEIGHTAGE}%")
                continue
                
            TOTAL_WEIGHTAGE -= weightage
            marks = float(input(f"How many {category} marks do you want to add? : "))
            criteriadic[category] = {"weightage": weightage, "marks": marks}
            weightage_list[category] = weightage / 100
            break
        except ValueError:
            print("Please enter a valid number")

#Handle CCE details and activities.
def handle_cce_details():
    global TOTAL_cce_WEIGHTAGE, TOTAL_WEIGHTAGE
    
    weightage = TOTAL_WEIGHTAGE
    if "CCE" not in criteriadic:
        criteriadic["CCE"] = {}
        
    criteriadic["CCE"]["weightage"] = weightage
    weightage_list["CCE"] = weightage / 100
    TOTAL_WEIGHTAGE = 0  # No weightage left for other categories after CCE
    
    print(Fore.RED +"\nTotal Remaining CCE weightage: ", TOTAL_cce_WEIGHTAGE, "%\n")
    add_cce_activities()
    #
    if TOTAL_cce_WEIGHTAGE != 0:
        print(Fore.RED + Style.BRIGHT + "\n\nPlease adjust the criteria to ensure the CCE weightage totals 100%.\n")
        TOTAL_cce_WEIGHTAGE = 100
        handle_cce_details()  # Restart the CCE entry process

#Add CCE activities and their weightage.
def add_cce_activities():
    # add all CCE activity in Array
    cce_activities = ["assignments", "projects", "quizzes", "value added courses", "practical tests", "attendance", "other activities"]
    
    for activity in cce_activities:
        if TOTAL_cce_WEIGHTAGE == 0:
            print("You have reached the maximum CCE weightage. No more activities can be added.")
            return
        
        if confirm_action(activity.capitalize()) == "Y":
            if activity == "attendance":
                add_attendance()
            else:
                while True:
                    try:
                        num = int(input(f"How many {activity} do you want to add? : "))
                        get_values(activity.capitalize(), num)
                        break
                    except ValueError:
                        print("Please enter a valid number")


#Add attendance weightage and marks.
def add_attendance():
    global TOTAL_cce_WEIGHTAGE
    if "Attendance" not in criteriadic["CCE"]:
        criteriadic["CCE"]["Attendance"] = {}
    while True:
        try:
            weightage = float(input("\tEnter Attendance Weightage: "))
            if weightage > TOTAL_cce_WEIGHTAGE:
                print(Fore.RED + f"Attendance weightage cannot be greater than the remaining CCE weightage: {TOTAL_cce_WEIGHTAGE}%")
                continue
            if weightage < 0:
                print(Fore.RED + "Attendance weightage cannot be negative.")
            criteriadic["CCE"]["Attendance"]["Attendance1"] = {"weightage": weightage, "marks": 100}
            TOTAL_cce_WEIGHTAGE -= weightage
            break
        except ValueError:
            print(Fore.RED +"Please enter a valid number" + Style.RESET_ALL)

#Get values for each activity.
def get_values(name, num):
    
    global TOTAL_cce_WEIGHTAGE , TOTAL_cce # Get Global Variables for edit
    
    # Check Ensure 'CCE' key exists
    if "CCE" not in criteriadic:
        criteriadic["CCE"] = {}
    
    # Ensure the 'name' key exists within 'CCE'
    if name not in criteriadic["CCE"]:
        criteriadic["CCE"][name] = {}
        
    for i in range(num):
        
        # Get {name} details
        while True:  # Keep asking until a valid name is provided
            name_name = input(Style.RESET_ALL + f"\tEnter name for {name} {i+1}: ")
            if name_name == "":
                print(Fore.RED + "\nName cannot be empty." + Style.RESET_ALL)
            else:
                break  # Exit the loop when a valid name is entered
        
        while True:
            try:
                    
                weightage = float(input("\tEnter Weightage: "))
                TOTAL_cce += weightage
                if weightage > TOTAL_cce_WEIGHTAGE:
                    print(f"\n{name_name} weightage cannot be greater than {TOTAL_cce_WEIGHTAGE}%\n")
                    continue
                elif weightage<0:
                    print(f"\n{name_name} weightage cannot be less than 0%\n")
                    continue
                    
                
                TOTAL_cce_WEIGHTAGE -= weightage
                marks = float(input("\tEnter Marks: "))
                if marks < 0:
                    print(f"\n{name_name} marks cannot be less than 0%\n")
                    continue
                
                # If all inputs are valid, update global values
                criteriadic["CCE"][name][name_name] = {"weightage": weightage, "marks": marks}
                print(Fore.RED + "\nTotal Remaining CCE weightage: ", TOTAL_cce_WEIGHTAGE, "%\n" + Style.RESET_ALL)
                break
                
            except ValueError:
                print("Please enter a valid number")


#Display the criteria in a formatted table
def display_criteria():
    table = []

    # Iterate through the main categories in the criteriadic
    for category, values in criteriadic.items():
        if category in ["Exam", "Jury"]:
            # Directly add Exam and Jury data
            table.append([category, "", "", values["weightage"], values["marks"]])
            
        elif category == "CCE":
            # Handle CCE and its sub-components dynamically
            table.append([category, "", "", values["weightage"], ""])
            
            for sub_category, sub_values in values.items():
                # isinstance is used to check if the object is a dictionary 
                # It is Prebuild Function
                if isinstance(sub_values, dict): 
                    
                    # Iterate through subcategories within CCE
                    for detail, detail_values in sub_values.items():
                        if isinstance(detail_values, dict):
                            # Add details (like assignments, projects, etc.)
                            table.append(["", sub_category, detail, detail_values["weightage"], detail_values["marks"]])

    # Print the table using tabulate
    headers = [Fore.GREEN + header + Style.RESET_ALL for header in ["Category", "Subcategory", "Details", "Weightage", "Marks"]]
    
    # Print the formatted table with colored headers
    print(tabulate(table, headers=headers, tablefmt="grid"))



# print(Fore.GREEN + f"Weightage list: {weightage_list}")


#-------------------------------------------------#
#----------| Add Criteria Function End |----------#
#-------------------------------------------------#



#-------------------------------------------------#
#-----| Assign values to students fun Start |-----#
#-------------------------------------------------#

def Student_evaluation():
    # Collect student details
    if criteriadic == {}:
        print(Fore.RED + "Criteriadic is empty. Please add some criteria first.")
        return
    
    
    st_Name = input(Fore.GREEN + "Enter Student Name: " + Style.RESET_ALL).upper()
    st_Env_No = input(Fore.GREEN + "Enter Enrollment Number: " + Style.RESET_ALL).upper()
    
    table = []
    total_score = 0
    total_weighted_score = 0

    
    # Iterate through the main categories in the criteriadic
    for category, values in criteriadic.items():
        if category in ["Exam", "Jury"]:
            while True:
                try:
                    # Ask for the student's score for Exam or Jury
                    student_score = float(input(f"Enter score for {category} from (0 - {values['marks']}): "))
                    if student_score < 0 or student_score > values["marks"]:
                        print(f"Invalid score. Please enter a value between 0 and {values['marks']}.")
                        continue
                    
                    weighted_score = (student_score / values["marks"]) * values["weightage"]
                    total_score += weighted_score  # Add weighted score directly
                    total_weighted_score += values["weightage"]  # Track the total weightage covered

                    # Add Exam and Jury data to the table
                    table.append([category, "", "", values["weightage"], values["marks"], student_score, weighted_score])
                    break  # Exit the loop after a valid input
                except ValueError:
                    print("Please enter a valid number.")

        elif category == "CCE":
            # Handle CCE and its sub-components dynamically
            cce_total_score = 0
            cce_max_marks = 0

            for sub_category, sub_values in values.items():
                if isinstance(sub_values, dict): 
                    # Iterate through subcategories within CCE
                    for detail, detail_values in sub_values.items():
                        if isinstance(detail_values, dict):
                            while True:
                                try:
                                    # Ask for the student's score for each detail (e.g., assignments, projects, etc.)
                                    student_score = float(input(f"Enter score for {detail} from (0 - {detail_values['marks']}): "))
                                    if student_score < 0 or student_score > detail_values["marks"]:
                                        print(f"Invalid score. Please enter a value between 0 and {detail_values['marks']}.")
                                        continue

                                    weighted_score = (student_score / detail_values["marks"]) * detail_values["weightage"]
                                    cce_total_score += weighted_score  # Add up all CCE weighted scores
                                    cce_max_marks += detail_values["weightage"]  # Sum up the total weightage for CCE

                                    # Add details (like assignments, projects, etc.) to the table
                                    table.append(["", sub_category, detail, detail_values["weightage"], detail_values["marks"], student_score])
                                    break  # Exit the loop after a valid input
                                except ValueError:
                                    print("Please enter a valid number.")

            # Now apply the CCE weightage to the accumulated score
            cce_final_score = (cce_total_score / cce_max_marks) * values["weightage"] if cce_max_marks > 0 else 0
            total_score += cce_final_score
            total_weighted_score += values["weightage"]

            # Add the CCE summary row to the table
            table.append([category, "", "Total CCE", values["weightage"], "100", cce_total_score, cce_final_score,weighted_score])


    # Print student name and enrollment number
    print(Fore.BLUE + Style.BRIGHT + f"\nStudent Name: {st_Name}\nEnrollment Number: {st_Env_No}" + Style.RESET_ALL)

    # Print the table using tabulate
    headers = [Fore.GREEN + header + Style.RESET_ALL for header in ["Category", "Subcategory", "Details", "Weightage", "Max Marks", "Student Score", "Weighted Score"]]
    print(tabulate(table, headers=headers, tablefmt="grid"))

    # Call final grade function
    final_grade(total_score,st_Name)
    

    # Display total scores
    print(Fore.BLUE + f"\nTotal Score: {total_score:.2f}")
    
    

        
    # print(Fore.BLUE + f"Total Weighted Score: {total_weighted_score}%\n")

def final_grade(total_score,st_Name):
    if 100 >= total_score >= 90:
        print(Fore.GREEN + f"Student {st_Name} is passed with Grade 'A'. Score: {total_score:.2f}%")
    elif 89 >= total_score >= 80:
        print(Fore.BLUE + f"Student {st_Name} is passed with Grade 'B'. Score: {total_score:.2f}%")
    elif 79 >= total_score >= 65:
        print(Fore.CYAN + f"Student {st_Name} is passed with Grade 'C'. Score: {total_score:.2f}%")
    elif 64 >= total_score >= 50:
        print(Fore.YELLOW + f"Student {st_Name} is passed with Grade 'D'. Score: {total_score:.2f}%")
    else:
        print(Fore.RED + f"Student {st_Name} has failed!!")

#-------------------------------------------------#
#------| Assign values to students fun end |------#
#-------------------------------------------------#


# Main function to run the program
def main():
    while True:
        try:
            option = int(input(Fore.GREEN + "\n1. Add Criteria\n2. Assign Criteria to Students\n3. Exit\n"+ Fore.RED + "Enter your choice: " + Style.RESET_ALL))
            if option == 1:
                add_criteria()
            elif option == 2:
                Student_evaluation()
            elif option == 3:
                print(Fore.GREEN + "Thank you for using the app!" + Style.RESET_ALL)
                break   
            else:
                print(Fore.RED + "Please enter a valid option." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid Number" + Style.RESET_ALL)
            

# Call the main function to start the program

if __name__ == "__main__":
    main()



#-----------------------------------------------#
#--------| Program Structure |---------------#
#-----------------------------------------------#
# """ Program -
#         Exam- 
#             -> WEIGHTAGE
#             -> MARKS
#         Jury-
#             -> WEIGHTAGE
#             -> MARKS
#         CCE-
#             Assignments-
#                 -> WEIGHTAGE
#                 -> MARKS
#             Projects-
#                 -> WEIGHTAGE
#                 -> MARKS
#             Quizzes-
#                 -> WEIGHTAGE
#                 -> MARKS
#             Value Added Courses-
#                 -> WEIGHTAGE
#                 -> MARKS
#             Practical Tests-
#                 -> WEIGHTAGE
#                 -> MARKS
#             Attendance-
#                 -> WEIGHTAGE
#                 -> MARKS
#             Other Activities-
#                 -> WEIGHTAGE
#                 -> MARKS
# ===========================================

# Exam -
#     weightage: 25%
#     Marks: 100
# Jury- 
#     weightage: 25%
#     Marks: 100
# CCE-
#     weightage: 50%
#     CCE_WEIGHTAGE = 100
#     Marks:
#         Assignments:
#             Assignment1: 
#                 weightage: 20%
#                 marks: 50
#             Assignment2: 
#                 weightage: 10%
#                 marks: 50
#         Projects:
#             Project1: 
#                 weightage: 30%
#                 marks: 60
#         Quizzes: 
#                 Quiz1: 
#                     weightage: 10%
#                     marks: 50
#                 Quiz2: 
#                     weightage: 20%
#                     marks: 50
#         Value Added Courses: I dont conduct any value added courses
#         Practical Tests: I dont conduct any practical tests
#         Attendance: 
#             weightage: 10%
#             marks: 100
#         Other Activities: i dont add any other activities at the moment
# """