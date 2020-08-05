expression = "15.5 1.5 + 2 swap + 2 5 * - print "
stack = []
ptr = 0

'''
    Functions that evaluate
'''
def dup():
    top = stack.pop()
    stack.append(top)
    stack.append(top)

def swap():
    a = stack.pop()
    b = stack.pop()
    stack.append(a)
    stack.append(b)

def rot():
    a = stack.pop()
    b = stack.pop()
    c = stack.pop()
    stack.append(c)
    stack.append(a)
    stack.append(b)

def drop():
    stack.pop()

def sum():
    summed = 0
    while len(stack) != 0:
        summed += stack.pop()
    stack.append(summed)

def avg():
    summed = 0
    total = len(stack)
    while len(stack) != 0:
        summed += stack.pop()
    stack.append(summed / total)

def printtop():
    print(stack.pop())

def add():
    a = stack.pop()
    b = stack.pop()
    stack.append(a + b)

def subtract():
    a = stack.pop()
    b = stack.pop()
    stack.append(a - b)

def multiply():
    a = stack.pop()
    b = stack.pop()
    stack.append(a * b)

def divide():
    a = stack.pop()
    b = stack.pop()
    stack.append(a / b)

'''
    Map keywords to the evaluating functions
'''
KEYWORDS = {
    "dup": dup,
    "swap": swap,
    "rot": rot,
    "drop": drop,
    "avg": avg,
    "print": printtop,
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

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
                KEYWORDS[word]()
            else:
                print("Unknown word '" + word + "'. Exiting.")
                exit()
        advance()