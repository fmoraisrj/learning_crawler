# _*_ encoding: utf-8 _*_

import string
import pdb
import codecs
import re


def open_txt(file_name):
	f = codecs.open(file_name, 'r' , encoding = 'utf-8')
	return f.read()

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

def remove_break_lines(txt):
	txt =  txt.replace("\n", " ")
	return string.strip(txt)
	


def remove_punctuation(txt):
	return re.sub("[?.!,\"\'\n()]", " ", txt)
	

def remove_less_than_3(txt):
	i = 0
	cleaned_txt = []
	txt = txt.split()

	while i < len(txt):
		if not (len(txt[i]) < 3):
			cleaned_txt.append(txt[i])
		i += 1
	cleaned_txt = string.join(cleaned_txt, " ")
	return cleaned_txt


def most_popular_word(file_name):
	txt = open_txt(file_name)
	txt_without_break_lines = remove_break_lines(txt)
	txt_without_punctuation = remove_punctuation(txt_without_break_lines)
	txt_without_punctuation_and_less_than_3_words = remove_less_than_3(txt_without_punctuation)

	return count_a_number_of_repetitions_and_say_who_is_more_mentioned(txt_without_punctuation_and_less_than_3_words)	



