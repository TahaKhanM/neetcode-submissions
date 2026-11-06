class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = {}
        subL = 0
        subR = -1
        valid = True
        if len(t) > len(s):
            return ""
        
        for i in range(len(t)):
            c2 = s[i]
            if i <= len(t) - 1:
                c = t[i]
                if c not in td:
                    td[c] = 0
                td[c] += 1
            if c2 not in td:
                td[c2] = 0
            td[c2] -= 1


    
        l = 0 
        r = len(t) - 1

        for v in td.values():
            if v > 0:
                valid = False
    
        while r < len(s) and l < len(s):


            if valid:
                if r - l < (subR - subL) or (subR-subL) < 0:
                    subL = l
                    subR = r
                l += 1
                td[s[l-1]] += 1
            else:
                if r == len(s) - 1:
                    break
                r += 1
                if s[r] in td:
                    td[s[r]] -= 1
                else:
                    td[s[r]] = -1
            
            valid = True
            for v in td.values():
                if v > 0:
                    valid = False
        
        return s[subL:subR+1]


