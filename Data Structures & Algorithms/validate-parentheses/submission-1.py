class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        st = []

        for c in s:
            if c in pairs:
                if not st or st.pop() != pairs[c]:
                    return False
            else:
                st.append(c)

        return not st