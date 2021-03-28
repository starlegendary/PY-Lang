class Reader:
    def __init__(self, script,n):
        self.s = [iter(script) for i in range(n)]
        self.p = [next(self.s[i]) for i in range(n)]
        self.l = 0
        self.token = ''


    def __str__(self):
      
      return " Stored [|" + str(self.token)+'|]\n' + str(list(map(lambda x : 'p'+str(x[0])+' -> '+ str(x[1]), list(enumerate(self.p)))))
    
    def move(self, index, isadd = lambda x: False):
        prev = self.p[index]
        if(isadd(prev)): self.token += prev
        if(prev == '\n'): self.l += 1
        try:
            value = next(self.s[index])
            self.p[index] = value
        except StopIteration:
            value = None
        #print(self)
        return value

    def movetil(self, index,cond, isadd = lambda x: False):
        v = self.move(index,isadd)
        if v == None: return 
        while not cond(v):
              v = self.move(index,isadd)
              if v == None: return 
        return v
    def join(self, a, b, isadd = lambda x: True):
        return self.movetil(a, lambda x: x== self.p[b], isadd)
    
    def clear(self): 
        v = self.token
        self.token = ''
        return v
''''
    def movetil(self, index,cond, isadd = lambda x: False):
        v = self.move(index,isadd)
        while not cond(v):
              v = self.move(index,isadd)
        return v
'''