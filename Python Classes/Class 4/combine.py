username =input("Username:")
password =input("Password:")

if username == "Student":
    if password == "Password":
        print("Login Successful!")

        for row in range (1,4):
            for student in range (1,2):
                print("Row:",row,"Student:",student)
    
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")