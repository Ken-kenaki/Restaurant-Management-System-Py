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
        saleMonth, chef, saleAmount = sale.strip().split(",")
        if (month.lower() in saleMonth.lower()):
            print(f"Sales for {saleMonth.upper()} {saleAmount}")
            print(f"Chef responsible for that sale: {chef}")


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
    while True:
        print("\nManager Menu:")
        print("1. View Staff")
        print("2. Edit Staff Details")
        print("3. View Sales Report")
        print("4. Add Sales Entry")
        print("5. View Customer Feedback")
        print("6. Log Out")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_staff()  # View staff details
        elif choice == "2":
            edit_staff()  # Edit staff details
        elif choice == "3":
            view_sales_report()  # View sales report
        elif choice == "4":
            add_sales()  # Add a new sales entry
        elif choice == "5":
            view_feedback()  # View customer feedback
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# View Staff Details
def view_staff():
    print("\nStaff List:")
    try:
        with open("user.txt", "r") as file:
            users = file.readlines()
            for user in users:
                username, password, role = user.strip().split(",")
                print(f"Username: {username}, Role: {role}")
    except FileNotFoundError:
        print("No staff data found.")

# Edit Staff Details
def edit_staff():
    print("\nEdit Staff Details:")
    username = input("Enter the username of the staff member to edit: ").strip()
    new_username = input("Enter new username (leave blank to keep unchanged): ").strip()
    new_password = input("Enter new password (leave blank to keep unchanged): ").strip()
    new_role = input("Enter new role (leave blank to keep unchanged): ").strip()

    found = False
    try:
        with open("user.txt", "r") as file:
            users = file.readlines()

        with open("user.txt", "w") as file:
            for user in users:
                current_username, current_password, current_role = user.strip().split(",")
                if current_username == username:
                    found = True
                    if new_username:
                        current_username = new_username
                    if new_password:
                        current_password = new_password
                    if new_role:
                        current_role = new_role
                    print(f"Updated staff details for {username}.")
                file.write(f"{current_username},{current_password},{current_role}\n")
                
    except FileNotFoundError:
        print("No staff data found.")

    if not found:
        print(f"Staff member with username {username} not found.")

# View Sales Report
def view_sales_report():
    print("\nView Sales Report")
    date_range = input("Enter date range (e.g., 'daily' or 'weekly'): ").strip().lower()

    try:
        with open("sales.txt", "r") as file:
            sales = file.readlines()

        print("Sales Report:")
        for sale in sales:
            sale_date, chef_name, amount = sale.strip().split(",")
            if date_range == "daily":
                print(f"Date: {sale_date}, Chef: {chef_name}, Sales: {amount}")
            elif date_range == "weekly":
                print(f"Week: {sale_date}, Chef: {chef_name}, Sales: {amount}")
            else:
                print(f"Date: {sale_date}, Chef: {chef_name}, Sales: {amount}")

    except FileNotFoundError:
        print("Sales report file not found.")

# Add Sales Entry
def add_sales():
    print("\nAdd Sales Entry:")
    date = input("Enter the date of sale: ").strip()
    chef_name = input("Enter the chef's name: ").strip()
    amount = input("Enter the total sales amount: ").strip()

    with open("sales.txt", "a") as file:
        file.write(f"\n{date},{chef_name},{amount}")
    
    print(f"Sales entry added for {chef_name} on {date} with amount {amount}.")

# View Customer Feedback
def view_feedback():
    print("\nView Customer Feedback:")
    try:
        with open("feedback.txt", "r") as file:
            feedback = file.readlines()
            for entry in feedback:
                customer_name, comment, rating = entry.strip().split(",")
                print(f"Customer: {customer_name}, Comment: {comment}, Rating: {rating}")
    except FileNotFoundError:
        print("No feedback data found.")


# Chef
def chef():
    chefUserName = input("Enter your chef name: ")
    while True:
        print("\nChef Menu:")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. View Sales Report")
        print("4. Log Out")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_orders()
        elif choice == "2":
            update_order_status()
        elif choice == "3":
            view_chef_sales(chefUserName)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def view_orders():
    print("\nPending Orders:")
    try:
        with open("orders.txt", "r") as file:
            orders = file.readlines()
            for order in orders:
                customer, details, status = order.strip().split(",")
                if status.lower() == "pending":
                    print(f"Customer: {customer}, Order: {details}, Status: {status}")
    except FileNotFoundError:
        print("No orders found.")




def update_order_status():
    print("\nUpdate Order Status:")
    customer = input("Enter the customer's username whose order is completed: ").strip()

    found = False
    try:
        with open("orders.txt", "r") as file:
            orders = file.readlines()

        with open("orders.txt", "w") as file:
            for order in orders:
                order_customer, details, status = order.strip().split(",")
                if order_customer == customer and status.lower() == "pending":
                    status = "Completed"
                    found = True
                    print(f"Order for {customer} has been marked as completed.")
                file.write(f"{order_customer},{details},{status}\n")

    except FileNotFoundError:
        print("No orders found.")

    if not found:
        print(f"No pending order found for {customer}.")




def view_chef_sales(chef_name):
    print(f"\nSales Report for {chef_name}:")
    try:
        with open("sales.txt", "r") as file:
            sales = file.readlines()

        total_sales = 0
        for sale in sales:
            date, chef, amount = sale.strip().split(",")
            if chef == chef_name:
                print(f"Date: {date}, Sales: {amount}")
                total_sales += int(amount)

        print(f"Total Sales: {total_sales}")
    except FileNotFoundError:
        print("No sales record found.")


# Customer Functionality
def customer():
    while True:
        print("\nCustomer Menu:")
        print("1. Place Order")
        print("2. View Order Status")
        print("3. Provide Feedback")
        print("4. Log Out")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            place_order()
        elif choice == "2":
            view_order_status()
        elif choice == "3":
            provide_feedback()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

# Place Order
def place_order():
    username = input("Enter your username: ").strip()
    order_details = input("Enter your order: ").strip()
    with open("orders.txt", "a") as file:
        file.write(f"\n{username},{order_details},pending")
    print("Order placed successfully!")

# View Order Status
def view_order_status():
    username = input("Enter your username: ").strip()
    try:
        with open("orders.txt", "r") as file:
            orders = file.readlines()
        found = False
        for order in orders:
            customer, details, status = order.strip().split(",")
            if customer == username:
                print(f"Order: {details}, Status: {status}")
                found = True
        if not found:
            print("No orders found.")
    except FileNotFoundError:
        print("No order records found.")

# Provide Feedback
def provide_feedback():
    username = input("Enter your username: ").strip()
    feedback_text = input("Enter your feedback: ").strip()
    with open("feedback.txt", "a") as file:
        file.write(f"\n{username},{feedback_text}")
    print("Thank you for your feedback!")


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
