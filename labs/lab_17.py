

def palindrome_check(input):
    letter_list = []
    for letter in input:
        letter_list.append(letter)
    letter_list.reverse()

    if input == ''.join(letter_list):
        print(f"\n{input} is a palindrome.")
    else:
        print(f"\n{input} isn't a palindrome.")


def anagram_check(input, input2):
    anagram_check = []
    anagram_check2 = []
    input = input.replace(' ', '')
    input2 = input2.replace(' ', '')

    for letter in input:
        anagram_check.append(letter)

    for letter in input2:
        anagram_check2.append(letter)

    anagram_check.sort()
    anagram_check2.sort()

    if ''.join(anagram_check) == ''.join(anagram_check2):
        print(f"\n{input} and {input2} are anagrams.")
    else:
        print(f"\n{input} and {input2} are not anagrams.")

user_input = input("Write a word or phrase: ").lower()
user_input2 = input("\nWrite another word or phrase: ").lower()

palindrome_check(user_input)

anagram_check(user_input, user_input2)
