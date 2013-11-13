# _*_ encoding: utf-8 _*_

import crawler
import string 
import unittest
import codecs


class TestLeTxt(unittest.TestCase):

	def setUp(self):
		_write("text")

	def test_open_txt_return_text_inside_file(self):
		assert crawler.open_txt("my.txt") == "text"


class TestRemovePunctuation(unittest.TestCase): # Remove punctuation

	def test_remove_comma(self):
		assert crawler.remove_punctuation("teste, teste") == "teste  teste"

	def test_remove_punctuation(self):
		assert crawler.remove_punctuation("tete.") == "tete "

	def test_remove_points_punctuation(self):
		# assert crawler.remove_punctuation("tete" + string.punctuation) == "tete"
		assert crawler.remove_punctuation("ronaldo.. ronaldo") == "ronaldo   ronaldo"

#class TestMoreMentioned(unittest.TestCase): # Discover who is more mentioned 
	
	#def say_who_is_more_mentioned(self):
		# TODO 

class TestReomveLessThan3(unittest.TestCase): # Remove less than 3

	def test_remove_less_than_3_words(self):
		assert crawler.remove_less_than_3("tete de de de de de") == "tete"

class TestCountWords(unittest.TestCase): # Count Words
	
	def test_count_words_an_tell_wich_most_apear_is_ronaldo(self):
		assert crawler.count_a_number_of_repetitions_and_say_who_is_more_mentioned("ronaldo ronaldo") == "ronaldo"

	def test_count_words_when_has_equal_mentions_and_say_which_most_appear_is_ronaldo(self):
		assert crawler.count_a_number_of_repetitions_and_say_who_is_more_mentioned("ronaldo  abc ronaldo abc") == "ronaldo"

class TestRemoveBreakLines(unittest.TestCase):
	
	def test_remove_break_lines(self):
		assert crawler.remove_break_lines('\nbcd') == "bcd"
		

class TestMostPopularWord(unittest.TestCase): # Most popular word in text

	def test_tell_the_most_popular_word_is_ronaldo(self):
		_write("ronaldo ronaldo")
		assert crawler.most_popular_word("my.txt") == "ronaldo"

	def test_tell_me_the_most_popular_word_is_ball(self):
		_write("ball house ball")
		assert crawler.most_popular_word("my.txt") == "ball"

	def test_tell_me_the_most_popular_word_is_ronaldo_removing_punctuation(self):
		_write(u"ronaldo ronaldo, ronaldo. pelé pelé")
		assert crawler.most_popular_word("my.txt") == "ronaldo"
	
	def test_tell_me_the_most_popular_word_is_ronaldo_removing_punctuation_and_words_with_less_than_3_chars(self):	
		_write(u"ronaldo de de de de de  ronaldo, de  ronaldo. de  pelé pelé")
		assert crawler.most_popular_word("my.txt") == "ronaldo"

	def test_unicode(self):
		_write(u'a abraço')
		assert crawler.most_popular_word("my.txt") == u'abraço'

	def test_new_line(self):
		_write('a\nbcd')
		assert crawler.most_popular_word("my.txt") == 'bcd'

def _write(str):
	output = codecs.open("my.txt", 'w', encoding='utf-8')
	output.write(str)
	output.close()

	
if __name__ == "__main__":
	unittest.main()