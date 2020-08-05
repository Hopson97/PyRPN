from evaluate import KEYWORDS

stack = []

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

callstack = []
def callstackTop():
    global callstack
    return callstack[len(callstack) - 1]


'''
    User defined functions
'''
functions = {}
'''
    Parsing Functions
'''

def parseDigit():
    n = ""
    while not callstackTop().atEnd() and callstackTop().current().isdigit():
        n += callstackTop().current()
        callstackTop().advance()
    if callstackTop().current() == ".":
        n += "."
        callstackTop().advance() 
        while not callstackTop().atEnd() and callstackTop().current().isdigit():
            n += callstackTop().current()
            callstackTop().advance()
    return float(n)

def parseWord():
    word = ""
    while not callstackTop().atEnd() and (callstackTop().current().isalpha() or callstackTop().current() in "+-/*"):
        word += callstackTop().current()
        callstackTop().advance()
    return word

def compileFunction():
    callstackTop().advance()
    name = parseWord()
    body = ""
    while(True):
        if not callstackTop().atEnd():
            body += callstackTop().current()
            if callstackTop().current() != ";":
                callstackTop().advance()
            else:
                break
    functions[name] = body

def evaluate():
    while not callstackTop().atEnd():
        c = callstackTop().current()
        if c.isdigit():
            stack.append(parseDigit())
        elif c.isalpha() or c in "+-/*":
            word = parseWord()
            if word in KEYWORDS:
                KEYWORDS[word](stack)
            elif word in functions:
                callstack.append(StackFrame(functions[word]))
                evaluate()
                callstack.pop()
            else:
                print("Unknown word '" + word + "'. Exiting.")
                exit()
        elif c == ':':
            compileFunction()
        callstackTop().advance()

'''
    The main programme
'''
#
if __name__ == "__main__":
    expression = ":ADDTHREE 3 +; :ADDFIVE ADDTHREE 2 +; 2 ADDFIVE print "
    callstack.append(StackFrame(expression))
    evaluate()