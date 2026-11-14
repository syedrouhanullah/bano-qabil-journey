
while True:

    a = int(input("Enter Your First Number: "))
    b = int(input("Enter Your Second Number: "))

    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = int(input("Select Operation (1-5): "))

    if choice == 1:
        print(f"Answer: {a + b}")

    elif choice == 2:
        print(f"Answer: {a - b}")

    elif choice == 3:
        print(f"Answer: {a * b}")

    elif choice == 4:
        if b != 0:
            print(f"Answer: {a / b}")
        else:
            print("Cannot Divide by zero!")

    elif choice == 5:
        print("Calculator Closed!")
        break

    else:
        print("Invalid Choice!")
