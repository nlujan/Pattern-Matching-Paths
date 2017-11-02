# Pattern-Matching Paths # 

## Description

Given two lists: the first is a list of patterns, the second
is a list of slash-separated paths, it prints, for each path,
the pattern which best matches that path. ("Best" is defined more
rigorously below, under "Output Format".)

A pattern is a comma-separated sequence of non-empty fields. For a
pattern to match a path, every field in the pattern must exactly match
the corresponding field in the path. (Corollary: to match, a pattern and
a path must contain the same number of fields.) For example: the pattern
`x,y` can only match the path `x/y`. Note, however, that leading and
trailing slashes in paths should be ignored, thus `x/y` and `/x/y/` are
equivalent.

Patterns can also contain a special field consisting of a *single
asterisk*, which is a wildcard and can match any string in the path.

For example, the pattern `A,*,B,*,C` consists of five fields: three
strings and two wildcards. It will successfully match the paths
`A/foo/B/bar/C` and `A/123/B/456/C`, but not `A/B/C`,
`A/foo/bar/B/baz/C`, or `foo/B/bar/C`.


## Input Format

The first line contains an integer, N, specifying the number of
patterns. The following N lines contain one pattern per line where every 
pattern is unique. The next line contains a second integer,
M, specifying the number of paths. The following M lines contain one
path per line. Only ASCII characters appear in the input.


## Output Format

For each path encountered in the input, it prints the *best-matching
pattern*. The best-matching pattern is the one which matches the path
using the fewest wildcards.

If there is a tie (that is, if two or more patterns with the same number
of wildcards match a path), it prefers the pattern whose leftmost wildcard
appears in a field further to the right. If multiple patterns' leftmost
wildcards appear in the same field position, this rule is applied recursively
to the remainder of the pattern.

For example: given the patterns `*,*,c` and `*,b,*`, and the path
`/a/b/c/`, the best-matching pattern would be `*,b,*`.

If no pattern matches the path, it prints `NO MATCH`.


## Example Input

    6
    *,b,*
    a,*,*
    *,*,c
    foo,bar,baz
    w,x,*,*
    *,x,y,z
    5
    /w/x/y/z/
    a/b/c
    foo/
    foo/bar/
    foo/bar/baz/


## Example Output

    *,x,y,z
    a,*,*
    NO MATCH
    NO MATCH
    foo,bar,baz


## How To Run

    cat input_file | python your_program.py > output_file
