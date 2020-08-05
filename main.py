import evaluate
import lex

'''
    Opcodes...
'''
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

TOKEN_TO_BUILTIN = {
    lex.TOKEN_KEYWORD_DUP: OPCODE_DUP,
    lex.TOKEN_KEYWORD_SWAP: OPCODE_SWAP,
    lex.TOKEN_KEYWORD_ROT: OPCODE_ROT,
    lex.TOKEN_KEYWORD_DUP: OPCODE_DUP,
    lex.TOKEN_KEYWORD_DROP: OPCODE_DROP,
    lex.TOKEN_KEYWORD_AVG: OPCODE_AVG,
    lex.TOKEN_KEYWORD_PRINT: OPCODE_PRINT,
    lex.TOKEN_KEYWORD_ADD: OPCODE_ADD,
    lex.TOKEN_KEYWORD_SUB: OPCODE_SUBTRACT,
    lex.TOKEN_KEYWORD_MULTIPLY: OPCODE_MULTIPLY,
    lex.TOKEN_KEYWORD_DIVIDE: OPCODE_DIVIDE,
}

'''
    Map keywords to the evaluating functions
'''
BUILTIN = {
    OPCODE_DUP: evaluate.dup,
    OPCODE_SWAP: evaluate.swap,
    OPCODE_ROT: evaluate.rot,
    OPCODE_DROP: evaluate.drop,
    OPCODE_AVG: evaluate.avg,
    OPCODE_PRINT: evaluate.printtop,
    OPCODE_ADD: evaluate.add,
    OPCODE_SUBTRACT: evaluate.subtract,
    OPCODE_MULTIPLY: evaluate.multiply,
    OPCODE_DIVIDE: evaluate.divide
}


class StackFrame:
    def __init__(self, code):
        self.ip = 0
        self.code = code

class Machine:
    def __init__(self):
        self.stack = []
        self.functions = {}
        self.symbolTable = {}
        self.code = []

        self.callstack = []

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
            self.functions[len(self.functions)] = body
            self.symbolTable[name] = len(self.functions) - 1

        elif token.type == lex.TOKEN_IDEN:
            if not token.lexeme in self.symbolTable:
                print("Error: Unrecognised identifer: " + token.lexeme)
                return False
            code.append(OPCODE_CALL)
            code.append(self.symbolTable[token.lexeme])

        elif token.type in TOKEN_TO_BUILTIN:
            code.append(TOKEN_TO_BUILTIN[token.type])
            
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

    def _run(self, code):
        self.callstack.append(StackFrame(code))
        frame = self.callstack[len(self.callstack) - 1]
        while frame.ip < len(frame.code):
            instruction = frame.code[frame.ip]
            if instruction == OPCODE_PUSH: 
                self.stack.append(frame.code[frame.ip + 1])
                frame.ip += 2
            elif instruction == OPCODE_CALL:
                functionid = frame.code[frame.ip + 1]
                function = self.functions[functionid]
                self._run(function)
                self.callstack.pop()
                frame.ip += 2
            else:
                BUILTIN[instruction](self.stack)
                frame.ip += 1

    def run(self):
        self._run(self.code)


'''
    The main programme
'''
if __name__ == "__main__":
    expression = "3 3 :ADDTHREE 3 + ; :ADDFIVE ADDTHREE 2 + ; 2 ADDFIVE print "
    #expression = ": ADDTHREE 3 + ; 3 ADDTHREE print"
    #expression = "3 3 + print"
    machine = Machine()
    machine.compile(expression)
    machine.run()