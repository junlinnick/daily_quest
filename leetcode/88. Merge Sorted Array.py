class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        nums1_cp = nums1.copy()
        index_a=0
        index_b = 0
        index_total = 0

        while index_a < m and index_b < n :
            if  nums1_cp[index_a] <= nums2[index_b]:
                nums1[index_total]=nums1_cp[index_a]
                index_a += 1
            else:
                nums1[index_total]=nums2[index_b]
                index_b +=1
            index_total += 1
        while index_a < m:
            nums1[index_total]=nums1_cp[index_a]
            index_a += 1
            index_total+=1

        while index_b < n:
            nums1[index_total]=nums2[index_b]
            index_b +=1
            index_total+=1