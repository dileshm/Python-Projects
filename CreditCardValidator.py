print("---------------------------------------------------------------")
print("----------------------CREDIT CARD VALIDATOR--------------------")
print("---------------------------------------------------------------")

while True:
    sum_odd_digits = 0
    sum_even_digits = 0
    total = 0

    # Test Credit Card Account Numbers:
    # American Express: 378282246310005
    # MasterCard: 5555555555554444
    # Visa: 4111111111111111

    card_number = input("Enter a credit card #: ")
    card_number = card_number.replace("-", "")
    card_number = card_number.replace(" ", "")
    card_number = card_number[::-1]
    print(card_number)
# add all digits in the odd places from right to left
    for x in card_number[::2]:
        sum_odd_digits += int(x)
# double every second digit from right to left
    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1 + (x % 10))
        else:
            sum_even_digits += x

    total = sum_odd_digits + sum_even_digits

    if total % 10 == 0:
        print("VALID")
        break
    else:
        try_again = input("INAVLID, TRY AGAIN? (yes/no): ").lower()
        if try_again != "yes":
            break

print("Thank you for using this service!")
