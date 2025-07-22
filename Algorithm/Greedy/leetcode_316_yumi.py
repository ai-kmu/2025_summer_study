class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 인터넷 참고했어용
        counter = collections.Counter(s)
        stack = []

        for char in s:
            counter[char] -= 1

            if char in stack:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(char)
        return ''.join(stack)
