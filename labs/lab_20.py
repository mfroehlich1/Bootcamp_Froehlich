
ccn = '4556737586899855'
ccn_list = []
# Convert the input string into a list of ints
for char in ccn:
    ccn_list.append(int(char))
# Slice off the last digit. That is the check digit.
checksum = ccn_list.pop(-1)
# Reverse the digits.
ccn_list.reverse()
# Double every other element in the reversed list.
for i, num in enumerate(ccn_list):
    if (i % 2) == 0:
        ccn_list[i] = num * 2
# Subtract nine from numbers over nine.
for i, num in enumerate(ccn_list):
    if num > 9:
        ccn_list[i] = num - 9
# Sum all values.
sum = 0
for num in ccn_list:
    sum += num
# Take the second digit of that sum.
sum_list = []
for char in str(sum):
    sum_list.append(int(char))
# If that matches the check digit, the whole card number is valid.
if sum_list[1] == checksum:
    print(f"Checksum: {checksum}\nCaculation: {sum_list[1]}\nThis is a valid CCN!")
