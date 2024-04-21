# To solve the problem of grouping anagrams from a list of strings, we can use a dictionary to efficiently categorize and group strings that are anagrams of each other. Here's the step-by-step plan:

# 1. Create a Dictionary:
#    - Use a dictionary where each key is a sorted tuple of characters (which represents the canonical form of anagrams), and the value is a list of strings that, when sorted, equal this key.

# 2. Sort Each String:
#    - For each string in the input list, sort the string to normalize its order. This sorted string acts as the key in the dictionary.
#    - Convert the sorted string to a tuple, which ensures it can be used as a dictionary key (since lists cannot be used as dictionary keys due to their mutability).

# 3. Group Strings:
#    - Append the original string to the list corresponding to the sorted tuple key in the dictionary.
#    - By sorting the string and using it as a key, all anagrams will end up having the same key and thus be grouped together in the dictionary.

# 4. Extract Results:
#    - The final output can be obtained by returning all the values of the dictionary, which are the lists of grouped anagrams.

# This method leverages sorting and hashing (via dictionaries) to group the anagrams efficiently. The time complexity is primarily determined by the sorting step, making it O(nklogk), where n is the number of strings and k is the maximum length of a string in the list.



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)

        return list(anagrams.values())