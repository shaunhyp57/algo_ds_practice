''' 
Cracking The Coding Interview: 
Ch 1: Q1 - is Unique
"Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?"

Solutions:
Brute Force     O(n^2)
Dictionary      O(n)
Set             O(n)
Alphabet String O(n)

Note: this  implementation assumes that the input strings only include alphabet chars
      and that spaces are ignored
'''
import unittest

# remove spaces and lower case the string
def normalized(input_string):
    input_string = input_string.replace(" ", "")
    return input_string.lower()

# using nested for loop, compare each char in the string to each other 
# O(n^2)
def brute_isUnique(input_string):
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
def dict_isUnique(input_string):
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
def set_isUnique(input_string):
    if len(set(input_string)) == len(input_string):
        return True
    return False

# using no data structure, have a string with all letters of alphabet
# as you iterate through the input string, if the char is in the alphabet string, remove that
# char from the alphabet string. If the char is not in the alphabet string, 
# that means that is a duplicate, return False
# O(n)
def noDS_isUnique(input_string):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for c in input_string:
        if c in letters:
            letters = letters.replace(c, "")
        else:
            return False
    return True



# --------------------------------------------------- TEST -----------------------------------------------------#

class Test(unittest.TestCase):
    
    dataT = ("n", "", "j i t", " n", " ji ", " j i t ", "pace")

    dataF = ("haPpY", "poll", "Cassie", "kiss", "peace", "sister", "ss ss")
    
    def test_isUnique(self):
        
        # true test
        for test_string in self.dataT:
            print(test_string)
            brute_result = brute_isUnique(normalized(test_string))
            self.assertTrue(brute_result)
            
            dict_result = dict_isUnique(normalized(test_string))
            self.assertTrue(dict_result)

            set_result = set_isUnique(normalized(test_string))
            self.assertTrue(set_result)

            noDS_result = noDS_isUnique(normalized(test_string))
            self.assertTrue(noDS_result)
        
        # false test
        for test_string in self.dataF:
            print(test_string)
            brute_result = brute_isUnique(normalized(test_string))
            self.assertFalse(brute_result)
            
            dict_result = dict_isUnique(normalized(test_string))
            self.assertFalse(dict_result)

            set_result = set_isUnique(normalized(test_string))
            self.assertFalse(set_result)

            noDS_result = noDS_isUnique(normalized(test_string))
            self.assertFalse(noDS_result)

if __name__ == "__main__":
    unittest.main()