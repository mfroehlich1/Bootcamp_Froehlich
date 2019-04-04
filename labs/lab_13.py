# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m

# message = input("Input your phrase: ")
#
# charlist = []
#
# for letter in message:
#     charlist.append(chr(ord(letter) + 13))
#
# print(''.join(charlist))
#
# def rot13(index):
#     index = (index + 13) % 26
#     return index
#
#         cipher_message.append(chr(encoded_character))
#
#     return ''.join(cipher_message)
#
# secret = rot13("testing")
#
# print(secret)

message_dict = {}
cipher_dict = {}
cipher_list = []

for i in range(26):
    message_dict[i] = (chr(i + 97))
    cipher_dict[i] = (chr((i + 13) % 26 + 97))

print(message_dict)
print(cipher_dict)

message = input("Write your phrase: ")

for char in message:
    for k, v in message_dict.items():
        if char == v:
            for k in cipher_dict:
                cipher_list.append(cipher_dict[k])

print(cipher_list)
