class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i
            
        stack = []
        seen = set()

        for i in range(len(s)):
            c = s[i]
            if c in seen:
                continue
            while stack and c < stack[-1] and last_index[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(c)
            seen.add(c)

        return ''.join(stack)
