import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,  # use operator.div for Python 2
            '%' : operator.mod,
            '^' : operator.xor,
        }
        for token in tokens:
            if token in ops:
                val2 = stack.pop()
                val1=stack.pop()
                stack.append(int(ops[token](val1, val2)))
            else:
                stack.append(int(token))
                
        return stack[-1]