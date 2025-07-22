from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):

        stack = [] # 사전순 정렬 만족하는 문자 저장용 스택
        count = Counter(s) # 문자열에서 문자 등장 횟수 카운트
        visited = set() # 현재 스택 안에 있는 문자 확인용(시간복잡도 O(1))

        for ch in s:
            count[ch] -= 1 # 쓸거니까 일단 -1로 카운터에서 한개 빼줌

            if ch in visited: # 이미 스택에 있다는 뜻 중복 제거 조건에 따라 다시 추가 안함 
                continue
            
            # 3가지 조건 만족 시, 현재 스택에서 top 문자 제거(pop)
            '''
            1. 스택이 비어있지 않을 때
            2. 현재 문자 ch가 스택 맨 위 문자보다 사전순으로 더 앞 
            3. 스택 맨 위 문자가 이후에도 문자열에서 다시 등장 가능하면
            '''
            # 현재 문자가 더 나은 선택 이전 문자를 제거해도 안전 
            while stack and ch < stack[-1] and count[stack[-1]] > 0: 
                removed = stack.pop()
                visited.remove(removed)

            # 현재 문자 스택이랑 visited에 추가
            stack.append(ch)
            visited.add(ch)

        return ("".join(stack))


