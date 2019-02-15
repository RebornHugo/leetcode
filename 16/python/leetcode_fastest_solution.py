class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        closest = []

        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, length - 1

            # different with others' solution

            if num + nums[r] + nums[r - 1] < target:
                closest.append(num + nums[r] + nums[r - 1])
            elif num + nums[l] + nums[l + 1] > target:
                closest.append(num + nums[l] + nums[l + 1])
            else:
                while l < r:
                    closest.append(num + nums[l] + nums[r])
                    if num + nums[l] + nums[r] < target:
                        l += 1
                    elif num + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        return target

        closest.sort(key=lambda x: abs(x - target))
        return closest[0]
