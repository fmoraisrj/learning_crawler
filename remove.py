#! encoding: utf-8 
import string

def remove(txt):
	fruits = fruits.split()

	i = 0
	cleaned_fruits = []
	
	while i < len(fruits):
		if not (len(fruits[i]) < 3):
			cleaned_fruits.append(fruits[i])
		i += 1
	cleaned_fruits = string.join(cleaned_fruits, " ")
	return cleaned_fruits

print remove("tete de de de de de")