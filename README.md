# PyRPN
Mini Reverse Polish Notation (Postfix notation) parser and evaluator

It uses a stack based system.


| Keyword | Definition                                            | Stack Before | Stack After |
|---------|-------------------------------------------------------|--------------|-------------|
| `dup`   | Duplicates the stack top                              | 5 5 4        | 5 5 4 4     |
| `swap`  | Swap the top 2 stack items                            | 1 2 3        | 1 3 2       |
| `rot`   | Rotates the top 3 stack items                         | 1 2 3        | 3 1 2       |
| `drop`  | Removes the last stack item                           | 1 2 3        | 1 2         |
| `sum`   | Sums up the stack, and pushes the result              | 1 2 3        | 6           |
| `avg`   | Averages the stack, pushes result                     | 2 4 6        | 3           |
| `print` | Pops and prints the stack top                         | 5 5          | 5           |
| `+`     | Adds the top two stack items, pushes the result       | 5 10 15      | 5 25        |
| `-`     | Subtracts the top two stack items, pushes the result  | 5 10 15      | 5 -5        |
| `*`     | Multiplies the top two stack items, pushes the result | 2 5.5 2      | 11.0        |
| `/`     | Divides the top two stack items, pushes the result    | 5 10 2       | 5 5         |

Example:

Input: `15.5 1.5 + 2 swap + 2 5 * - print `

Output: `-9.0`
