expression = "15.5 1 + p"
stack = []
ptr = 0

def advance():
    global ptr
    ptr += 1

def current():
    return expression[ptr]

def hasNext():
    return ptr < len(expression) - 1

def parseDigit():
    n = ""
    while hasNext() and current().isdigit():
        n += current()
        advance()
    if hasNext() and current() == ".":
        n += "."
        advance() 
        while current().isdigit():
            n += current()
            advance()
    return float(n)

def parseWord():

    pass

if __name__ == "__main__":
    while ptr != len(expression):
        c = current()
        if c.isdigit():
            stack.append(parseDigit())
        elif c.isalpha():
            word = parseWord()
        elif c in "+-/*":
            a = stack.pop()
            b = stack.pop()
            if c == '+':
                stack.append(a + b)           
            if c == '-':
                stack.append(a - b)            
            if c == '/':
                stack.append(a / b)            
            if c == '*':
                stack.append(a * b)
        elif c == 'p':
            print(stack.pop())
        advance()