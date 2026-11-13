name = input("Enter Your Name: ")
age = int(input("Enter your age: "))
height = float(input("Enter Your Height: "))
gender = input("Enter Your Gender (male/female): ")
marks = int(input("Enter your marks: "))

print("Welcome", name)

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
else:
    print("You are Fail")

print("Your Name is:", name)
print("Your Age is:", age)
print("Your Height:", height)
print("Your Gender Is:", gender)
