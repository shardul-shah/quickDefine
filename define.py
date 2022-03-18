import nltk
from nltk.corpus import words
nltk.download('words')
from nltk.metrics.distance import edit_distance

# TODO 1: user inserts sentence -> define each word in sentence (and keep only letters in sentence before defining)
# TODO 2: allow other grammar to exist in a word without being filtered out (not sure a good way to detect/keep such grammar for now)
	# for now, allowing most common used such character - the hyphen " - "
# TODO 3: allow autocorrect off option
# TODO 5: Add definitions based on libary from Python

def main():
	# only one word for now
	dictionaryWords = words.words()
	print("\n\nQuick Define App\n")

	while True:
		word = obtainProperWord()
		if (word not in dictionaryWords):
			userSuggestion = autocorrect(dictionaryWords, [word])
			if (userSuggestion[0] == 0):
				print("You have perfect spelling, no autocorrect suggestions recommended.\n")
				break
			else:
				autocorrectInput = input("Did you mean " + userSuggestion[1] + "? (y/n)\n\n")

			if autocorrectInput == 'n':
				continue
			else:
				print("Autocorrect successful.\n")
				break
		else:
			print("You have perfect spelling, no autocorrect suggestions recommended.\n")		
			break	
			

def obtainProperWord():
	wordIsCorrectFlag = False
	word = input("Enter a word:\n")	
	while wordIsCorrectFlag == False:
		word = word.strip()
		# print(word)
		wordParts = word.split("-")
		for index, wordPart in enumerate(wordParts):
			if wordPart.isalpha() == True:
				if index+1 == len(wordParts):
					wordIsCorrectFlag = True
			else:
				word = input("Please try and enter only proper dictionary words (typos accepted):\n")
				break
	return word

def autocorrect(dictionaryWords, inputWords):
	print("\nDetecting correct spelling...\n")
	userSuggestions = []
	for word in inputWords:
		# use list comprehension to simplify things
		distances = [(edit_distance(word, dictionaryWord, transpositions=False), dictionaryWord) for dictionaryWord in dictionaryWords] 
		# TODO 4: if dist = 0
		closest = min(distances)
		# print(closest)
		userSuggestions.append(closest)

	# only one word for now
	return userSuggestions[0]


if __name__ == '__main__':
	main()