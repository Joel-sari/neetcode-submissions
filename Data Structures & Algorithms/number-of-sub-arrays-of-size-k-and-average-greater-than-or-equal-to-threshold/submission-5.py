class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = 0
        result = 0
        windowSum = 0

        while r < len(arr):
            windowSum += arr[r]

            windowLen = r - l + 1
            if windowLen == k:
                temp = windowSum // windowLen
                if temp >= threshold:
                    result += 1
                windowSum -= arr[l]
                l += 1
            r += 1

        return result

