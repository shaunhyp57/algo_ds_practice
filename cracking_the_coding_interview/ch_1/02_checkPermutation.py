''' 
Cracking The Coding Interview: 
Ch 1 Arrays and Strings: 
Q2 - Check Permutation
"Given two strings, write a method to decide if one is a permutation of the other."

Solutions:      Time Complexity:
Brute Force     O(n log n)
Dictionary      O(n)


Note: this  implementation assumes that the input strings only include alphabet chars
      and that spaces are ignored
'''
import unittest

# sort both strings then compare char by char
# O(n log n)
def brute_checkPermutation(input_string1, input_string2):
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
# O 
def dict_checkPermutation(input_string1, input_string2):
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

    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )

    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_checkPermutatons(self):

        # true test
        for test_strings in self.dataT:
            brute_result = brute_checkPermutation(*test_strings)
            self.assertTrue(brute_result)

            dict_result = dict_checkPermutation(*test_strings)
            self.assertTrue(dict_result)

        # false test
        for test_strings in self.dataF:
            brute_result = brute_checkPermutation(*test_strings)
            self.assertFalse(brute_result)

            dict_result = dict_checkPermutation(*test_strings)
            self.assertFalse(dict_result)

if __name__ == "__main__":
    unittest.main()