class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(arr, x, avoid):
            low = 0
            high = len(arr) - 1
            mid = 0
        
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    if mid == avoid:
                        return mid+1 if arr[mid+1] == arr[mid] else mid-1
                    return mid
            return -1
        
        for i in range(len(numbers)):
            j = binary_search(numbers,target-numbers[i],i)
            if j != -1:
                return [i+1,j+1]