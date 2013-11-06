import crawler
import string 
import unittest

class TestCrawler(unittest.TestCase): # remove punctuation

	def test_remove_comma(self):
		assert crawler.remove_punctuation("te,te") == "tete"

	def test_remove_punctuation(self):
		assert crawler.remove_punctuation("tete.") == "tete"

	def test_remove_all_punctuation(self):
		assert crawler.remove_punctuation("tete" + string.punctuation) == "tete"

class TestReomveLessThan3(unittest.TestCase): # remove less than 3
	def test_remove_less_than_3(self):
		assert crawler.remove_less_than_3("tete de") == "tete"



if __name__ == "__main__":
	unittest.main()