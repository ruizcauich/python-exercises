# A function that, given a list of integers (first parameter)
# and an integer (second parameter), returns if within the
# list there are two numbers, whose addition is equal to
# the second parameter


def find_operands(list, number):
    # To limit the iteration
    list_len = len(list)

    # indices are used to get list items and
    # check their sum.
    # index_two will always be greater than index_one
    index_one = 0
    index_two = 1

    if list_len < 2:
        return False

    while index_one < list_len and index_two < list_len:

        if list[index_one] + list[index_two] == number:
            return True

        # If index_two is in the end of the list
        # move index_one and set the value of index_two
        # as de next value
        if index_two == list_len-1:
            index_one += 1
            index_two = index_one + 1
        else:
            index_two += 1
    return False


if __name__ == "__main__":
    assert not find_operands([2, 4, 7, 3, 5, 1, 0], 17), "Should be False"
    assert find_operands([2, 4, 7, 3, 5, 1, 0], 10), "Should be True"
    assert find_operands([6, 7, 2, 12, 9, 3, 16], 19), "Should be True"
