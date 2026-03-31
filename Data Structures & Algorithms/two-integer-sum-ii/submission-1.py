class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                sum = numbers[i] + numbers[j]
                if (sum == target):
                    return [i + 1, j + 1]
        return [-1, -1]