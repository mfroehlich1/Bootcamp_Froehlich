

def rot13(message_input):
    alphabet_dict = {}

    for i in range(26): # generates my dictionary of the alphabet
        alphabet_dict[i] = chr(i + 97)
    cipher_list = []

    for char in message_input:
        if ord(char) >= 97 and ord(char) <= 122: # matches lowercase letters
            alphabet_num = (ord(char))
            cipher_num = ((alphabet_num - 97) + 13) % 26
            cipher_list.append(chr(cipher_num + 97))
        elif ord(char) >= 65 and ord(char) <= 90: # matches capital letters
            alphabet_num = (ord(char))
            cipher_num = ((alphabet_num - 65) + 13) % 26
            cipher_list.append(chr(cipher_num + 65))
        else: # anything that isn't matched above is kept as-is and added to list
            cipher_list.append(char)

    cipher_message = ''.join(cipher_list)
    return cipher_message


message = input("Input your message: ")

encrypted_message = rot13(message)

print(f"\n{encrypted_message}")
