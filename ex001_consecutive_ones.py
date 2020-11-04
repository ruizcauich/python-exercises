# Given a list of numbers or other data types
# count the max consecutive "ones" in the list

def count_consecutive_ones(numbers_list):
    consecutive_max = 0
    consecutive_count = 0

    for index in range(0, len(numbers_list)):
        if(numbers_list[index] == 1):
            consecutive_count += 1
        else:
            consecutive_count = 0

        if consecutive_count > consecutive_max:
            consecutive_max = consecutive_count
    return consecutive_max
    # [1,4,5,1,1,1,6,7,1,1] -> max consecutive 3


print(count_consecutive_ones([1, 4, 5, 1, 1, 1, 6, 7, 1, 1]))
print(count_consecutive_ones(["string", -4, 4]))
print(count_consecutive_ones([0, 2, 4, 1, 3, 1, 1, 3, 0, 10, -2, -3, 1]))
print(count_consecutive_ones([1, 1, 1, 1, 3, 1, 1, 3, 0, 10, -2, -3, 1]))
print(count_consecutive_ones([0, 2, 4, 0, 3, 0, 0, 3, 0, 10, -2, -3, 0]))
print(count_consecutive_ones([]))
print(count_consecutive_ones([None, 1, 1, 0, 1]))
print(count_consecutive_ones([None]))
