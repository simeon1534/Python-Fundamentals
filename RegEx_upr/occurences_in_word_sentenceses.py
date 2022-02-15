import re

data = input()
lowercased_data = data.lower()
given_word1 = input()
given_word=given_word1.lower()
pattern = r'\b{word}\b'.format(word=given_word)
variables = re.findall(pattern, lowercased_data)
print(len(variables))
