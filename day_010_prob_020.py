class Solution:
    def isValid(self, s: str) -> bool:
        # pretty inefficient solution use dictionary for better time complexity
        op = ['(','{','[']
        cl = [')','}',']']
        stack = []

        for b in s:
            if b in cl:
                if stack:
                    if cl.index(b) == op.index(stack.pop()):
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(b)
        if stack:
            return False
        return True