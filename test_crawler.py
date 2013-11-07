# _*_ encoding: utf-8 _*_

import crawler
import string 
import unittest

class TestCrawler(unittest.TestCase): # remove punctuation

	def test_remove_comma(self):
		assert crawler.remove_punctuation("teste, teste") == "teste teste"

	def test_remove_punctuation(self):
		assert crawler.remove_punctuation("tete.") == "tete"

	def test_remove_all_punctuation(self):
		assert crawler.remove_punctuation("tete" + string.punctuation) == "tete"
		assert crawler.remove_punctuation("ronaldo. ronaldo") == "ronaldo ronaldo"


class TestReomveLessThan3(unittest.TestCase): # remove less than 3

	def test_remove_less_than_3(self):
		assert crawler.remove_less_than_3("tete de") == "tete"

class count_words(unittest.TestCase):
	
	def test_count_words_an_tell_wich_most_apear(self):
		assert crawler.count_a_number_of_repetitions_and_say_who_is_more_mentioned("ronaldo ronaldo") == "ronaldo"

	def test_count_words_when_has_equal_mentions(self):
		assert crawler.count_a_number_of_repetitions_and_say_who_is_more_mentioned("ronaldo  abc ronaldo abc") == "ronaldo"

class TestPerfectWorld(unittest.TestCase):

	def test_tell_the_most_popular_word_is_ronaldo(self):
		assert crawler.most_popular_word("ronaldo ronaldo") == "ronaldo"

	def test_tell_me_the_most_popular_word_is_ball(self):
		assert crawler.most_popular_word("ball house ball") == "ball"

	def test_tell_me_the_most_popular_word_is_ronaldo_removing_punctuation(self):
		assert crawler.most_popular_word("ronaldo ronaldo, ronaldo. pelé pelé") == "ronaldo"
	
	def test_tell_me_the_most_popular_word_is_ronaldo_removing_punctuation_and_words_with_less_than_3_chars(self):	
		assert crawler.most_popular_word("ronaldo de de de de de  ronaldo, de  ronaldo. de  pelé pelé") == "ronaldo"
if __name__ == "__main__":
	unittest.main()