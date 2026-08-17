from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        d = Counter(t)
        c = {i: 0 for i in t}

        formed = 0
        required = len(d)

        ans = ""
        ans_len = float("inf")

        for right in range(len(s)):
            char = s[right]

            if char in c:
                c[char] += 1

                if c[char] == d[char]:
                    formed += 1

            while formed == required:
                if right - left + 1 < ans_len:
                    ans = s[left:right + 1]
                    ans_len = right - left + 1

                char = s[left]

                if char in c:
                    c[char] -= 1

                    if c[char] < d[char]:
                        formed -= 1

                left += 1

        return ans