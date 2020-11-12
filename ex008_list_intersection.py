
# Write a function that acepts an array as parametter (str_arr)
# str_arr will contains 2 elements, both are strings representing
# comma-separated numbes which are sorted in ascendin order.
# Your goal is return a comma-separeted string containing the
# numbers that occur in elements of str_arr in sorted
# ascending order
# https://coderbyte.com/editor/Find%20Intersection:Python3

# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1,4,13

# Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# Output: 1,9,10

def find_intersection(str_arr):
    # to manage number by number
    str_arr_one = [int(n) for n in str_arr[0].split(',')]
    str_arr_two = [int(n) for n in str_arr[1].split(',')]
    str_arr_result = []

    # The idea is to move each index
    # using only one loop
    index_one = 0
    index_two = 0
    # If the lenght of each array is different
    # then we need to have limits for each index
    index_one_limit = len(str_arr_one)
    index_two_limit = len(str_arr_two)

    # Since the elements are sorted in ascending order
    # it's possible to offset one or both of the
    # indexes looking for equal numbers in both
    # str_atrs (the elements that intersect).
    #
    # 1- if current elements are equals: offset by one
    #    both indexes (check the next)
    # 2- if the current element of the first str_arr
    #   is lower than the second: offset by one just
    #   the index_one
    # 3- if the current element of the second str_arr
    #   is lower than te first one: offset by one the
    #   index_two
    #
    # Iterate over and over checking the numbers
    # of each array until the limit of one of the
    # indexes is reached.
    while index_one < index_one_limit and index_two < index_two_limit:
        number_of_one = str_arr_one[index_one]
        number_of_two = str_arr_two[index_two]

        if number_of_one == number_of_two:
            str_arr_result.append(str(number_of_one))
            index_one += 1
            index_two += 1
            continue
        if number_of_one < number_of_two:
            index_one += 1
        elif number_of_one > number_of_two:
            index_two += 1

    return ','.join(str_arr_result)


if __name__ == "__main__":
    assert find_intersection(["1, 3, 4, 7, 13",
                             "1, 2, 4, 13, 15"]) == '1,4,13', 'Shuld be 1,4,13'

    assert find_intersection(["1, 3, 9, 10, 17, 18",
                              "1, 4, 9, 10"]) == '1,9,10', 'Shuld be 1,9,10'
