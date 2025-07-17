class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        length = len(s)
        result = []
        def recursive(s, idx):
            if idx == length:
                result.append(s)
                return 
            if s[idx].isdecimal():
                return recursive(s, idx+1)
            else:
                string1 = str(s)
                string2 = str(s)
                string1 = string1[:idx] + string1[idx].upper() + string1[idx+1:]
                string2 = string2[:idx] + string2[idx].lower() + string2[idx+1:]
                recursive(string2, idx+1)
                recursive(string1, idx+1)
        recursive(s,0)
        return result
