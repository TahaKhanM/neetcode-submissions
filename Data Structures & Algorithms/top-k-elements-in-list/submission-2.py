class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 1) + 1 
       
            
        return sorted(count, key=lambda x: count.get(x), reverse=True)[:k]