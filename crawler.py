# _*_ encoding: utf-8 _*_

import string
import pdb
# texto = "como uma onde no mar, como uma onda no mar."


def count_a_number_of_repetitions_and_say_who_is_more_mentioned(txt):
	txt = txt.split() 
	counter_words = {}
	# Separa as palavra mais mencionadas e quantas vezes foram mencionadas em um dicionário
	for x in txt:
		if x in counter_words:
			counter_words[x] += 1
		else:
			counter_words[x] = 1

	# Descobre quem é o mais mencionado
	maxkey = ""	
	maxval = 0		
	for x in counter_words:
		if counter_words[x] > maxval:
			maxkey = x.title()
			maxval = counter_words[x]

	return string.lower(maxkey)
	


def remove_punctuation(txt):
	return txt.translate(None, string.punctuation)

def remove_less_than_3(txt):
	i = 0;
	txt = txt.split(" ")
	# pdb.set_trace()
	while i < len(txt):
		if len(txt[i]) < 3:
			txt.remove(txt[i])
		i += 1
	# Transformando list em uma string separada por spaço
	txt = string.join(txt, " ")
	return txt

def most_popular_word(txt):
	txt_without_punctuation = remove_punctuation(txt)
	txt_without_punctuation_and_less_than_3_words = remove_less_than_3(txt_without_punctuation)

	return count_a_number_of_repetitions_and_say_who_is_more_mentioned(txt_without_punctuation_and_less_than_3_words)	



