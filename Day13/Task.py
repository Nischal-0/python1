#decorator
def header_decorator(func):
    def wrapper():
        print("========================================================================================")
        print("\n")
        func()
        print("\n")
        print("========================================================================================")
    return wrapper


#Creating list for users to be stored
users = []


def email_exists(email):
    for user in users:
        if user.get('email')==email:
            return True
        return False


#Register 
@header_decorator
def Register():
    print(f"\t\t\t\tWelcome to Register Portal")
    email = input("Enter Email: ")

    password = input("Enter Password: ")
    C_Password = input("Confirm Password: ")

    if not email_exists(email=email):
        if password == C_Password:
            user = {'email': email, 'password': password}
            users.append(user)
            print("\n")
            print("Registration successful!")
        else:
            print("Passwords do not match. Registration failed.")
    else:
        print(f"Email already exists! Please try again or Log in.")



#Login
@header_decorator
def login():
    print(f"\t\t\t\tWelcome to Login Portal")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user['email'] == email and user['password'] == password:
            print("\n")
            print("Login successful!")
            global isLogin
            isLogin = True
            return 

    print("Invalid email or password. Login failed.")



# Logout
@header_decorator
def logout():
    global isLogin
    isLogin = False
    print("\n")
    print("Logout successful!")



# List all users
@header_decorator
def list_users():
    print("\t\t\t\tList of all users")
    if len(users) > 0:
        for i, user in enumerate(users):
            print(f"User {i + 1}: Email - {user['email']}")
    else:
        print("No users registered yet.")


#main code
isLogin=False
def user_menu():
    print("\n=============== Welcome to the User Registration System===============\n")
    while True:
        print("===== USER MENU =====")
        print("1. User Registration")
        print("2. User Login")
        print("3. List of all the users")
        print("4. Exit")
 
        if isLogin:
            print("5. Logout")
            choice = input("\nEnter your choice (1-5): ")
        else:
            choice = input("\nEnter your choice (1-4): ")


        if choice == '1':
            Register()

        elif choice == '2':
            login()
        
        elif choice == '3':
            if isLogin:
                list_users()
            else:
                print('\n====================| Login first |====================\n')
        
        elif choice == '4':
            return
        
        elif choice == '5' and isLogin:
            logout()
        
        else:
            print("Invalid choice. Please try again.")


user_menu()
