# Global Variables
available_roles = {"admin", "manager", "chef", "customer"}


# Admin.......

def admin():
    print("Welcome!, Admin. Can you choose an action that you want to perform:")
    print("1. Add Staff")
    print("2. Edit Staff")
    print("3. Delete Staff")
    print("4. View Sales Report by month")
    print("5. View Customer Feedback")
    print("6. Update Admin's Profile")
    print("7. Log Out")

    adminChoice = int(input("Enter your choice: "))

    if adminChoice == 1:
        addStaff()
    elif adminChoice == 2:
        editStaff()  
    elif adminChoice == 3:
        deleteStaff()
    elif adminChoice == 4:
        viewSalesReport()
    elif adminChoice == 5:
        viewFeedback()
    elif adminChoice == 6:
        updateProfile()
    elif adminChoice == 7:
        print("Logging out...")
        return
    else:
        print("Invalid choice.")


def addStaff():
    print("Enter details to add new staff members..")
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    role = input("Enter Role (admin, manager, chef, customer): ").strip().lower()

    # Checking if the user has inputed an valid role.
    if role not in available_roles:
        print("Invalid role. Try again.")
        role = input("Enter Role (admin, manager, chef, customer): ").strip().lower()

    # Appending role to the user.txt file
    with open("user.txt", "a") as users:
        users.write(f"\n{username.lower()},{password},{role}")
    print(f"User {username.upper()} added sucessfully!!")



# Deleting staffs...

def deleteStaff():
    print("Delete Staff Members!")
    delUserName = input("Enter an user name of the staff to delete: ")

    with open("user.txt", 'r') as userFile:
        users = userFile.readlines()


    #Using enumerate to add indexing to each value in user list
    
    userFound = False
    for i, user in enumerate(users):
        userName, userPassword, role = user.strip().split(",")
        if userName == delUserName:
            userFound= True
            print(f"Deleting {delUserName}")
            del users[i]
            break
    if userFound:
        with open("user.txt", "w") as file:
            file.writelines(users)
            print(f"Staff {delUserName} deleted successfully.")
    else:
        print(f"Staff {delUserName} not found.")
        



# Viewing Feedbacks
def viewFeedback():
    with open("feedback.txt", "r") as feedbackFiles:
        feedbacks = feedbackFiles.readlines()

    print("Customer Feedback:")
    for feedback in feedbacks:
        username, feedback_text = feedback.strip().split(",", 1)
        print(f"From {username}: {feedback_text}")

# Updating Profile..

def updateProfile():
    adminUsername = input("Enter your username to update your profile: ").strip()
    newPassword = input("Enter new password: ").strip()
    newRole = input("Enter new role: ").strip()

    with open("user.txt", "r") as file:
        users = file.readlines()

    adminFound = False
    for i, user in enumerate(users):
        userName, userPassword, role = user.strip().split(",")
        if userName == adminUsername and role == "admin":
            adminFound = True
            users[i] = f"{adminUsername},{newPassword},{newRole}\n"
            break

    if adminFound:
        with open("user.txt", "w") as file:
            file.writelines(users)
        print("Profile updated successfully.")
    else:
        print("Admin not found.")



# To view sales report
def viewSalesReport():
    month = input("Enter month to view sales report for that month:").strip()

    with open("sales.txt", "r") as file:
        sales = file.readlines()

    print("Sales Report:")
    for sale in sales:
        saleMonth, saleAmount = sale.strip().split(",")
        if (month.lower() in saleMonth.lower()):
            print(f"Sales for {saleMonth.upper()}:  {saleAmount}")


# To edit staff
def editStaff():
     print("Edit Staff Member")
     editUserName = input("Enter Username of the staff to edit: ").strip()

     with open("user.txt", "r") as userFile:
        users = userFile.readlines()
    
     staffFound = False

     for i, user in enumerate(users):
        userName, userPassword, role = user.strip().split(",")
        if(userName == editUserName):
            staffFound = True
            print(f"Editing {editUserName}")
            new_password = input("Enter new password: ").strip()
            new_role = input("Enter new role: ").strip().lower()

            if new_role not in available_roles:
                print("Invalid role. No changes made.")
                return

            # Updating staff details
            users[i] = f"{editUserName},{new_password},{new_role}\n"
            break

     if staffFound:
        with open("user.txt", "w") as file:
            file.writelines(users)
        print(f"Staff {userName} edited successfully.")
     else:
        print(f"Staff {editUserName} not found.")



























# Manager
def manager():
    print("You are a manager..")

# Chef
def chef():
    print("You are a chef..")

# Customer
def customer():
    print("You are a customer..")





#Authentication
def authentication():
    auth = int(input("1.Login\n 2.Sign Up"))

    if auth == 1:
        login()
    if auth == 2:
        signUp()


#Sign Up 
def signUp():
    print("You need to sign up....")
    createUser = input("Enter Your User Name:").lower()
    createUserPassword = input("Enter Your Password:")
    createUserRole = input("Enter Your Role:").lower()


    # Checking if the provided role is valid or not!!
    if createUserRole not in available_roles:
        print("Invalid role!! Please enter a valid role!!")
        createUserRole = input("Enter Your Role:").lower()


    with open("user.txt", 'a') as users:
        users.write(f"\n{createUser},{createUserPassword},{createUserRole}")
    print(f"Sign Up Sucessfully! You may now choose to log in!")
    return authentication()





#Login
def login():
    attempts = 3 
    while attempts > 0:
        username = input("Enter Your Username: ").strip().lower()
        password = input("Enter Your Password: ").strip().lower()

        with open("user.txt", 'r') as users:
            for user in users:
                userName, userPassword, role = user.strip().split(",")

                print(role)

                # Checking username and password
                if username == userName and password == userPassword:
                    print(f"\nLogin Successful!\nWelcome {username}, you are logged in as a {role}.\n")

                    # Dictionary to map roles to functions
                    role_functions = {
                        "admin": admin,
                        "manager": manager,
                        "chef": chef,
                        "customer": customer
                    }

                    if role in role_functions:
                        role_functions[role]()
                        return 

        
        print("Invalid Credentials..., Try Again!")
        attempts -= 1

    print("Too many failed attempts, Try again later..")



authentication()
