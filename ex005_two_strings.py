# Given two strings, determine if they share a common
# substring. A substring may be as small as one character.

# For example, the words "a", "and", "art" share the
# common substring . The words "be" and "cat" do not
# share a substring.

# Sample Input
# hello
# world
# hi
# world

# Sample Output
# YES
# NO

# Taken from:
# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


def share_substring(string_one, string_two):
    # True if there is only one char in common
    for char_one in string_one:
        for char_two in string_two:
            if char_one == char_two:
                return 'YES'
    return 'NO'


if __name__ == "__main__":
    assert share_substring('hello', 'world') == 'YES', 'Must be YES'
    assert share_substring('hi', 'world') == 'NO', 'Must be NO'
