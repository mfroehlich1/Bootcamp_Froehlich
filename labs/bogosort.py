import random


def random_list(n):
	rand_list = []
	for _ in range(n):
		random_num = random.randint(1, 99)
		rand_list.append(random_num)
	return rand_list


def shuffle_list(b_list):
	random.shuffle(b_list)
	return b_list


def is_sorted(b_list):
	for i, n in enumerate(b_list):
		try:
			if n > b_list[i + 1]:
				return False
		except IndexError:
			return True


def main():
	bogo_list = random_list(15)
	print(bogo_list)
	counter = 0

	while True:
		bogo_list = shuffle_list(bogo_list)
		counter += 1
		if is_sorted(bogo_list):
			break

	print(bogo_list)
	print(counter)


main()
