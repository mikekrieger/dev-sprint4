#Name: Michael Krieger

#Ex 11.9

def has_duplicates(t):
d = {}
for x in t:
	if x in d:
		return True
	d[x] = True
return False

def has_duplicates2(t):
	return len(set(t)) < len(t)

if __name__ == '__main__'
	t = [1, 2, 3]
	print has_duplicates(t)
	t.append(1)
	print has_duplicates(t)

	t = [1, 2, 3]
	print has_duplicates2(t)
	t.append(1)
	print has_dupicates2(t)

#Ex 11.10

from rotate import rotate_word

def make_word_dict():
	d = dict()
	fin = open('words.txt')
	for line in fin:
		word = line.strip().lower()
		d[word] = word

	return d

def rotate_pairs(word, word_dict):
	for i in range(1, 14):
		rotated = rotate_word(word, i)
		if rotated in word_dict:
			print word, i, rotated

if __name__ == '__main__'
	word_dict = make_word_dict()

	for word in word_dict:
		rotate_pairs(word, word_dict)