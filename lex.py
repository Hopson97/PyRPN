TOKEN_NUMBER = 0
TOKEN_IDEN = 1
TOKEN_COLON = 2
TOKEN_KEYWORD_DUP = 3
TOKEN_KEYWORD_SWAP = 4
TOKEN_KEYWORD_ROT = 5
TOKEN_KEYWORD_DROP = 6
TOKEN_KEYWORD_AVG = 7
TOKEN_KEYWORD_PRINT = 8
TOKEN_KEYWORD_ADD = 9
TOKEN_KEYWORD_SUB = 10
TOKEN_KEYWORD_MULTIPLY = 11
TOKEN_KEYWORD_DIVIDE = 12
TOKEN_COLON = 13
TOKEN_SEMICOLON = 14
TOKEN_ERROR = 15
TOKEN_END = 16

KEYWORD_MAP = {
    "dup": TOKEN_KEYWORD_DUP,
    "swap": TOKEN_KEYWORD_SWAP,
    "rot": TOKEN_KEYWORD_ROT,
    "drop": TOKEN_KEYWORD_DUP,
    "avg": TOKEN_KEYWORD_AVG,
    "print": TOKEN_KEYWORD_PRINT,
    "+": TOKEN_KEYWORD_ADD,
    "-": TOKEN_KEYWORD_SUB,
    "*": TOKEN_KEYWORD_MULTIPLY,
    "/": TOKEN_KEYWORD_DIVIDE,
}

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

        # Skip whitespace
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
            if word in KEYWORD_MAP:
                return Token(KEYWORD_MAP[word], word)
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
