''' 
Cracking The Coding Interview: 
Ch 1 Arrays and Strings: 
Q2 - Check Permutation
"Given two strings, write a method to decide if one is a permutation of the other."

Solutions:      Time Complexity:
Brute Force     O(n log n)
Dictionary      O(n)


Note: these assume that the input strings only include alphabet chars
      and that spaces are ignored
'''

import unittest

# sort both strings then compare char by char
# O(n log n)
def naive_check_permutation(input_string1, input_string2):
    if len(input_string1) != len(input_string2):
        return False

    sorted1 = sorted(input_string1)
    sorted2 = sorted(input_string2)

    for i, c in enumerate(sorted1):
        if c != sorted2[i]:
            return False
    return True

# using dictionary, hash str1 then check if contents of str2 are in dictionary
# if not or the dict is not empty at the end, return False
# O(n)
def dict_check_permutation(input_string1, input_string2):
    if len(input_string1) != len(input_string2):
        return False

    check_perm = {}

    for c in input_string1:
        if c in check_perm:
            check_perm[c] += 1
        else:
            check_perm[c] = 1

    for c in input_string2:
        if c in check_perm:
            if check_perm[c] > 1:
                check_perm[c] -= 1
            else:
                check_perm.pop(c)
        else:
            return False

    if check_perm:
        return False
    
    return True


# --------------------------------------------------- TEST ----------------------------------------------------------#


class Test(unittest.TestCase):

    data_t = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )

    data_t = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_check_permutaton(self):

        # true test
        for test_strings in self.data_t:
            naive_result = naive_check_permutation(*test_strings)
            self.assertTrue(naive_result)

            dict_result = dict_check_permutation(*test_strings)
            self.assertTrue(dict_result)

        # false test
        for test_strings in self.data_f:
            naive_result = naive_check_permutation(*test_strings)
            self.assertFalse(naive_result)

            dict_result = dict_check_permutation(*test_strings)
            self.assertFalse(dict_result)

if __name__ == "__main__":
    unittest.main()