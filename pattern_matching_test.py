import unittest
from pattern_matching import get_best_match

class GetBestMatchTestCase(unittest.TestCase):
	"""Tests for `get_best_match`."""

	def test_no_match1(self):
		"""If no match from non-empty patterns list, output is "NO MATCH"""

		patterns = ["*,b,*", "a,*,*", "*,*,c", "foo,bar,baz", "w,x,*,*", "*,x,y,z"]
		path = "foo/"

		self.assertEqual(get_best_match(patterns, path), "NO MATCH")

	def test_no_match2(self):
		"""If no match from empty patterns list, output is "NO MATCH"""

		patterns = []
		path = "foo/"

		self.assertEqual(get_best_match(patterns, path), "NO MATCH")


	def test_one_match1(self):
		"""When only one match with no wildcards"""

		patterns = ["a,b,c", "a,b,e" ,"a,b,d"]
		path = "a/b/d"

		self.assertEqual(get_best_match(patterns, path), "a,b,d")

	def test_one_match2(self):
		"""When only one match which also has wildcard"""

		patterns = ["a,b,c", "a,*,c" ,"a,*,*"]
		path = "a/b/d"

		self.assertEqual(get_best_match(patterns, path), "a,*,*")

	def test_tie_least_wildcards(self):
		"""When multiple matches but one has the least wildcards"""

		patterns = ["a,b,*", "a,b,c" ,"a,*,*"]
		path = "a/b/c"

		self.assertEqual(get_best_match(patterns, path), "a,b,c")


	def test_tie_same_num_wildcards1(self):
		"""When multiple matches and more than one have the least wildcards"""

		patterns = ["*,*,c,d", "*,b,c,*", "*,b,*,d"]
		path = "a/b/c/d/"

		self.assertEqual(get_best_match(patterns, path), "*,b,c,*")

	def test_tie_same_num_wildcards2(self):
		"""When multiple matches and more than one have the least wildcards"""
		
		patterns = ["p,*,i,*,*,t,r", "p,*,*,u,*,t,r", "p,*,i,*,y,t,*", "p,*,i,*,y,*,r"]
		path = "p/o/i/u/y/t/r/"

		self.assertEqual(get_best_match(patterns, path), "p,*,i,*,y,t,*")

	def test_tie_same_num_wildcards3(self):
		"""When multiple matches and more than one have the least wildcards"""
		
		patterns = ["p,*,i,*,*,t,r", "p,*,*,u,y,t,r", "p,*,i,*,y,t,*", "p,*,i,*,y,*,r"]
		path = "p/o/i/u/y/t/r/"

		self.assertEqual(get_best_match(patterns, path), "p,*,*,u,y,t,r")

	def test_tie_same_num_wildcards4(self):
		"""When multiple matches and more than one have the least wildcards"""
		
		patterns = ["p,*,i,*,*,*,*,e,v,*,x,*", "p,*,i,*,*,*,*,e,v,c,*,*", "p,*,i,*,*,*,*,e,v,*,*,s"]
		path = "p/o/i/u/y/t/r/e/v/c/x/s/"

		self.assertEqual(get_best_match(patterns, path), "p,*,i,*,*,*,*,e,v,c,*,*")


if __name__ == '__main__':
    unittest.main()
