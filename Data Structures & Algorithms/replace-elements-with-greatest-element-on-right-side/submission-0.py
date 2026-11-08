class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            highest = 0
            for j in range(i + 1, len(arr)):
                highest = max(highest, arr[j])
            arr[i] = highest
        arr[-1] = -1
        return arr