from reader import Reader
from lexer2 import Lexer
from parser import Parser
import pandas as pd

def run(file_name):
    with open(file_name,'r') as file:
        script = file.read()

    print(script)

    alltoken = Lexer(Reader(script,2)) 
    print(alltoken)
    print("\nALLTOKEN: ")
    print(pd.DataFrame(alltoken,columns =  ['type', 'value']))
    tree = Parser(alltoken,2)
    
    return 


run('hw.spy')