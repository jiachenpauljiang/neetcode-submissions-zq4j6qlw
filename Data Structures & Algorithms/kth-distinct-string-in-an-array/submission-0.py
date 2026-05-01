class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        charToAppearance = {}

        for i in range(len(arr)):
            if arr[i] in charToAppearance.keys():
                charToAppearance[arr[i]] += 1
            else:
                charToAppearance[arr[i]] = 1
        print(charToAppearance)
        
        cur = 0
        for i in range(len(arr)):
            if charToAppearance[arr[i]] == 1:
                cur += 1
                if cur == k:
                    return arr[i]
        return ""