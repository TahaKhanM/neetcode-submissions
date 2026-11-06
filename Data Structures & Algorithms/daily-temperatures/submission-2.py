
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minstack = []
        results = [0 for x in range(len(temperatures) - 1)]
        i = 0
        for temperature in temperatures:
            while minstack and temperature > minstack[-1][0]:
                results[minstack[-1][1]] = i - minstack[-1][1]
                minstack.pop()
            
            minstack.append((temperature, i))


            i += 1
        results.append(0)
        return results