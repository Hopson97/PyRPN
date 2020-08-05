import lex
import evaluate

'''
    Opcodes...
'''
OPCODE_PUSH = 0
OPCODE_CALL = 1
OPCODE_DUP = 2
OPCODE_SWAP = 3
OPCODE_ROT = 4
OPCODE_DROP = 5
OPCODE_AVG = 6
OPCODE_PRINT = 7
OPCODE_ADD = 8
OPCODE_SUBTRACT = 9
OPCODE_MULTIPLY = 10
OPCODE_DIVIDE = 11

'''
    Maps token names to opcode names
'''
TOKEN_TO_BUILTIN = {
    lex.TOKEN_KEYWORD_DUP: OPCODE_DUP,
    lex.TOKEN_KEYWORD_SWAP: OPCODE_SWAP,
    lex.TOKEN_KEYWORD_ROT: OPCODE_ROT,
    lex.TOKEN_KEYWORD_DUP: OPCODE_DUP,
    lex.TOKEN_KEYWORD_DROP: OPCODE_DROP,
    lex.TOKEN_KEYWORD_AVG: OPCODE_AVG,
    lex.TOKEN_KEYWORD_PRINT: OPCODE_PRINT,
    lex.TOKEN_KEYWORD_ADD: OPCODE_ADD,
    lex.TOKEN_KEYWORD_SUB: OPCODE_SUBTRACT,
    lex.TOKEN_KEYWORD_MULTIPLY: OPCODE_MULTIPLY,
    lex.TOKEN_KEYWORD_DIVIDE: OPCODE_DIVIDE,
}

'''
    Map keywords to the evaluating functions
'''
BUILTIN = {
    OPCODE_DUP: evaluate.dup,
    OPCODE_SWAP: evaluate.swap,
    OPCODE_ROT: evaluate.rot,
    OPCODE_DROP: evaluate.drop,
    OPCODE_AVG: evaluate.avg,
    OPCODE_PRINT: evaluate.printtop,
    OPCODE_ADD: evaluate.add,
    OPCODE_SUBTRACT: evaluate.subtract,
    OPCODE_MULTIPLY: evaluate.multiply,
    OPCODE_DIVIDE: evaluate.divide
}