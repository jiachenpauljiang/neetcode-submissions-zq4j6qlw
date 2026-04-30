class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            curNum = nums1[i]
            index_in_nums2 = nums2.index(curNum)
            subset_nums2 = nums2[index_in_nums2 + 1:]

            for num in subset_nums2:
                if num > curNum:
                    res[i] = num
                    break

        return res