class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_set = set(c for c in s)
        last_index = {c: i for i, c in enumerate(s)}
        seen = set()
        result = []

        for i, c in enumerate(s):
            if c in seen:
                continue
            while result and c < result[-1] and last_index[result[-1]] > i:
                removed = result.pop()
                seen.remove(removed)
            result.append(c)
            seen.add(c)

        return "".join(result)
