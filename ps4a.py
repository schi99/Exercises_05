# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

from typing import List


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    pass  # Remove this and replace with your code here


def test_get_permutation(input_sequence: str, expected_output: List):
    """
    Test your `get_permutations` function by calling this function 
    and passing an input_sequence and your expected output. If the 
    actual output from the function matches the expected output, 
    the function will print True to the output.

    Parameters
    ----------
    input_sequence : a string sequence to test your function with.
    expected_output : the output that is expected from your function.

    Returns
    -------
    None.
    """

    print(f"Input: {input_sequence}")
    
    actual_output = get_permutations(input_sequence)

    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {actual_output}")
    print(f"Are ouputs same? {actual_output == expected_output}")


if __name__ == '__main__':
    test_get_permutation('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # Add three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for 
    # a sequence of length n)
    pass  # Remove this and replace with your code here