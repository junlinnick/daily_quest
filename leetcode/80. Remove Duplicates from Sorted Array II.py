class Solution:
    def removeDuplicates(self, nums) -> int:
        def solve(k):
            u = 0
            for x in nums:
                index = u - k
                target = nums[u-k]
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            return u
        return solve(2)


if __name__ == "__main__":
    s1 = Solution()
    nums=[1,1,1,1,1,2,2,2,2,3,3,4,4,5,5,5]
    nums2=[1,1,1,1,1,1,1]
    res = s1.removeDuplicates(nums)

