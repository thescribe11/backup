import sys
from termcolor import colored, cprint

ERROR_PRINT = lambda text: cprint(text, 'red')

# Token categories
EOF = 0 #End of File
PRINT = 1 #"print" keyword
UNSIGNEDINT = 2 #unsigned integer
NAME = 3 #Identifier
ASSIGNOP = 4 # "="
LEFTPAREN = 5
RIGHTPAREN = 6
PLUS = 7
MINUS = 8
TIMES = 9
DIVIDE = 10
NEWLINE = 11
ERROR = 12

source: str

line = 0
column = 0
blankline = True

TOKENS = []


class Token:
    def __init__(self, line, column, category, lexeme):
        self.line = line
        self.column = column
        self.category = category
        self.lexeme = lexeme

def getchar(index) -> (str, int):
    try:
        char = source[index]
    except IndexError:
        return (EOF, index)
    index += 1
    if char == ' ':
        char = getchar(index)
    

def gettoken(index) -> Token:
    pass

def tokenizer():
    for sourceindex in source:
        current_token = gettoken(sourceindex)

def main():
    if len(sys.argv) >= 2:
        try:
            infile = open(sys.argv[1], 'r')
            source = infile.read()
            infile.close()
        except FileNotFoundError:
            ERROR_PRINT("\n[!] ERROR: That file does not exist.\n")
            return
    else:
        ERROR_PRINT("\n[!] ERROR: No input file supplied.\n")
        return

    print(source)

    if source[-1] != '\n':
        source[-1] = '\n'
    
    tokenizer(source)

    

if __name__ == "__main__":
    main()