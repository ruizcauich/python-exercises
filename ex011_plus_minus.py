"""Given an array of integers, calculate the ratios
of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line
with  places after the decimal.

https://www.hackerrank.com/challenges/plus-minus/
problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Input:[1, 1, 0, -1, -1]
Output: 0.400000
        0.400000
        0.200000

Input: [-4, 3, -9, 0, 4, 1]
Output: 0.500000
        0.333333
        0.166667

Output Format

Print the following 3 lines, each to 6 decimals:

proportion of positive values
proportion of negative values
proportion of zeros
"""

from utils.tests import mock_print

def plus_minus(arr):
    """Calculates and prints the ratio of positives, negatives,
    and zeros in a number list
    """

    list_length = len(arr)
    
    positives_count = len(list(filter(lambda x: x>0, arr)))
    negatives_count = len(list(filter(lambda x: x<0, arr)))
    zeros_count = arr.count(0)
    

    print(f'{positives_count/list_length:.6f}')
    print(f'{negatives_count/list_length:.6f}')
    print(f'{zeros_count/list_length:.6f}')


if __name__ == '__main__':

    @mock_print
    def test_plus_minus(arr, spected, mock):
        plus_minus(arr)
        assert mock.getvalue()==f'{spected}\n', 'Should be ' + spected

    
    function_input = [1, 1, 0, -1, -1]
    function_output = '0.400000\n' '0.400000\n' '0.200000'
    test_plus_minus(function_input, function_output)
    
    function_input = [-4, 3, -9, 0, 4, 1]
    function_output = '0.500000\n' '0.333333\n' '0.166667'
    test_plus_minus(function_input, function_output)

    

    
    
