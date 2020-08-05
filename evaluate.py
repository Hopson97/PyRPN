'''
    Functions that evaluate
'''
def dup(stack):
    top = stack.pop()
    stack.append(top)
    stack.append(top)

def swap(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a)
    stack.append(b)

def rot(stack):
    a = stack.pop()
    b = stack.pop()
    c = stack.pop()
    stack.append(c)
    stack.append(a)
    stack.append(b)

def drop(stack):
    stack.pop()

def sum(stack):
    summed = 0
    while len(stack) != 0:
        summed += stack.pop()
    stack.append(summed)

def avg(stack):
    summed = 0
    total = len(stack)
    while len(stack) != 0:
        summed += stack.pop()
    stack.append(summed / total)

def printtop(stack):
    print(stack.pop())

def add(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a + b)

def subtract(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a - b)

def multiply(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a * b)

def divide(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a / b)