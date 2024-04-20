
# To solve this problem, we can use several methods to check for duplicate values in the list. Here are the main approaches:

# 1. Using a Set:
#    - Iterate through the list and add each element to a set.
#    - Before adding, check if the element is already in the set.
#    - If the element is found in the set, it means there's a duplicate, and we return `True`.
#    - If the loop completes without finding duplicates, return `False`.
#    - This approach is efficient with a time complexity of O(n) and space complexity also O(n) in the worst case, where n is the length of the array.

# 2. Sorting the List:
#    - Sort the list first.
#    - Then, iterate through the sorted list and check consecutive elements for equality.
#    - If any two consecutive elements are equal, return `True` as it indicates a duplicate.
#    - This approach has a time complexity of O(n log n) due to sorting and a space complexity of O(1) if the sorting is done in place.

# 3. Using Dictionary:
#    - Similar to using a set, but using a dictionary to count occurrences.
#    - This approach provides the same performance as the set but allows further manipulation if we need more than just the existence of duplicates (like counting occurrences).

# For this task, the first approach using a set is ideal because it offers a good balance between time complexity and straightforward implementation. It directly checks for the existence of duplicates without additional overhead.

# I will proceed with this approach to implement the function in the Python Code Interpreter.

# I've written the function `containsDuplicate` which checks for duplicates in a list using a set. This method is efficient, with a time complexity of O(n), where n is the number of elements in the list.

# Here's a quick overview of the function:
# - It initializes an empty set called `seen`.
# - It iterates through each number in the list `nums`.
# - If a number is already in the `seen` set, it returns `True`, indicating a duplicate exists.
# - If not, it adds the number to the `seen` set.
# - If the loop completes without finding any duplicates, it returns `False`.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
