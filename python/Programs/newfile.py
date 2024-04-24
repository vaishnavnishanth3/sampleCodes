
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

word = input("Enter your Word: ").lower()

new_word = ""

for n in range(len(word)):
		for i in alph:
			if i != word[n]:
				print(new_word+i)
			elif i == word[n]:
				new_word += i
				print(new_word)
				break
			if new_word == word:
				break
				print(new_word)