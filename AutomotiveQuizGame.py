print("Welcome to 'The Automotive Quiz'!")

questions = ("What engine type does a Mazda RX-7 have?: ",
             "Is Mercedes Italian?: ",
             "What is AWD?: ",
             "When did Henry Ford build his first car?: ",
             "Where was Toyota founded?: ",
             "Why is it not the best idea to drive a powerful Rear Wheel Drive car in the snow?: ",
             "How does a naturally aspirated engine function?: ",
             "Who founded Honda?: ")

options = (("A. A wankel/rotary engine", "B. A boxer engine", "C. A V6", "D. An Inline 6"),
           ("A. Yes.", "B. No, it's American.",
            "C. No, it's German.", "D. No, it's Japanese."),
           ("A. Automated Wax Dissolver", "B. All Wheel Discs",
            "C. All Wheel Drive", "D. Automatic Window Drivers"),
           ("A. 1896", "B. 1869", "C. 1912", "D. 1941"),
           ("A. United Kingdom", "B. Italy", "C. Japan", "D. India"),
           ("A. Because you'll have lots of grip.", "B. Because it's easy to lose control of.",
            "C. Because it doesn't clear the snow as easily.", "D. Because it could ruin the road."),
           ("A. It uses atmospheric pressure to draw air into the cylinders.", "B. It uses a turbo.",
            "C. It naturally drives by itself.", "D. The engine aspires to be faster."),
           ("A. Enzo Ferrari", "B. Soichiro Honda", "C. Ferruccio Lamborghini", "D. Kiichiro Toyoda"))

answers = ("A", "C", "C", "A", "C", "B", "A", "B")

while True:
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("-----------------------------------------------------------------------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            print("CORRECT!")
            score += 1
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")

        question_num += 1

    print("---------------------------------------------------------------")
    print("---------------------------RESULTS-----------------------------")
    print("---------------------------------------------------------------")

    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break
