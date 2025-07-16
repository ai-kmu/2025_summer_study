class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:        
        result = []        
        current_searching_path = []
                
        def backtrack(index):      
            # 문자열의 끝에 도달한 경우   
            if index == len(s):
                # 지금까지 탐색한 문자열 합쳐서 result에 append
                result.append("".join(current_searching_path))
                return
            
            char = s[index]            
            if char.isalpha():  # 문자인 경우
                current_searching_path.append(char.lower())
                # 다음 문자 탐색             
                backtrack(index + 1)
                # 백트래킹 - 경로에서 방금 추가한 소문자를 제거
                current_searching_path.pop()
                                
                current_searching_path.append(char.upper())
                # 다음 문자 탐색               
                backtrack(index + 1)
                # 백트래킹 - 경로에서 방금 추가한 대문자를 제거
                current_searching_path.pop()

            else:  # 숫자인 경우
                current_searching_path.append(char)    
                # 다음 문자 탐색            
                backtrack(index + 1)
                # 백트래킹 - 경로에서 방금 추가한 숫자를 제거
                current_searching_path.pop()
        
        backtrack(0)
        return result