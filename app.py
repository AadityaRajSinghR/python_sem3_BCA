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
