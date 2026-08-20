from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the #
            while s[j] != '#':
                j += 1

            # Get length of the string
            length = int(s[i:j])

            # Start and end of actual string
            start = j + 1
            end = start + length

            # Add string to result
            res.append(s[start:end])

            # Move to next encoded string
            i = end

        return res


# Test
solution = Solution()

strs = ["Hello", "World"]

encoded_string = solution.encode(strs)
print("Encoded:", encoded_string)

decoded_strs = solution.decode(encoded_string)
print("Decoded:", decoded_strs)