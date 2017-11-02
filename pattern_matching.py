def get_best_match(patterns, path):
	"""Get the best matching pattern for a path from a list of patterns.
		
		If there are multiple matches, chose the pattern with the least
		wildcards(*). If there are multiple matches with the least number 
		of wildcards, pick one with leftmost wildcard further to the right.
	Args:
		patterns: A list of strings of patterns, e.g. ["*,b,*", "a,*,*"]
		path: A string, slash seperated path e.g. "a/b/c"
	Returns:
		A string that is the pattern that best matches the path. 
	"""

	matches = [p for p in patterns if does_match(p, path)]

	if len(matches) == 0:
		return "NO MATCH"

	min_wild = min((m.count("*") for m in matches))

	matches = [m for m in matches if m.count("*") == min_wild]

	if len(matches) == 1 or min_wild == 0:
		return matches[0]

	return max(((m.split(",").index("*"), m) for m in matches))[1]


def does_match(pattern, path):
	"""Tell whether the pattern matches the path.
	
		A pattern matches a path if every field in the pattern exactly 
		matches the corresponding field in the path. If a field
		is a wildcard(*), it matches with any other character.
	Args:
		pattern: A string, comma seperated pattern e.g. "a,b,c"
		path: A string, slash seperated path e.g. "a/b/c" 
	Returns:
		A boolean of whether the pattern matches the path.
	"""

	pattern = pattern.split(",")
	path = path.strip("/").split("/")

	if len(pattern) != len(path):
		return False

	for i in xrange(len(pattern)):
		if (pattern[i] != "*" and path[i] != "*") and pattern[i] != path[i]:
			return False

	return True


if __name__ == "__main__":

	patterns = [raw_input() for _ in xrange(int(raw_input()))]
	paths = [raw_input() for _ in xrange(int(raw_input()))]

	for path in paths:
		print get_best_match(patterns, path)
