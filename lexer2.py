import re

def eq(cond, sth1 = True):
    if type(cond) == bool: return lambda x: cond 
    return lambda x: (x == cond) == sth1

def has(cond, sth = True): 
    return lambda x: (x in cond) == sth

def match(cond, sth = True): 
    return lambda x: bool(re.match(cond,x)) == sth

def Lexer(r):
    alltoken = []
    stop = True
    while(stop != None):

        #comment
        if r.p[1] == '#': 
            r.movetil(1,eq('#'))
        #remove space and nextline
        elif r.p[1] in ' \n':
            stop = r.movetil(1,has(' \n', False))
            continue
        #check default symbol
        elif r.p[1] in '_{}:;,':
            t = r.p[1]
            alltoken.append((t,t))
        elif r.p[1] == '-':
            r.move(1,eq(True))
            if(r.p[1] != '>'):
                raise Exception ('Cannot recognize -')
            stop = r.move(1,eq(True))
            t = r.clear()
            alltoken.append((t,t))
            continue
        
        elif match("[_a-zA-Z]")(r.p[1]):
            stop = r.movetil(1, match("[_a-zA-Z]", False), eq(True))
            alltoken.append(('fun', r.clear()))
            continue
        #check for objects
        elif has(("'", '"'))(r.p[1]):
            r.move(1, eq(False))
            r.movetil(1, has(("'", '"')), eq(True))
            alltoken.append(('obj', r.clear()))
        else:
            raise Exception ('Cannot recognize', r.p[1])
        stop = r.move(1)

    return alltoken