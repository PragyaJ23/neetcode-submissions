class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0

        for right in range(len(s)):

            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Find maximum frequency
            max_freq = max(count.values())

            # Current window length
            window_length = right - left + 1

            # If too many replacements needed, shrink window
            while window_length - max_freq > k:
                count[s[left]] -= 1
                left += 1

                max_freq = max(count.values())
                window_length = right - left + 1

            # Store maximum valid substring
            result = max(result, window_length)

        return result

        