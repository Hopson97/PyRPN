import lex
import opcodes as op
from compiler import Parser

class StackFrame:
    def __init__(self, code):
        self.ip = 0
        self.code = code

class Machine:
    def __init__(self):
        self.stack = []
        self.functions = {}
        self.symbolTable = {}
        self.code = []

        self.callstack = []

    def _run(self, code):
        self.callstack.append(StackFrame(code))
        frame = self.callstack[len(self.callstack) - 1]
        while frame.ip < len(frame.code):
            instruction = frame.code[frame.ip]
            if instruction == op.OPCODE_PUSH: 
                self.stack.append(frame.code[frame.ip + 1])
                frame.ip += 2
            elif instruction == op.OPCODE_CALL:
                functionid = frame.code[frame.ip + 1]
                function = self.functions[functionid]
                self._run(function)
                self.callstack.pop()
                frame.ip += 2
            else:
                op.BUILTIN[instruction](self.stack)
                frame.ip += 1

    def run(self, source):
        parser = Parser()
        parser.compile(self, source, self.code)
        self._run(self.code)

'''
    The main programme
'''
if __name__ == "__main__":
    source = "3 3 :ADDTHREE 3 + ; :ADDFIVE ADDTHREE 2 + ; 2 ADDFIVE print "
    #expression = ": ADDTHREE 3 + ; 3 ADDTHREE print"
    #expression = "3 3 + print"
    machine = Machine()
    machine.run(source)