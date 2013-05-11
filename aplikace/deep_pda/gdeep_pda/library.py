'''
Obsahuje ruzne funkce a tridy.

@author: Vendula Poncova
'''

import sys
from codecs import open
from .error import EPARAM, EIO, check


DEBUG = False
DEBUG_CODE = "[Library]"

#=================================================================== enum()

def enum(*sequential, **named):
    
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

#=================================================================== unquote()

def isSurrounded(item, left, right):
    
    return len(item) >= 2 and item[0] == left and item[-1] == right

def unquote(item, char = "'"):
    
    if isinstance(item, list) :
        
        for n,i in enumerate(item):
            item[n] = unquote(i)
                
    elif isinstance(item, str) :
        
        if isSurrounded(item, char, char) :
            item = item[1:-1]
            #check(item)
            
    return item

#=================================================================== printHelp()

def printHelp():
    msg = '''
    gdeep_pda: Redukce zobecneneho zasobnikoveho automatu
    Vendula Poncova (xponco00)

    gdeep_pda [-h|--help] [--input=filename] [--output=filename] [--reduce-states]
         [--reduce-symbols] [--analyze-string="string"]


    -h, --help                   Vypise napovedu.
    --input=filename             Nacte vstup ze souboru.
    --output=filename            Vypise vystup do souboru.
    --reduce-states              Zredukuje pocet stavu.
    --reduce-symbols             Zredukuje pocet nevstupnich symbolu.
    --analyze-string="string"    Zjisti, zda string je retezec jazyka prijimaneho
                                 danym automatem, a vypise sekvenci kroku.
    \n'''
    sys.stdout.write(msg)

#=================================================================== processParams()

def processParams(argv):
    from .parser import GDPParser

    check("Zpracovani parametru.", DEBUG_CODE, DEBUG, level = 0)   

    arg_options = {"--input": "input", "--output": "output", "--analyze-string": "analyze_string"}

    flag_options = { "--help": "help", "-h": "help",
                     "--reduce-states": "reduce_states", 
                     "--reduce-symbols": "reduce_symbols",  
                   }
    args = {} 

    # zpracovani parametru
    for arg in argv:
        opt, sep, value = arg.partition("=")

        if arg in flag_options and flag_options[arg] not in args:
            args[flag_options[arg]] = True

        elif opt in arg_options and arg_options[opt] not in args:
            args[arg_options[opt]] = value

        else: raise EPARAM

    if ("help" in args) and len(args) != 1:
        raise EPARAM
        
    if "input" not in args :
        args["input"] = None

    if "output" not in args :
        args["output"] = None
        
    if "analyze_string" in args :
        string = GDPParser().parseString(args["analyze_string"])
        
        if string == None :
            raise EPARAM
        else:
            args["analyze_string"] = string
            check(string, DEBUG_CODE, DEBUG, level = 3)


    check(args, DEBUG_CODE, DEBUG, level = 2)
    return args

#=================================================================== readInput()

def readInput (filename):
    check("Nacteni vstupu.", DEBUG_CODE, DEBUG, level = 0)
    try:
        
        # cteni ze souboru
        if filename != None :
            
            file = open(filename, mode='r', encoding='utf8')
            input = file.read()
            file.close()
            
        # cteni ze stdin
        else:
            input = sys.stdin.read()

    except IOError:
        raise EIO("Chyba pri cteni souboru.")

    check(input, DEBUG_CODE, DEBUG, level = 2)
    return input

#=================================================================== readOutput()

def writeOutput(filename, output):
    check("Zapis vystupu.", DEBUG_CODE, DEBUG, level = 0)
    try:
        
        # zapis do souboru
        if filename != None :
            file = open(filename, mode='w', encoding='utf8')
            file.write(output)
            file.close()
        
            check(output, DEBUG_CODE, DEBUG, level = 2)
            
        # zapis na stdout
        else:
            file = sys.stdout.write(output)

    except IOError:
        raise EIO("Chyba pri zapisu do souboru.")


##################################################################### konec souboru