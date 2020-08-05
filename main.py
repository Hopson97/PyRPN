from evaluate import KEYWORDS

expression = "15.5 1.5 + 2 swap + 2 5 * - print "
stack = []
ptr = 0

'''
    Parsing Functions
'''
def advance():
    global ptr
    ptr += 1

def current():
    return expression[ptr]

def atEnd():
    return ptr == len(expression)

def parseDigit():
    n = ""
    while not atEnd() and current().isdigit():
        n += current()
        advance()
    if current() == ".":
        n += "."
        advance() 
        while not atEnd() and current().isdigit():
            n += current()
            advance()
    return float(n)

def parseWord():
    word = ""
    while not atEnd() and (current().isalpha() or current() in "+-/*"):
        word += current()
        advance()
    return word

'''
    The main programme
'''
if __name__ == "__main__":
    while not atEnd():
        c = current()
        if c.isdigit():
            stack.append(parseDigit())
        elif c.isalpha() or c in "+-/*":
            word = parseWord()
            if word in KEYWORDS:
                KEYWORDS[word](stack)
            else:
                print("Unknown word '" + word + "'. Exiting.")
                exit()
        advance()