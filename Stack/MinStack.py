#used alot of hints and answers
class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val):
        if len(self.stack)==0:
            self.minstack.append(val)
        elif self.minstack[-1]<val:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
        self.stack.append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.minstack[-1]
        """
        :rtype: int
        """
