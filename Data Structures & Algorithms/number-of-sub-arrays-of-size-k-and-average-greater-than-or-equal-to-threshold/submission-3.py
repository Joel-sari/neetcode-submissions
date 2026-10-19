class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = 0
        result = 0
        windowSum = 0

        while r < len(arr):
            windowSum += arr[r]

            if r - l + 1 > k:
                windowSum -= arr[l]
                l += 1

            if r - l + 1 == k:
                temp = windowSum // (r - l + 1)
                if temp >= threshold:
                    result += 1
            r += 1

        return result

