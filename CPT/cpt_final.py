import ctypes

"""
------------------------------------------------------------------------------------------------------------------------
Name:		cpt_final.py
Purpose:    To test a person on his understanding of Computer Science

Author:		Sablok.R

Created:    5/6/2019
------------------------------------------------------------------------------------------------------------------------
"""

print("********** Welcome **********\n")


score_in_letters = []
counter = 0
mark = 0

# Defining the Function


def intro():
    # Introduction
    print("****************************Multiple choice quiz****************************")
    name = input("What is your name: ")
    print("Hi", name, "let us start the quiz.")


def end():
    print("Your mark is ", mark, " out of 8")
    print(score_in_letters)


def box(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def multiple_choice(question_mcq, answer1, answer2, answer3, answer4, mcq_answer, words):
    global counter, mark, score_in_letters
    print(question_mcq)
    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)
    user_input = int(input("Input your choice from 1 to 4: "))
    while user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
        user_input = int(input("Enter a answer between 1 to 4: "))
    if user_input == mcq_answer:
        mark = mark + 1
        score_in_letters.append("Right")
        box('Right', 'You got it right carry on with the good work!', 0)
    else:
        score_in_letters.append("Wrong")
        box('Wrong', 'Oops, you got it wrong, the correct answer is ' + words, 0)


def true_or_false(t_f_question, t_f_answer):

    global counter, mark, score_in_letters
    print(t_f_question)
    user_input = input("Please enter in capitals here: ")
    print()
    try:
        while user_input != "T" and user_input != "F":
            user_input = input("Please enter T for Truth and F for false: ")
    except ValueError:
        while user_input != "T" and user_input != "F":
            user_input = input("Please enter T for Truth and F for false: ")
    if user_input == t_f_answer:
        mark = mark + 1
        score_in_letters.append("Right")
        box('Right', 'You got it right keep up the good work! ', 0)
    else:
        box('Wrong', 'Oops, you got it wrong, the correct answer is ' + t_f_answer, 0)
        score_in_letters.append("Wrong")


intro()

true_or_false("Q1: I byte equals to 64 bits", "F")
true_or_false("Q2: I byte equals to 8 bits", "T")
true_or_false("Q3: Worms eat your computers hardware.", "F")
multiple_choice("Q4: Which of them are not malwares.", "1. Back doors", "2. Root kit", "3. Trojan ", "4. Copy kit", 4, "4. Copy Kit")
multiple_choice("Q5: Which of the following malwares create fake FBI notifications.", "1. Virus", "2. Ransomware", "3. Back Dorrs", "4. Rouge security software", 2, "2. Ransomware")
true_or_false("Q6: Monitor is a peripheral component not a hardware component.", "T")
multiple_choice("Q7: What is the full form of ISP", "1. International service provider", "2. Internet service provider", "3. Inportant service provider", "4. None of the above", 2, "2. Internet service provider")
multiple_choice("Q8: What is firewall", "1. A wall that protects you from fire", "2. It is a program that tells you where a fire is.", "3. It is a program that keeps you safe from people of the outside world trying to connect to your computer", "4. All of the above", 3, "3. It is a Program that keeps you safe from the people of the outside world trying to your computer.")
end()
