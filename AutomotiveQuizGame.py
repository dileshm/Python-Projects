def new_game():
    guesses = []
    correct_guesses
    question_num = 1

    for key in questions:
        print("------------------")
        print(key)
    for in in options[question_num-1]:
        print(1)
    guess = input("Enter a b c or c")
    guess = guess.upper()
    guesses.append(guess)
    question_num += 1

    check_answer(answer, guess)

    if answer guess
        print correct
        return 1


def check_answer(a):
    pass


def display_score(correct_guesses, guesses):
    print("dmksmf")
    print("REsults")
    print(NDK)
    print(Answers end)
    for i in questions
    print(questions.get(1) end)

    for i in guesses
    print i end

    score intcorrect guess/len questions * 100


print your score is =score


def play_again():

    response = input(Do you want to play again") y or no
    response = response.upper()

    if response ==- yes
    return True
    else 
    return false
                     

#print

questions = {
    "What engine type does a Mazda RX-7 have? ": A
    "Is Mercedes Italian? ": C
    "What is AWD? ":C
    "When did Henry Ford build his first car?"D
    "Where was Toyota founded?"C
    "Why is it not the best idea to drive a powerful Rear Wheel Drive car in the snow? "B
    "How does a naturally aspirated engine function? "D
    "Who founded Honda? "B
}

options = (("A. A wankel/rotary engine", "B. A boxer engine", "C. A V6". "D. An Inline 6"),
          ("A. Yes", "B. No, it's American", "C. No, it's German". "D. No, it's Japanese")
          ("A. Automated Wax Dissolver", "B. All Wheel Discs", "C. All Wheel Drive". "D. Automatic Window Drivers")            
          ("A. 1896", "B. 1869", "C. 1912". "D. 1941")
          ("A. United Kingdom", "B. Italy", "C. Japan". "D. India")
          ("A. Because you'll have lots of grip", "B. Because it's easy to lose control of", "C. Because it doesn't clear the snow as easily". "D. Because it could ruin the road")            
          ("A. It uses atmospheric pressure to draw air into the cylinders", "B. It uses a turbo", "C. It naturally drives by itself". "D. The engine aspires to be faster")
          ("A. Enzo Ferarri", "B. Soichiro Honda", "C. Ferruccio Lamborghini", "D. Kiichiro Toyoda")
))

# new_game()

# while play_again(): 
#     new_game()

# print("Thanks for playing!")

