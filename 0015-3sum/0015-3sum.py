class Solution:
    def threeSum(self, nums: list):
        nums.sort()
        result = []

        for k in range(len(nums) - 2):
            # Skip duplicate numbers for k
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            p1, p2 = k + 1, len(nums) - 1
            while p1 < p2:
                total = nums[k] + nums[p1] + nums[p2]
                if total == 0:
                    result.append([nums[k], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    # Skip duplicates for p1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    # Skip duplicates for p2
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif total < 0:
                    p1 += 1
                else:
                    p2 -= 1

        return result
