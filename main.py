from evaluate import KEYWORDS
import lex

class Machine:
    def __init__(self, source):
        self.stack = []
        self.functions = {}
        self.lexer = lex.Lexer(source)

    def run(self):
        token = self.lexer.nextToken()
        while not token.type == lex.TOKEN_END:
            if token.type == lex.TOKEN_NUMBER:
                self.stack.append(float(token.lexeme))

            elif token.type == lex.TOKEN_COLON:
                token = self.lexer.nextToken()
                if token.type != lex.TOKEN_IDEN:
                    print("Error: Expected TOKEN_IDEN but got " + token.lexeme)
                    return
                name = token.lexeme
                body = []
                while token.type != lex.TOKEN_SEMICOLON:
                    if (token.type == lex.TOKEN_END or token.type == lex.TOKEN_ERROR):
                        print("Error: Function end never found.")
                        return
                    token = self.lexer.nextToken()
                    body.append(token)
                self.functions[name] = body
                    
            elif token.type == lex.TOKEN_IDEN:
                if not token.lexeme in self.functions:
                    print("Error: Unrecognised identifer: " + token.lexeme)
                    return
                body = self.functions[token.lexeme]
                
            elif token.type == lex.TOKEN_KEYWORD:
                KEYWORDS[token.lexeme](self.stack)
            token = self.lexer.nextToken()
'''
    The main programme
'''
if __name__ == "__main__":
    expression = "3 3 :ADDTHREE 3 + ; :ADDFIVE ADDTHREE 2 + ; 2 ADDFIVE print "
    expression = ":ADDTHREE 3 + ; 3 3 + print"
    machine = Machine(expression)
    machine.run()