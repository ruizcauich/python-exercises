"""Sam's house has an apple tree and an orange tree that
yield an abundance of fruit.

-----|-------|--------|-----|------
     a       s        t     b

- The s-t region denotes the Sam0s house.  The apple tree
is to the left of the house (a), and the orange tree is to
its right (b).

When a fruit falls from its tree, it lands d units of
distance from its tree of origin along the x-axis.

Negative value of d means the fruit fell d units to the
tree's left, and a positive value of d means it falls d units
to the tree's right.

Complete the count_apples_and_oranges function should print
the number of apples and oranges that land on Sam's house,
each on a separate line.

Given the value of d for m apples and n oranges, determine
how many apples and oranges will fall on Sam's house
(i.e., in the inclusive range [s,t] )?

https://www.hackerrank.com/challenges/apple-and-orange/
problem?isFullScreen=true&h_r=next-challenge&h_v=zen

ex012_test_case.txt contains the input for the function
"""

from utils.tests import mock_print

#
# Complete the 'count_apples_and_oranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    
    apples_in_house = 0
    oranges_in_house = 0
    for d in apples:
        if s <= (a+d) <= t:
            
            apples_in_house += 1

    for d in oranges:
        if s<= (b+d) <= t:
            
            oranges_in_house += 1
    
    
    print(apples_in_house)
    print(oranges_in_house)

if __name__ == '__main__':

    @mock_print
    def test_count_appeles_and_oranges(s, t, a, b, apples, oranges, mock):
        function_output = '18409\n19582'
        count_apples_and_oranges(s, t, a, b, apples, oranges)

        assert mock.getvalue()==function_output, "Shuold be\n" + function_output
        
        

    with open('ex012_test_case.txt', 'r') as file:
         
        lines = file.readlines()
        first_multiple_input = lines[0].rstrip().split()

        s = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        second_multiple_input = lines[1].rstrip().split()

        a = int(second_multiple_input[0])

        b = int(second_multiple_input[1])

        third_multiple_input = lines[2].rstrip().split()

        m = int(third_multiple_input[0])

        n = int(third_multiple_input[1])

        apples = list(map(int, lines[3].rstrip().split()))

        oranges = list(map(int, lines[4].rstrip().split()))

        test_count_appeles_and_oranges(s, t, a, b, apples, oranges)
