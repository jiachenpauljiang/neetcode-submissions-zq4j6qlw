class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            maxNum = max(arr[i + 1:])
            arr[i] = maxNum
        arr[-1] = -1
        return arr