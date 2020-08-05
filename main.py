import evaluate
import lex

'''
    Map keywords to the evaluating functions
'''
KEYWORDS = {
    "dup": evaluate.dup,
    "swap": evaluate.swap,
    "rot": evaluate.rot,
    "drop": evaluate.drop,
    "avg": evaluate.avg,
    "print": evaluate.printtop,
    "+": evaluate.add,
    "-": evaluate.subtract,
    "*": evaluate.multiply,
    "/": evaluate.divide
}

OPCODE_PUSH = 0
OPCODE_CALL = 1
OPCODE_DUP = 2
OPCODE_SWAP = 3
OPCODE_ROT = 4
OPCODE_DROP = 5
OPCODE_AVG = 6
OPCODE_PRINT = 7
OPCODE_ADD = 8
OPCODE_SUBTRACT = 9
OPCODE_MULTIPLY = 10
OPCODE_DIVIDE = 11

class Machine:
    def __init__(self):
        self.stack = []
        self.functions = {}
        self.symbolTable = {}
        self.code = []

    def parse(self, lexer, token, code):
        if token.type == lex.TOKEN_NUMBER:
            code.append(OPCODE_PUSH)
            code.append(float(token.lexeme))

        elif token.type == lex.TOKEN_COLON:
            token = lexer.nextToken()
            if token.type != lex.TOKEN_IDEN:
                print("Error: Expected TOKEN_IDEN but got " + token.lexeme)
                return False
            name = token.lexeme
            body = []
            token = lexer.nextToken()
            while token.type != lex.TOKEN_SEMICOLON:
                if not self.parse(lexer, token, body):
                    return False
                if (token.type == lex.TOKEN_END or token.type == lex.TOKEN_ERROR):
                    print("Error: Function end never found.")
                    return False
                token = lexer.nextToken()
                body.append(token)
            self.functions[len(self.functions)] = body
            self.symbolTable[name] = len(self.functions) - 1
            print("Added", name)

        elif token.type == lex.TOKEN_IDEN:
            if not token.lexeme in self.symbolTable:
                print("Error: Unrecognised identifer: " + token.lexeme)
                return False
            code.append(OPCODE_CALL)
            code.append(self.symbolTable[token.lexeme])

        # smh direct mappings for keywords and tokens
        elif token.type == lex.TOKEN_KEYWORD_DUP:
            code.append(OPCODE_DUP)
        elif token.type == lex.TOKEN_KEYWORD_SWAP:
            code.append(OPCODE_SWAP)
        elif token.type == lex.TOKEN_KEYWORD_ROT:
            code.append(OPCODE_ROT)
        elif token.type == lex.TOKEN_KEYWORD_DROP:
            code.append(OPCODE_DROP)
        elif token.type == lex.TOKEN_KEYWORD_AVG:
            code.append(OPCODE_AVG)
        elif token.type == lex.TOKEN_KEYWORD_PRINT:
            code.append(OPCODE_PRINT)
        elif token.type == lex.TOKEN_KEYWORD_ADD:
            code.append(OPCODE_ADD)
        elif token.type == lex.TOKEN_KEYWORD_SUB:
            code.append(OPCODE_SUBTRACT)
        elif token.type == lex.TOKEN_KEYWORD_MULTIPLY:
            code.append(OPCODE_MULTIPLY)
        elif token.type == lex.TOKEN_KEYWORD_DIVIDE:
            code.append(OPCODE_DIVIDE)
        else:
            print("Unexpected token: " + token.type)
            return False
        return True

    def compile(self, source):
        lexer = lex.Lexer(source)
        token = lexer.nextToken()
        while not token.type == lex.TOKEN_END:
            if not self.parse(lexer, token, self.code):
                return
            token = lexer.nextToken()

    def run(self):
        print(self.code)
        pass

'''
    The main programme
'''
if __name__ == "__main__":
   # expression = "3 3 :ADDTHREE 3 + ; :ADDFIVE ADDTHREE 2 + ; 2 ADDFIVE print "
    expression = ": ADDTHREE 3 + ; 3 ADDTHREE print"
    machine = Machine()
    machine.compile(expression)
    machine.run()