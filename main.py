from evaluate import KEYWORDS

class StackFrame:
    def __init__(self, expr):
        self.expression = expr
        self.ptr = 0

    def advance(self):
        self.ptr += 1

    def current(self):
        return self.expression[self.ptr]

    def atEnd(self):
        return self.ptr == len(self.expression)

class Machine:
    def __init__(self):
        self.callstack = []
        self.stack = []
        self.frame = None
        self.functions = {}

    def addStackFrame(self, stackframe):
        self.callstack.append(stackframe)
        self.frame = self.callstack[len(self.callstack) - 1]

    def popStackFrame(self):
        self.callstack.pop()
        self.frame = self.callstack[len(self.callstack) - 1]

    def evaluate(self):
        while not self.frame.atEnd():
            c = self.frame.current()
            if c.isdigit():
                self.stack.append(self.parseDigit())
            elif c.isalpha() or c in "+-/*":
                word = self.parseWord()
                if word in KEYWORDS:
                    KEYWORDS[word](self.stack)
                elif word in self.functions:
                    self.addStackFrame(StackFrame(self.functions[word]))
                    self.evaluate()
                    self.popStackFrame();
                else:
                    print("Unknown word '" + word + "'. Exiting.")
                    exit()
            elif c == ':':
                self.compileFunction()
            self.frame.advance()


    def parseDigit(self):
        n = ""
        while not self.frame.atEnd() and self.frame.current().isdigit():
            n += self.frame.current()
            self.frame.advance()
        if self.frame.current() == ".":
            n += "."
            self.frame.advance() 
            while not self.frame.atEnd() and self.frame.current().isdigit():
                n += self.frame.current()
                self.frame.advance()
        return float(n)

    def parseWord(self):
        word = ""
        while not self.frame.atEnd() and (self.frame.current().isalpha() or self.frame.current() in "+-/*"):
            word += self.frame.current()
            self.frame.advance()
        return word

    def compileFunction(self):
        self.frame.advance()
        name = self.parseWord()
        body = ""
        while(True):
            if not self.frame.atEnd():
                body += self.frame.current()
                if self.frame.current() != ";":
                    self.frame.advance()
                else:
                    break
        self.functions[name] = body
'''
    The main programme
'''
if __name__ == "__main__":
    expression = ":ADDTHREE 3 + ; :ADDFIVE ADDTHREE 2 + ; 2 ADDFIVE print "
    machine = Machine()
    machine.addStackFrame(StackFrame(expression))
    machine.evaluate()