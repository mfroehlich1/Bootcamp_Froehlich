# x = 67
# tens_digit = x//10
# ones_digit = x%10

teens_dict = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    }

tens_dict = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
    }

ones_dict = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    }

user_input = int(input("Using numbers, pick a number between 0-99: "))

if user_input == 0:
    print("zero")

elif user_input in teens_dict:
    for key in teens_dict:
        if key == user_input:
            print(teens_dict[key])

elif user_input in ones_dict:
    for key in ones_dict:
        if key == user_input:
            print(ones_dict[key])

else:
    tens_digit = user_input // 10
    ones_digit = user_input % 10

    print(f"{tens_dict[tens_digit]}{ones_dict[ones_digit]}")
