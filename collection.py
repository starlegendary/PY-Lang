class OBJ:
    def __init__(self, value):
        self.val = value
        self.s = len(value)
    def comb(self, obj): return OBJ(self.val + obj.val)
    def conv(self,var):
        toval = dict(zip(var,[None]*len(var)))
        i_inp = 0
        for i_var in range(len(var)):
            if var[i_var] == '_':
                if i_var == var.index('_'):  
                  i_inp = self.s - len(var[i_var+1:])
            else:
                toval[var[i_var]] =  self.val[i_inp] 
                if (len(var) < self.s and i_var == len(var)-1):
                    toval[var[i_var]] += self.val[i_inp+1:]
                i_inp += 1
            i_inp = i_inp% self.s
        return dict(map(lambda x: (x[0],OBJ(x[1])),list(filter(lambda x: x[0] != '_',toval.items()))))
    def __str__(self): return self.val