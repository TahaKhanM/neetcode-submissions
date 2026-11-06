class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroProduct = False
        doubleZeroProduct = False
        for num in nums: 
            if (num != 0):
                product *= num
            elif (zeroProduct):
                doubleZeroProduct = True
            else:
                zeroProduct = True
        
        outputArr = []
        
        for num in nums:
            if (num == 0):
                if (doubleZeroProduct):
                    outputArr.append(0)
                else:
                    outputArr.append(product)
            else:
                if (zeroProduct):
                    outputArr.append(0)
                else:
                    outputArr.append(int(product/num))

        return outputArr