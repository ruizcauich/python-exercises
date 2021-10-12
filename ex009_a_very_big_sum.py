"""In this challenge, you are required to calculate
and print the sum of the elements in an array, keeping
in mind that some of those integers may be quite large.

https://www.hackerrank.com/challenges/a-very-big-sum/problem?
isFullScreen=true

Input:[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
Output: 5000000015

Input: [1001458909, 1004570889, 1007019111, 1003302837, 1002514638,
 1006431461, 1002575010, 1007514041, 1007548981, 1004402249]

Output: 10047338126
"""

def a_very_big_sum(ar):
    """Sum the ar elments which are big integers which result would
    exceed the max value of a integer
    """
    # since python use a dyanamic typing we can use the sum
    # built in function
    # return sum(ar)

    # In order to create an algorithm that calculate the sum
    # of big integers for languages without dynamic typing; 
    # The next lines are a programmatic way of a clasic addition
    # by hand, where you have a to carry a number to the next column
    # if the current collumn sum is of two digits:
    #  135
    # + 86
    # =221
    
    def programmatic_stacked_sum(arr=[], carried_number=0):
        if len(arr) == 0:
            return '' if carried_number == 0 else carried_number

        # The digit at the end of each number
        tail_digits = [number%10 for number in arr]
        # Add the carried number of the previus process
        tail_digits.append(carried_number)
        # The number witout the tailing digit
        new_numbers = [number//10 for number in arr if number//10 >0]

        digits_sum = sum(tail_digits)

        result = f'{programmatic_stacked_sum(new_numbers, digits_sum//10)}{digits_sum%10}'
        
        return result

    return programmatic_stacked_sum(ar)


if __name__ == '__main__':
    print('Runing test cases')
    
    assert a_very_big_sum(
        [1000000001, 1000000002,
         1000000003, 1000000004,
         1000000005
        ]
    ) == '5000000015', 'Should be 5000000015'

    assert a_very_big_sum(
        [1001458909, 1004570889,
         1007019111, 1003302837, 
         1002514638, 1006431461,
         1002575010, 1007514041,
         1007548981, 1004402249
        ]
    ) == '10047338126', 'Should be 10047338126'

    print('Completed without error')