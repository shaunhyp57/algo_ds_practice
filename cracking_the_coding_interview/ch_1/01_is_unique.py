''' 
Cracking The Coding Interview: 
Ch 1 Arrays and Strings: 
Q1 - Is Unique
"Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?"

Solutions:      Time Complexity:
Brute Force     O(n^2)
Dictionary      O(n)
Set             O(n)
Alphabet String O(n)


Note: these assume that the input strings only include alphabet chars
      and that spaces are ignored
'''

import unittest

# remove spaces and lower case the string
def normalized(input_string):
    input_string = input_string.replace(" ", "")
    return input_string.lower()

# using nested for loop, compare each char in the string to each other 
# O(n^2)
def naive_is_unique(input_string):
    length = len(input_string)

    if length < 2:
        return True

    for i, c in enumerate(input_string):
        if i == length - 1:
            break
        for j in range(i+1, length):
            if input_string[j] == c:
                return False
    return True

# using dictionary, as you interate through the string, add to the dict.
# if char is in dict, return False 
# O(n)
def dict_is_unique(input_string):
    unique = {}

    for c in input_string:
        if c in unique:
            return False
        else:
            unique[c] = 1
    return True

# using a set, checks to see if the length of the set of the chars in the 
# string equal to the number of chars in the original string.
# if not equal, return False
# O(n)
def set_is_unique(input_string):
    if len(set(input_string)) == len(input_string):
        return True
    return False

# using no data structure, have a string with all letters of alphabet
# as you iterate through the input string, if the char is in the alphabet string, remove that
# char from the alphabet string. If the char is not in the alphabet string, 
# that means that is a duplicate, return False
# O(n)
def no_ds_is_unique(input_string):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for c in input_string:
        if c in letters:
            letters = letters.replace(c, "")
        else:
            return False
    return True


# --------------------------------------------------- TEST -----------------------------------------------------#


class Test(unittest.TestCase):
    
    data_t = ("n", "", "j i t", " n", " ji ", " j i t ", "pace")

    data_f = ("haPpY", "poll", "Cassie", "kiss", "peace", "sister", "ss ss")
    
    def test_is_unique(self):
        
        # true test
        for test_string in self.data_t:
            print(test_string)
            naive_result = naive_is_unique(normalized(test_string))
            self.assertTrue(naive_result)
            
            dict_result = dict_is_unique(normalized(test_string))
            self.assertTrue(dict_result)

            set_result = set_is_unique(normalized(test_string))
            self.assertTrue(set_result)

            no_ds_result = no_ds_is_unique(normalized(test_string))
            self.assertTrue(no_ds_result)
        
        # false test
        for test_string in self.data_f:
            print(test_string)
            naive_result = naive_is_unique(normalized(test_string))
            self.assertFalse(naive_result)
            
            dict_result = dict_is_unique(normalized(test_string))
            self.assertFalse(dict_result)

            set_result = set_is_unique(normalized(test_string))
            self.assertFalse(set_result)

            no_ds_result = no_ds_is_unique(normalized(test_string))
            self.assertFalse(no_ds_result)

if __name__ == "__main__":
    unittest.main()