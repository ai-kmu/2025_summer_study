class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_appear_index = {char: i for i, char in enumerate(s)}        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):            
            if char in seen:
                continue                   
            # stack이 존재하고, 현재 글자가 스택 마지막 글자보다 작고, 스택 마지막 글자가 뒤에 또 나온다면 pop()
            while stack and char < stack[-1] and i < last_appear_index[stack[-1]]:            
                seen.discard(stack.pop())                         
            stack.append(char)
            seen.add(char)   
                 
        return "".join(stack)