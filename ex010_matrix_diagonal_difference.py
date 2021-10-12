"""Given a square matrix, calculate the absolute difference
between the sums of its diagonals.

https://www.hackerrank.com/challenges/diagonal-difference/
problem?isFullScreen=true&h_r=next-challenge&h_v=zen

Input: [[11, 2, 4],
        [4,  5, 6],
        [10, 8, -12]]

Output: 15   
"""

def diagonal_difference(arr):
    """Calculate the absolute difference between the sum of
    the diagonals of a square matrix
    """
    matrix_length = len(arr)

    first_diagonal_sum = 0
    second_diagonal_sum = 0


    for offset in range(matrix_length):
        first_diagonal_sum += arr[offset][offset]
        second_diagonal_sum += arr[offset][matrix_length-1-offset]

    return abs(first_diagonal_sum - second_diagonal_sum)



if __name__ == '__main__':
    print("Running test cases")

    matrix = [
        [11, 2, 4],
        [4,  5, 6],
        [10, 8, -12]
    ] 

    assert diagonal_difference(matrix) == 15, "Should be 15"

    print("Completed without errors")
