while True:
    print("Calculator menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        add = num1 + num2
        print("The addition is:", add)

    elif choice == '2':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sub = num1 - num2
        print("The subtraction is:", sub)

    elif choice == '3':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        mul = num1 * num2
        print("The multiplication is:", mul)

    elif choice == '4':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            div = num1 / num2
            print("The division is:", div)

    if choice == '5':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        mod = num1 % num2  
        print("The modulus is:", mod)


    elif choice == '6':
        break

    else:
        print("Invalid entry. Please try again.")
