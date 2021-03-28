class Parser:

    def __init__(self, alltoken,n):
        self.alltoken = alltoken
        self.dick = {}
        self.isexp = dict(zip(alltoken, [False] * len(alltoken)))
    def output(self, token):
        if self.isexp(token): print(token[1])
        else: self.check(token)
    def check(self,token): return
    def unpack(self,par, pack):
        p = iter(pack)
        curr = next(p)
        rest ={}
        def inner(prev):
            try: 
                curr = next(p)
                return inner(curr)
            except StopIteration:  return rest
        return inner(curr)

    def op(self,left,right,value):
        result = {}
        if value == '<=':
            result[left] = right
        
        elif value == '->':
            result[left] = right 
        
        return result