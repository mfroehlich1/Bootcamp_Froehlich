from string import punctuation

with open('book.txt', 'r') as book:

	punctuation_list = list(punctuation)
	word_dict = {}
	STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
				 "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
				 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs',
				 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is',
				 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
				 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
				 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
				 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
				 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
				 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
				 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
				 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn',
				 "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
				 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn',
				 "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

	for line in book:
		line1 = line.rstrip('\n').lower()
		for punc in punctuation_list:
			line1 = line1.replace(punc, '')

		line1_list = line1.split()

		for word in line1_list:
			if word in word_dict.keys():
				word_dict[word] += 1
			else:
				new_word = {word: 1}
				word_dict.update(new_word)

	for stopword in STOPWORDS:
		if stopword in word_dict.keys():
			del word_dict[stopword]

	# word_dict is a dictionary where the key is the word and the value is the count
	words_list = list(word_dict.items())  # .items() returns a list of tuples
	words_list.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
	for i in range(min(10, len(words_list))):  # print the top 10 words, or all of them, whichever is smaller
		print(words_list[i])

	a = 1
