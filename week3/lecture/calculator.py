def main():
    num1 = get_number()
    num2 = get_number()
    while True:
        try:
            user_function = input("Addition, division, multiplication or subtraction? ")
        except user_function.lower() != "addition" and "division" and "multiplication" and "subtraction":
            print("Please enter correct name of function, ensure spelling is correct")
        else:
            break
    match user_function.lower():
        case "addition": 
            print(addition(num1, num2))
        case "division":
            print(division(num1, num2))
        case "multiplication":
            print(multiplication(num1, num2))
        case "subtraction":
            print(subtraction(num1, num2))
        case _:
            print("Please enter")


def get_number():
    while True:
        try:
            return int(input("Number: "))
        except ValueError:
            print("Please enter intergers only...")


def addition(a, b):
    return a + b


def division(a, b):
    return round(float(a) / float(b), 2)


def multiplication(a, b):
    return a * b


def subtraction(a, b):
    return a - b


main()
