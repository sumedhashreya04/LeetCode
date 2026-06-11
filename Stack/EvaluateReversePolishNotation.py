class Solution(object):
    def evalRPN(self, tokens):
        struct=[]
        operations={
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: int(float(x) / y)
        }
        for i in range(len(tokens)):
            if tokens[i] in operations:
                a=struct.pop()
                b=struct.pop()
                c=operations[tokens[i]](b,a)
                struct.append(c)
            else:
                struct.append(int(tokens[i]))
        return struct[-1]
