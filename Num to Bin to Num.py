while True:
    print("What you want to do:")
    print("1. Number to Binary")
    print("2. Binary to Number")

    choose = input("Enter your choice (1 or 2): ")

    if choose == '1' or 'number to binary' in choose.lower():
        number = int(input("Enter Your Number: "))
        new = ""
        while number > 0:
            if number % 2 == 0:
                space = (len(new) + 1) % 5
                if space == 0:
                    new = ' ' + new
                new = '0' + new
            else:
                space = (len(new) + 1) % 5
                if space == 0:
                    new = ' ' + new
                new = '1' + new
            number //= 2
        print(f"Binary = {new}\n\n")

    elif choose == '2' or 'binary to number' in choose.lower():
        binary_input = input("Enter the binary number: ")
        # Remove spaces from the binary input
        binary_input = binary_input.replace(" ", "")

        if not all(bit in '01' for bit in binary_input):
            print("Invalid binary input. Only 0s and 1s are allowed.")
        else:
            answer = int(binary_input, 2)
            print(f"Numeric = {answer}\n\n")

    else:
        print("Invalid choice. Please choose 1 or 2.")
