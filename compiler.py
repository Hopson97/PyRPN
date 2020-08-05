import opcodes as op
import lex

class Parser:
    def __init__(self):
        self.symbolTable = {}

    def parse(self, functions, lexer, token, code):
        if token.type == lex.TOKEN_NUMBER:
            code.append(op.OPCODE_PUSH)
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
                if not self.parse(functions, lexer, token, body):
                    return False
                if (token.type == lex.TOKEN_END or token.type == lex.TOKEN_ERROR):
                    print("Error: Function end never found.")
                    return False
                token = lexer.nextToken()
            functions[len(functions)] = body
            self.symbolTable[name] = len(functions) - 1    
        elif token.type == lex.TOKEN_IDEN:
            if not token.lexeme in self.symbolTable:
                print("Error: Unrecognised identifer: " + token.lexeme)
                return False
            code.append(op.OPCODE_CALL)
            code.append(self.symbolTable[token.lexeme]) 
        elif token.type in op.TOKEN_TO_BUILTIN:
            code.append(op.TOKEN_TO_BUILTIN[token.type])    
        else:
            print("Unexpected token: " + token.type)
            return False
        return True 

    def compile(self, functions, source, code):
        lexer = lex.Lexer(source)
        token = lexer.nextToken()
        while not token.type == lex.TOKEN_END:
            if not self.parse(functions, lexer, token, code):
                return
            token = lexer.nextToken()