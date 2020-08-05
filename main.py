expression = "15.5 1.5 + 2 swap p"
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
    word = ""
    while hasNext() and current().isalpha():
        word += current()
        advance()
    return word

if __name__ == "__main__":
    while ptr != len(expression):
        c = current()
        if c.isdigit():
            stack.append(parseDigit())
        elif c.isalpha():
            word = parseWord()
            if word == "dup":
                top = stack.pop()
                stack.append(top)
                stack.append(top)
            elif word == "swap":
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
            elif word == "rot":
                a = stack.pop()
                b = stack.pop()
                c = stack.pop()
                stack.append(c)
                stack.append(a)
                stack.append(b)
            elif word == "drop":
                stack.pop()
            elif word == "sum":
                summed = 0
                while len(stack) != 0:
                    summed += stack.pop()
                stack.pop(summed)
            elif word == "avg":
                summed = 0
                total = len(stack)
                while len(stack) != 0:
                    summed += stack.pop()
                stack.pop(summed / total)
            elif word == "print":
                print(stack.pop())
            else:
                print("Unknown word '" + word + "'. Exiting.")
                exit()
            advance()
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
        advance()
    print(stack)