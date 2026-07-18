class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_of_occurrences = {}
        result = 0 

        left_p = 0 

        for right_p in range(len(s)):
            count_of_occurrences[s[right_p]]= 1+ count_of_occurrences.get(s[right_p], 0)

            while (right_p - left_p + 1) - max(count_of_occurrences.values()) > k:
                count_of_occurrences[s[left_p]] -= 1
                left_p += 1

            result = max(result, right_p - left_p + 1)
        return result

        