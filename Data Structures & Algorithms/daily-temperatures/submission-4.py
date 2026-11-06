
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minstack = []
        results = [0] * len(temperatures)
        i = 0
        for temperature in temperatures:
            while minstack and temperature > minstack[-1][0]:
                results[minstack[-1][1]] = i - minstack[-1][1]
                minstack.pop()
            
            minstack.append((temperature, i))


            i += 1

        return results