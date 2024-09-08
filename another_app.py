# Student Grades Calculator App

# I can declare a Global dictionary here which will be used to store all the criterias
criteriadic = {}
TOTAL_WEIGHTAGE = 100
TOTAL_cce_WEIGHTAGE = 100
weightage_list = {}
cce_weightage = {}


def criteria():
    condition = True
    global TOTAL_WEIGHTAGE  # Declare TOTAL_WEIGHTAGE as global
    
    # Criteria Details
    while condition:
        
        # Teacher's Details
        # subname = input("Enter subject name: ")
        # instucter = input("Enter teacher name: ")
        
        
        #-------------------------------------------------------------------------------------------------#
        #-----| Ask user if they want to add assignments and how many exam weightages they want to add |--#
        #-------------------------------------------------------------------------------------------------#
        
        print("\n--------| Enter Some Exam Details |--------\n")
        
        conf = input("Do you want to add Exam? Y/N : ").upper()
        if conf == "Y":
            while True:
                print("\nTotal weightage: ", TOTAL_WEIGHTAGE, "%\n")
                try:
                    weightage = float(input("How many exam weightages do you want to add? : "))
                    if weightage > TOTAL_WEIGHTAGE:   # Check if weightage is less than Total weightage
                        print(f"Total weightage of Exam cannot be greater than {TOTAL_WEIGHTAGE}%")
                        continue
                    
                    # Minus TOTAL_WEIGHTAGE with weightage
                    TOTAL_WEIGHTAGE -= weightage
                    
                    marks = float(input("How many exam marks do you want to add? : "))
                    criteriadic["Exam"] = {
                        "weightage": weightage,
                        "marks": marks
                    }
                  
                    weightage_list["Exam"] = weightage/100
                    break
                except ValueError:
                    print("Please enter a valid number")
         
        print("\n--------| Enter Some Jury Details |--------\n")
        
        
        #-----------------------------------------------------#
        #---|  how many Jury weightages they want to add |----#
        #-----------------------------------------------------#
        conf = input("Do you want to add Jury? Y/N : ").upper()
        if conf == "Y":
            while True:
                print("\nTotal Remaining weightage: ", TOTAL_WEIGHTAGE, "%\n")
                try:
                    weightage = float(input("How many Jury weightages do you want to add? : ")) 
                    if weightage > TOTAL_WEIGHTAGE: # Check if weightage is less than Total weightage
                        print(f"Total weightage of Jury cannot be greater than {TOTAL_WEIGHTAGE}% because you have only {TOTAL_WEIGHTAGE}% left")
                        continue
                        
                    # Minus TOTAL_WEIGHTAGE with weightage
                    TOTAL_WEIGHTAGE -= weightage
                    marks = float(input("How many Jury marks do you want to add? : "))
                    criteriadic["Jury"] = {
                        "weightage": weightage,
                        "marks": marks
                    }
                    
                    print("\n\nTotal weightage after adding Jury: ", TOTAL_WEIGHTAGE, "\n\n")
                
                    weightage_list["Jury"] = weightage/100
                    break
                except ValueError:
                    print("Please enter a valid number")
                
                
        #-------------------------------------------------------------------------------------------------#
        #---| how many Continuous and Comprehensive Evaluation (CCE) weightages they want to add |----#
        #-------------------------------------------------------------------------------------------------#
    
        print("\n--------| Enter Some Continuous and Comprehensive Evaluation (CCE) Details |--------\n")
        
        while True:
            print("\nTotal Remaining weightage: ", TOTAL_WEIGHTAGE, "%\n")
            print("\nWe can add all remaining weightage into CCE \n")
            
            weightage=TOTAL_WEIGHTAGE
            weightage_list["CCE"] = weightage/100
            
            
            # Ask user if they want to add assignments
            print("\nTotal Remaining CCE weightage: ", TOTAL_cce_WEIGHTAGE, "%\n")
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
    global TOTAL_cce_WEIGHTAGE  # Declare TOTAL_WEIGHTAGE as global
    # Ensure '*name' key exists
    if name not in criteriadic and weightage_list:
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
        weightage=TOTAL_cce_WEIGHTAGE
        if TOTAL_cce_WEIGHTAGE >= weightage:
            weightage_list[name][name_name] = weightage/100
            TOTAL_cce_WEIGHTAGE-=weightage
            print("\nTotal Remaining CCE weightage: ", TOTAL_cce_WEIGHTAGE, "%\n")
        else:
            print(f"\n {name_name} weightage cannot be greater than {TOTAL_cce_WEIGHTAGE}%\n")
            
        



criteria()