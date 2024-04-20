# To determine if one string is an anagram of another, there are several approaches that we can take:

# 1. Sorting Method:
#    - Sort both strings and compare them. If the sorted strings are equal, then one string is an anagram of the other.
#    - Time complexity: O(nlogn) due to the sorting step, where n is the length of the strings.

# 2. Character Count Method:
#    - Use a frequency counter (like a dictionary) to count the occurrences of each character in both strings.
#    - Compare the frequency counts. If they are identical, then the strings are anagrams of each other.
#    - Time complexity: O(n), where n is the length of the strings.

# 3. Array Count Method (Optimized for English Letters):
#    - Use a fixed-size list of 26 elements to count occurrences of each character, assuming the input is restricted to lowercase English letters.
#    - Increment the count for each character in the first string and decrement for each character in the second string.
#    - Finally, check if all counts are zero. If they are, the strings are anagrams.
#    - Time complexity: O(n), with a potentially lower constant time than the dictionary-based method due to direct array indexing.

# I've implemented the isAnagram function using the character count method with a dictionary:

# - First, the function checks if the strings 's' and 't' have the same length. If not, it returns 'False' immediately.
# - Then, it uses a dictionary 'char_count' to count the occurrences of each character in the string 's'.
# - As it iterates through the string 't', it decrements the count of each character in the dictionary.
#   - If a character in 't' is not found in the dictionary or its count goes below zero, it indicates that 't' is not an anagram of 's', and the function returns 'False'.
# - After processing both strings, if all values in the dictionary are zero, the function returns 'True', indicating that 't' is an anagram of 's'.



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count < 0:
                    return False
            else:
                return False
            
        return all(count == 0 for count in char_count.values())
