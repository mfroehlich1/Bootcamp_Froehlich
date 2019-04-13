from string import punctuation
from math import ceil


def get_word_char_count():

	with open('book.txt', 'r') as book:

		punctuation_list = list(punctuation)
		word_dict = {'Word Count': 0}
		char_dict = {'Character Count': 0}
		sentence_punc = ['!', '.', '?']
		sentence_count = 0

		for line in book:
			line1 = line.rstrip('\n').lower()

			for char in line:
				if char in sentence_punc:
					sentence_count += 1

			for punc in punctuation_list:
				line1 = line1.replace(punc, '')

			char_list = []
			for char in line1:
				char_list.append(char)
			for character in char_list:
				char_dict['Character Count'] += 1

			line1_list = line1.split()
			for word in line1_list:
				word_dict['Word Count'] += 1

	return word_dict['Word Count'], char_dict['Character Count'], sentence_count


def ari_calc(w, c, s):

	ari = (4.71 * (c / w)) + (0.5 * (w / s)) - 21.34

	ari = int(ceil(ari))

	return ari


def csv_to_dict(file_path):
	with open(file_path) as f:
		csv = []
		col_list = []
		for row in f:
			if not col_list:
				row = row.rstrip('\n')
				col_list = row.split(',')
				continue
			row = row.rstrip('\n')
			row_list = row.split(',')
			row_dict = dict(zip(col_list, row_list))
			csv.append(row_dict)

		return csv


def main():

	words, chars, sentences = get_word_char_count()

	print(f'\nWords: {words}\nCharacters: {chars}\nSentences: {sentences}\n')

	ari = ari_calc(words, chars, sentences)

	reading_level = csv_to_dict('reading_level.csv')

	for row in reading_level:
		if row['Score'] == str(ari):
			print(f'The ARI for The Picture of Dorian Grey is {ari}.\nThis corresponds to a {row["Grade Level"]} level of difficulty\nthat is suitable for an average person {row["Ages"]} years old.\n')


main ()
