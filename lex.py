from evaluate import KEYWORDS

TOKEN_NUMBER = 0
TOKEN_IDEN = 1
TOKEN_COLON = 2
TOKEN_KEYWORD = 3
TOKEN_COLON = 4
TOKEN_SEMICOLON = 5
TOKEN_ERROR = 6
TOKEN_END = 7

class Token:
    def __init__(self, token, lexeme):
        self.type = token
        self.lexeme = lexeme

class Lexer:
    def __init__(self, source):
        self.current = 0
        self.source = source
    
    def nextToken(self):
        if self._atEnd():
            return Token(TOKEN_END, "")

        c = self._curr()

        skipped = False
        while c == ' ':
            self.current += 1
            c = self._curr()
        self.current += 1

        skipped = False
        while c == ' ':
            self.current += 1
            c = self._curr()
            skipped = True
        if (skipped):
            print("skipyp")

        # Find tokens 
        if c.isdigit():
            return self._tokenNumber()
        elif c.isalpha() or c in "+-/*":
            word = self._lexword()
            if word in KEYWORDS:
                return Token(TOKEN_KEYWORD, word)
            else:
                return Token(TOKEN_IDEN, word)
        elif c == ":":
            return Token(TOKEN_COLON, c)
        elif c == ';':
            return Token(TOKEN_SEMICOLON, c)
        else:
            return Token(TOKEN_ERROR, c)

    def _tokenNumber(self):
        n = self._prev()
        while not self._atEnd() and self._curr().isdigit():
            n += self._curr()
            self.current += 1
        if self._curr() == ".":
            n += "."
            self.current += 1
            while not self._atEnd() and self._curr().isdigit():
                n += self._curr()
                self.current += 1
        return Token(TOKEN_NUMBER, n)

    def _lexword(self):
        word = self._prev()
        while not self._atEnd() and (self._curr().isalpha() or self._curr() in "+-/*"):
            word += self._curr()
            self.current += 1
        return word

    def _curr(self):
        return self.source[self.current]

    def _prev(self):
        return self.source[self.current - 1]

    def _atEnd(self):
        return self.current == len(self.source)
