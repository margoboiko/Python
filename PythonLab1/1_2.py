import string

str = input('Enter string: ')
words = [word.strip(string.punctuation) for word in str.split()]
maximum = max(words, key=len)
for word in words:
	if len(word)==len(maximum):
		str = str.replace(word, '')

print("New string: ", str)
