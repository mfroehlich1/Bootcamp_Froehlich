import string


def rot13(message_input):
    alphabet_dict = {}
    punctuation = string.punctuation
    punctuation_list = []

    for item in punctuation:
        punctuation_list.append(item)

    for i in range(26):
        alphabet_dict[i] = chr(i + 97)
    cipher_list = []

    for char in message_input:
        if char != " ":
            if ord(char) >= 97 and ord(char) <= 122:
                alphabet_num = (ord(char))
                cipher_num = ((alphabet_num -97) + 13) % 26
                cipher_list.append(chr(cipher_num + 97))
            if ord(char) >= 65 and ord(char) <= 90:
                alphabet_num = (ord(char))
                cipher_num = ((alphabet_num - 65) + 13) % 26
                cipher_list.append(chr(cipher_num + 65))
        if char == ' ':
            cipher_list.append(char)
        for item in punctuation_list:
            if item == char:
                cipher_list.append(char)
        if char.isdigit():
            cipher_list.append(char)

    cipher_message = ''.join(cipher_list)
    return cipher_message


message = input("Input your message: ")

encrypted_message = rot13(message)

print(f"\n{encrypted_message}")
