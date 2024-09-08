# Student Grades Calculator App

# I can declare a Global dictionary here which will be used to store all the criterias
criteriadic = {}
TOTAL_WEIGHTAGE = 100
weightage_list = {}

def criteria():
    condition = True
    global TOTAL_WEIGHTAGE  # Declare TOTAL_WEIGHTAGE as global
    
    # Criteria Details
    while condition:
        
        # Teacher's Details
        # subname = input("Enter subject name: ")
        # instucter = input("Enter teacher name: ")
        
        # Ask user if they want to add assignments and how many exam weightages they want to add
        print("\n--------| Enter Some Exam Details |--------\n")
        
        conf = input("Do you want to add Exam? Y/N : ").upper()
        if conf == "Y":
            while True:
                print("\n\nTotal weightage before adding Exam: ", TOTAL_WEIGHTAGE)
                try:
                    weightage = int(input("How many exam weightages do you want to add? : "))
                    if weightage > TOTAL_WEIGHTAGE:   # Check if weightage is less than Total weightage
                        print(f"Total weightage of Exam cannot be greater than {TOTAL_WEIGHTAGE}%")
                        continue
                    
                    # Minus TOTAL_WEIGHTAGE with weightage
                    TOTAL_WEIGHTAGE -= weightage
                    weightage_list["Exam"] = weightage
                    marks = int(input("How many exam marks do you want to add? : "))
                    criteriadic["Exam"] = {
                        "weightage": weightage,
                        "marks": marks
                    }
                    
                    break
                except ValueError:
                    print("Please enter a valid number")
         
        print("\n--------| Enter Some Jury Details |--------\n")
        
        # And how many Jury weightages they want to add
        while True:
            print("\n\nTotal weightage before adding Jury: ", TOTAL_WEIGHTAGE, "\n\n")
            try:
                weightage = int(input("How many Jury weightages do you want to add? : ")) 
                if weightage > TOTAL_WEIGHTAGE: # Check if weightage is less than Total weightage
                    print(f"Total weightage of Jury cannot be greater than {TOTAL_WEIGHTAGE}% because you have only {TOTAL_WEIGHTAGE}% left")
                    continue
                    
                # Minus TOTAL_WEIGHTAGE with weightage
                TOTAL_WEIGHTAGE -= weightage
                weightage_list["Jury"] = weightage
                
                marks = int(input("How many Jury marks do you want to add? : "))
                criteriadic["Jury"] = {
                    "weightage": weightage,
                    "marks": marks
                }
                
                print("\n\nTotal weightage after adding Jury: ", TOTAL_WEIGHTAGE, "\n\n")
                break
            except ValueError:
                print("Please enter a valid number")
        
        print("\n--------| Enter Some Continuous and Comprehensive Evaluation (CCE) Details |--------\n")
        
        while True:
            print("\n\nTotal weightage before adding CCE: ", TOTAL_WEIGHTAGE, "\n\n")
        
            # Ask user if they want to add assignments
            conf = input("Do you want to add assignments? Y/N : ").upper()
            if conf == "Y":
                while True:
                    try:
                        num = int(input(f"How many assignments do you want to add? : "))
                        get_values("Assignment", num)
                        break
                    except ValueError:
                        print("Please enter a valid number")

            # Ask user if they want to add projects
            conf = input("Do you want to add projects? Y/N : ").upper()
            if conf == "Y":
                while True:
                    try:
                        num = int(input(f"How many projects do you want to add? : "))
                        get_values("Project", num)
                        break
                    except ValueError:
                        print("Please enter a valid number")
                
            # Ask user if they want to add Quiz
            conf = input("Do you want to add Quiz? Y/N : ").upper()
            if conf == "Y":
                while True:
                    try:
                        num = int(input(f"How many Quizzes do you want to add? : "))
                        get_values("Quiz", num)
                        break
                    except ValueError:
                        print("Please enter a valid number")
                
            # Ask user if they want to add Value added course
            conf = input("Do you want to add Value added course? Y/N : ").upper()
            if conf == "Y":
                while True:
                    try:
                        num = int(input(f"How many Value added courses do you want to add? : "))
                        get_values("Value added course", num)
                        break
                    except ValueError:
                        print("Please enter a valid number")
            
            # Ask user if they want to add Practical Test
            conf = input("Do you want to add Practical Test? Y/N : ").upper()
            if conf == "Y":
                while True:
                    try:
                        num = int(input(f"How many Practical Tests do you want to add? : "))
                        get_values("Practical Test", num)
                        break
                    except ValueError:
                        print("Please enter a valid number")
                        
            conf = input("Do you want to add Attendance? Y/N : ").upper()
            if conf == "Y":
                weightage = int(input("Enter Weightage: "))
                criteriadic["Attendance"] = {
                    "weightage": weightage,
                    "marks": 100
                }
            
            while True:
                conf = input("Do you want to add Other Activity? Y/N : ").upper()
                if conf == "Y":
                    while True:
                        try:
                            name = input("Enter name of Other Activity: ")
                            get_values(name, 1)
                            conf = input("Do you want to add more Other Activities? Y/N : ").upper()
                            if conf == "N":
                                break
                        except ValueError:
                            print("Please enter a valid value")
                else:
                    break

            break
                
        print(f"\n\nCriteriadic: {criteriadic}\n\n")  
        print(f"Weightage list: {weightage_list}\n\n") 
        conf = input("Do you want to continue? Y/N : ")
        if conf == "N" or conf == "n":
            condition = False

def get_values(name, num):
    # Ensure '*name' key exists
    if name not in criteriadic:
        criteriadic[name] = {}

    # Add *name to the dictionary
    for i in range(num):
        # Get {name} details
        name_name = input(f"Enter name for {name} {i+1}: ")
        weightage = int(input("Enter Weightage: "))
        weightage_list[name] = weightage
        marks = int(input("Enter Marks: "))

        # Add project to the dictionary
        criteriadic[name][name_name] = {
            "weightage": weightage,
            "marks": marks
        }



criteria()









# Student Grades Calculator App

# Global dictionary to store all the criteria
# criteriadic = {}
# TOTAL_WEIGHTAGE = 100
# weightage_list = {}

# def prompt_for_weightage(context):
#     # Prompt the user for weightage and marks with error handling.
#     while True:
#         try:
#             weightage = int(input(f"Enter weightage for {context}: "))
#             if weightage <= TOTAL_WEIGHTAGE:
#                 return weightage
#             else:
#                 print(f"Weightage cannot be greater than {TOTAL_WEIGHTAGE}%. Please enter a valid weightage.")
#         except ValueError:
#             print("Please enter a valid number.")
            
# def prompt_for_CCE_weightage(context):
#     # Prompt the user for weightage and marks with error handling.
#     while True:
#         try:
#             weightage = int(input(f"Enter weightage for {context}: "))
#             if weightage <= TOTAL_WEIGHTAGE:
#                 return weightage
#             else:
#                 print(f"Weightage cannot be greater than {TOTAL_WEIGHTAGE}%. Please enter a valid weightage.")
#         except ValueError:
#             print("Please enter a valid number.")

# def get_values(name, num):
#     # Get details for each item type and update the global dictionary.
#     if name not in criteriadic:
#         criteriadic[name] = {}
    
#     for i in range(num):
#         name_name = input(f"Enter name for {name} {i+1}: ")
#         weightage = prompt_for_weightage(name_name)
#         marks = int(input(f"Enter marks for {name_name}: "))
        
#         criteriadic[name][name_name] = {
#             "weightage": weightage,
#             "marks": marks
#         }

# def criteria():
#     global TOTAL_WEIGHTAGE  # Declare TOTAL_WEIGHTAGE as global
    
#     while True:
#         print("\n--------| Enter Exam Details |--------\n")
        
#         if input("Do you want to add Exam? Y/N : ").upper() == "Y":
#             print(f"Total weightage before adding Exam: {TOTAL_WEIGHTAGE}%")
#             weightage = prompt_for_weightage("Exam")
#             weightage_list["Exam"] = weightage
#             TOTAL_WEIGHTAGE -= weightage
            
#             marks = int(input("Enter the number of exam marks: "))
#             criteriadic["Exam"] = {
#                 "weightage": weightage,
#                 "marks": marks
#             }
        
#         print("\n--------| Enter Jury Details |--------\n")
        
#         if input("Do you want to add Jury? Y/N : ").upper() == "Y":
#             print(f"Total weightage before adding Jury: {TOTAL_WEIGHTAGE}%")
#             weightage = prompt_for_weightage("Jury")
#             weightage_list["Jury"] = weightage
#             TOTAL_WEIGHTAGE -= weightage
            
#             print(f"\n\nTotal weightage after adding Jury: {TOTAL_WEIGHTAGE}% \n\n")
            
#             marks = int(input("Enter the number of jury marks: "))
#             criteriadic["Jury"] = {
#                 "weightage": weightage,
#                 "marks": marks
#             }
        
#         print("\n--------| Enter CCE Details |--------\n")
#         cce_weightage = 100
#         if TOTAL_WEIGHTAGE > 0:
#             weightage = TOTAL_WEIGHTAGE
#             weightage_list["CCE"] = weightage
#             # TOTAL_WEIGHTAGE -= weightage
#             criteriadic["CCE"] = {
#                 "weightage": weightage,
#                 "marks": 100  # Assuming full marks are always 100 for CCE
#             }
        
#         for category in ["Assignments", "Projects", "Quiz", "Value added course", "Practical Test"]:
#             if input(f"\nDo you want to add {category}? Y/N : ").upper() == "Y":
#                 num = int(input(f"How many {category} do you want to add? : "))
#                 get_values(category, num)
        
#         if input("Do you want to add Attendance? Y/N : ").upper() == "Y":
#             weightage = prompt_for_CCE_weightage("Attendance")
#             criteriadic["Attendance"] = {
#                 "weightage": weightage,
#                 "marks": 100  # Assuming full marks are always 100 for Attendance
#             }
        
#         while input("Do you want to add Other Activity? Y/N : ").upper() == "Y":
#             name = input("Enter name of Other Activity: ")
#             get_values(name, 1)
        
#         print("\nFinal Criteria Dictionary:")
#         print(criteriadic)
        
        
#         print("\nFinal Weightage Dictionary:")
#         print(weightage_list)
        
#         if input("Do you want to continue? Y/N : ").upper() == "N":
#             break

# criteria()












# # Student Grades Calculator App

# # Import colorama for text color formatting
# from colorama import Fore, Style, init
# from tabulate import tabulate
# init(autoreset=True)  # Automatically reset color to default after each print

# criteriadic = {}
# TOTAL_WEIGHTAGE = 100
# TOTAL_cce_WEIGHTAGE = 100
# weightage_list = {}

# # Function to confirm user action
# def confirm_action(op):
#     return input(Fore.RED + f"Do you want to add {op}? Y/N : ").upper()


# def criteria():
#     condition = True
#     global TOTAL_WEIGHTAGE  # Declare TOTAL_WEIGHTAGE as global
    
#     while condition:
        
#         # Exam Details
#         print(Fore.CYAN + "\n--------| Enter Some Exam Details |--------\n")
#         if confirm_action("Exam") == "Y":
#             add_weightage("Exam")
         
#         # Jury Details
#         print(Fore.CYAN + "\n--------| Enter Some Jury Details |--------\n")
#         if confirm_action("Jury") == "Y":
#             add_weightage("Jury")
                
#         # Continuous and Comprehensive Evaluation (CCE) Details
#         print(Fore.CYAN + "\n--------| Enter Some Continuous and Comprehensive Evaluation (CCE) Details |--------\n")
        
#         handle_cce_details()
        
         
        
#         # Check if user wants to continue
#         cont = input(Fore.YELLOW + "Do you want to continue? Y/N : ").upper()
#         if cont == "N":
#             print(Fore.MAGENTA + "Thank you for using the app!")
#             condition = False
#         elif cont != "Y":
#             print(Fore.RED + "Please enter a valid option.")

# def add_weightage(category):
#     global TOTAL_WEIGHTAGE  # Declare TOTAL_WEIGHTAGE as global
#     while True:
#         print("\nTotal Remaining weightage: ", TOTAL_WEIGHTAGE, "%\n")
#         try:
#             weightage = float(input(f"How many {category} weightages do you want to add? : "))
#             if weightage > TOTAL_WEIGHTAGE:
#                 print(f"Total weightage of {category} cannot be greater than {TOTAL_WEIGHTAGE}%")
#                 continue
                
#             TOTAL_WEIGHTAGE -= weightage
#             marks = float(input(f"How many {category} marks do you want to add? : "))
#             criteriadic[category] = {"weightage": weightage, "marks": marks}
#             weightage_list[category] = weightage / 100
#             break
#         except ValueError:
#             print("Please enter a valid number")

# def handle_cce_details():
#     global TOTAL_cce_WEIGHTAGE, TOTAL_WEIGHTAGE
#     weightage = TOTAL_WEIGHTAGE
#     if "CCE" not in criteriadic:
#         criteriadic["CCE"] = {}
        
#     criteriadic["CCE"] = {"weightage": weightage}
#     weightage_list["CCE"] = weightage / 100
#     TOTAL_WEIGHTAGE = 0  # No weightage left for other categories after CCE
    
#     print(Fore.RED +"\nTotal Remaining CCE weightage: ", TOTAL_cce_WEIGHTAGE, "%\n")
#     Style.RESET_ALL
#     add_cce_activities()

# def add_cce_activities():
#     Style.RESET_ALL
#     cce_activities = ["assignments", "projects", "quizzes", "value added courses", "practical tests", "attendance", "other activities"]
#     for activity in cce_activities:
#         if TOTAL_cce_WEIGHTAGE == 0:
#             print("You have reached the maximum CCE weightage. No more activities can be added.")
#             return
#         else:
#             if confirm_action( activity.capitalize()) == "Y":
                
#                 if activity == "attendance":
#                     add_attendance()
#                 else:
#                     while True:
#                         try:
#                             num = int(input(Style.RESET_ALL + f"How many {activity} do you want to add? : "))
#                             get_values(activity.capitalize(), num)
#                             break
#                         except ValueError:
#                             print("Please enter a valid number")

# def add_attendance():
#     global TOTAL_cce_WEIGHTAGE
#     while True:
#         try:
#             weightage = float(input("\tEnter Attendance Weightage: "))
#             if weightage > TOTAL_cce_WEIGHTAGE:
#                 print(Fore.RED + f"Attendance weightage cannot be greater than the remaining CCE weightage: {TOTAL_cce_WEIGHTAGE}%")
#                 Style.RESET_ALL
#                 continue
#             criteriadic["CCE"]["Attendance"] = {"weightage": weightage, "marks": 100}
#             TOTAL_cce_WEIGHTAGE -= weightage
#             break
#         except ValueError:
#             print(Fore.RED +"Please enter a valid number" + Style.RESET_ALL)

# def get_values(name, num):
#     global TOTAL_cce_WEIGHTAGE
#     # Ensure 'CCE' key exists
#     if "CCE" not in criteriadic:
#         criteriadic["CCE"] = {}
    
#     # Ensure the 'name' key exists within 'CCE'
#     if name not in criteriadic["CCE"]:
#         criteriadic["CCE"][name] = {}
        
#     for i in range(num):
#         name_name = input(f"\tEnter name for {name} {i+1}: ")
#         while True:
#             try:
#                 weightage = float(input("\tEnter Weightage: "))
#                 if weightage > TOTAL_cce_WEIGHTAGE:
#                     print(f"\n{name_name} weightage cannot be greater than {TOTAL_cce_WEIGHTAGE}%\n")
#                     continue
#                 TOTAL_cce_WEIGHTAGE -= weightage
#                 marks = float(input("\tEnter Marks: "))
#                 criteriadic["CCE"][name][name_name] = {"weightage": weightage, "marks": marks}
#                 print("\nTotal Remaining CCE weightage: ", TOTAL_cce_WEIGHTAGE, "%\n")
#                 break
#             except ValueError:
#                 print("Please enter a valid number")

# criteria()

# print(Fore.BLUE + f"\n\nCriteriadic: {criteriadic}\n\n")  



# # Prepare data for tabulate dynamically
# def display_criteria():
#     """Display the criteria in a formatted table"""
#     table = []
#     for category, values in criteriadic.items():
#         if isinstance(values, dict) and "weightage" in values:
#             table.append([category, "", "", values["weightage"], values.get("marks", "")])
#         else:
#             for sub_category, sub_values in values.items():
#                 for detail, detail_values in sub_values.items():
#                     table.append(["CCE", sub_category, detail, detail_values["weightage"], detail_values["marks"]])

#     print(tabulate(table, headers=["Category", "Subcategory", "Details", "Weightage", "Marks"], tablefmt="grid"))

# display_criteria()



# print(Fore.GREEN + f"Weightage list: {weightage_list}")



