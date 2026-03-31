class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        left, right = 0, n-1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]: ## minimum is in right == left is ascending
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: ## minimum is in left == right is ascending
                if nums[mid] < target <= nums[right]: # target in left
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

