class Solution(object):
    def letterCasePermutation(self, s):
        result = ['']  # 초기에는 빈 문자열만 존재

        for char in s:
            temp = []  # 이번 문자에 대한 새로운 조합 저장
            for prefix in result:
                if char.isalpha():
                    # 문자인 경우: 소문자, 대문자 둘 다 붙이기
                    temp.append(prefix + char.lower())
                    temp.append(prefix + char.upper())
                else:
                    # 숫자인 경우: 그대로 붙이기
                    temp.append(prefix + char)
            result = temp  # 업데이트된 결과로 바꾸기

        return result