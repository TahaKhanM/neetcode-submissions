class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))] 
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        print(count)
        for num in count:
            print(num)
            print(buckets)
            buckets[count[num]-1].append(num)

        output = []
        #print(buckets)
        for i in range(len(buckets)- 1, -1, -1):
            while ((len(output) < k) and (buckets[i] != [])):
                
                output.append(buckets[i].pop(0))

        return output