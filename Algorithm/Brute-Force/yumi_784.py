class Solution(object):
    def letterCasePermutation(self, s):

        chars = list(s)

        # 알파벳이 등장하는 위치
        alpha_pos = [i for i, c in enumerate(chars) if c.isalpha()]
        n = len(alpha_pos)

        output_set = []

        # 총 2^n 가지 대소문자 조합
        for mask in range(1 << n):
            temp = chars[:]
            
            for j in range(n):
                idx = alpha_pos[j]
                if (mask >> j) & 1:
                    temp[idx] = temp[idx].upper()
                else:
                    temp[idx] = temp[idx].lower()
            output_set.append("".join(temp))

        return output_set
            
