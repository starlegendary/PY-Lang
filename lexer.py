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
    allop = dict(map(lambda x: (x[0],x[1:]),['->','<-']))
    while(stop != None):

        #comment
        if r.p[1] == '#': 
            r.movetil(1,eq('#'))
        #remove space and nextline
        elif has(' \n')(r.p[1]):
            stop = r.movetil(1,has(' \n', False))
            continue
        #check default symbol
        elif has('_{}:;')(r.p[1]):
            alltoken.append((r.p[1],''))
        elif r.p[1] == '-':
            r.move(1,eq(True))
            if(r.p[1] != '>'):
                raise Exception ('Cannot recognize -')
            stop = r.move(1,eq(True))
            alltoken.append((r.clear(),''))
            continue
        
        #check default seperator
        #elif has(',;')(r.p[1]):
        #    alltoken.append(('sep',r.p[1]))
        #check default operation
        #elif has(':=')(r.p[1]):
        #    alltoken.append(('op',r.p[1]))
        #check default double operation ->

        #elif r.p[1] in allop:
        #    for correct in allop[r.p[1]]:
        #        curr = r.move(1,eq(True))
        #        if(not (curr == correct)):
        #            raise Exception ('Cannot recognize', r.clear())
        #    stop = r.move(1, eq(True))
        #    alltoken.append(('op', r.clear()))
        #    continue
        #check for functions
        
        
        elif match("[_a-zA-Z]")(r.p[1]):
            stop = r.movetil(1, match("[_a-zA-Z]", False), eq(True))
            alltoken.append(('fun', r.clear()))
            continue
        #check for objects
        elif has(("'", '"'))(r.p[1]):
            r.move(1, eq(False))
            r.movetil(1, has(("'", '"'), True), eq(True))
            alltoken.append(('obj', r.clear()))
            
        else:
            raise Exception ('Cannot recognize', r.p[1])
        stop = r.move(1)

    return alltoken