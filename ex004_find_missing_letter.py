# Find the missing letter
# Write a method that takes an array of consecutive (increasing)
# letters as input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always
# exactly one letter be missing. The length of the array will
# always be at least 2.
# The array will always contain letters in only one case.
# Example:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)
# Returns '' if there is no missin letter


def find_missing_letter(list):
    current_index = 0
    next_index = 1

    list_len = len(list)
    result = ''

    while current_index < list_len and next_index < list_len:
        # The numeric ASCII value of each letter
        ascii_current_char = ord(list[current_index])
        ascii_next_char = ord(list[next_index])

        # Finding a difference greater than 1 means the
        # next element is not the next char in the alphabet
        if ascii_next_char - ascii_current_char > 1:
            result = chr(ascii_current_char+1)
            break

        # Always check consecutive elements
        current_index += 1
        next_index += 1

    return result


if __name__ == "__main__":
    assert find_missing_letter(['a', 'b', 'c', 'e', 'f']) == 'd', "Sholud be e"
    assert find_missing_letter(['A', 'C', 'D', 'E', 'F']) == 'B', "Sholud be B"
    assert find_missing_letter(['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P'
                                ]) == 'N', "Sholud be N"
