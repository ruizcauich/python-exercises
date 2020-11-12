# You are given a string containing characters A and B only.
# Your task is to change it into a string such that there
# are no matching adjacent characters. To do this, you are
# allowed to delete zero or more characters in the string.

# Your task is to find the minimum number of required deletions.

# For example, given the string s= AABAAB, remove an A at positions
# 0 and 3 to make s=ABAB in 2 deletions.

# Taken from:
# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
# "AAAA" -> 3
# "BABABABA" -> 0
#  "BAABBA" -> 2

def alternate_AB_chars(string):
    counter = 0
    string_length = len(string)
    for index in range(string_length):
        if index == string_length-1:
            break

        if string[index] == string[index+1]:
            counter += 1
    return counter


if __name__ == "__main__":

    assert alternate_AB_chars("AAAA") == 3, 'Shuld be 3'
    assert alternate_AB_chars("BBBBB") == 4, 'Shuld be 4'
    assert alternate_AB_chars("ABABABAB") == 0, 'Shuld be 0'
    assert alternate_AB_chars("BABABA") == 0, 'Shuld be 0'
    assert alternate_AB_chars("AAABBB") == 4, 'Shild be 4'
