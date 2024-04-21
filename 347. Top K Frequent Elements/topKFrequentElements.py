# Bucket Sort
# 1. Count Frequencies: As before, count the frequency of each element using a dictionary.
# 2. Bucket Sort Frequencies: Create "buckets" where each bucket index represents a frequency, and the bucket stores the elements with that frequency.
#    - This is efficient because the maximum frequency cannot exceed the length of the array.
# 3. Collect Results: Traverse the buckets from highest to lowest frequency and collect elements until you have gathered k elements.
# 4. Complexity: This method is O(n) since you go through the array to build the frequency map, and then another pass to collect the top k elements from the buckets. The efficiency stems from the fact that frequency collection and bucket sorting directly correspond to the number of elements.

# For optimal performance given the constraints and the need for better than O(nlog n) complexity, the bucket sort method is usually the preferred approach because its complexity can approach O(n) in the best cases. However, for a moderate size of k, the heap approach is also very efficient and simpler to implement with existing library functions.

from collections import defaultdict
import itertools

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1 

        buckets = [[] for r in range(len(nums)+1)]
        for num, freq in frequency.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) -1, 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
                if len(result) >= k:
                    return result[:k]