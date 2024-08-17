unit = input(
    "What unit would you like to view today's temperature in (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    if temp > 30:
        print("It's a hot day")
    elif temp > 20:
        print("It's a warm day")
    elif temp > 10:
        print("It's a bit cold")
    else:
        print("It's a cold day")

elif unit == "F":
    if temp > 86:
        print("It's a hot day")
    elif temp > 68:
        print("It's a warm day")
    elif temp > 50:
        print("It's a bit cold")
    else:
        print("It's a cold day")

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is: {temp}°C")
else:
    print(f"Sorry, {unit} is an invalid unit of measurement")
