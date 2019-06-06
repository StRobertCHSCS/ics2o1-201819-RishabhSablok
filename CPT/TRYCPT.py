# Defining the Function
def function1():
    # Introduction
    print("Multiple choice quiz")
    # Adding the Question and Answers in 2 Arrays so that it is easier to call them when I need them.
    # Also created an empty array to see what question the user got wrong or right.
    question = ["Q1: 1 Byte is equal to 64 bits", "Q2: 1 Byte equal to 8 bits", "Q3: Worms are type of viruses that eat your computers hardware."]
    answer = ["F", "T", "F"]
    f = []
    counter = 0
    mark = 0
    while counter < 3:
        print(question[counter])
        print("Type T for Truth and F for False")
        user_input = input("Please enter in capitals here: ")
        print()
        while user_input != "T" and user_input != "F":
            user_input = input("Please enter T for Truth and F for false: ")
        if user_input == answer[counter]:
            mark = mark + 1
            f.append("Right")
        else:
            f.append("Wrong")
        counter += 1

    print("Q4: Which of them are not malwares.")
    print("1. Virus")
    print("2. Root Kit")
    print("3. Trojan")
    print("4. Copy kit")
    a = int(input("Enter answer(1 - 4): "))
    while a != 1 or a != 2 or a != 3 or a != 4:
        a = int(input("Enter a answer that is between 1 and 4: "))
    if a == 4:
        mark = mark + 1
        f.append("Right")
    else:
        f.append("Wrong")

    print("Q5: Which of the following malwares create fake FBI notifications.")
    print("1. Root Kit")
    print("2. Ransomware")
    print("3. Backdoor")
    print("4. Rouge Security Software")
    b = int(input("Enter answer(1 - 4): "))
    while b != 1 or b != 2 or b != 3 or b != 4:
        b = int(input("Enter a answer between 1 to 4"))
    if b == 3:
        mark = mark + 1
        f.append("Right")
    else:
        f.append("Wrong")

    print("Q6: Is a monitor a peripheral component or a hardware component.")
    print("1. Peripheral")
    print("2. Hardware")
    print("3. Neither")
    print("4. Both")
    b = int(input("Enter answer(1 - 4): "))
    if b == 1:
        mark = mark + 1
        f.append("Right")
    else:
        f.append("Wrong")

    print("Your mark is ", mark, " out of 6")
    print(f)


function1()
