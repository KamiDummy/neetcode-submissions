class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        concs = []
        for item in nums:
            if item == 1: 
                n += 1
            else:
                concs.append(n)
                n = 0
            concs.append(n)
        return max(concs)
