# WhiteSpace ASM

## Stack Manipulation (IMP: [Space])

Stack manipulation is one of the more common operations, hence the shortness of the IMP [Space]. There are four stack instructions.

| Instruction | Parameters | Meaning                             | WS Command  |
|-------------|------------|-------------------------------------|-------------|
|   `push`    |   Number   | Push the number onto the stack      | [Space]     |
|   `dup`     |     -      | Duplicate the top item on the stack | [LF][Space] |
|   `swap`    |     -      | Swap the top two items on the stack | [LF][Tab]   |
|   `pop`     |     -      | Discard the top item on the stack   | [LF][LF]    |

## Arithmetic (IMP: [Tab][Space])

Arithmetic commands operate on the top two items on the stack, and replace them with the result of the operation. The first item pushed is considered to be left of the operator.

| Instruction | Parameters | Meaning                             | WS Command     |
|-------------|------------|-------------------------------------|----------------|
|    `add`    |     -      | Addition                            | [Space][Space] |
|    `sub`    |     -      | Subtraction                         | [Space][Tab]   |
|    `mul`    |     -      | Multiplication                      | [Space][LF]    |
|    `div`    |     -      | Integer Division                    | [Tab][Space]   |
|    `mod`    |     -      | Modulo                              | [Tab][Tab]     |

## Heap Access (IMP: [Tab][Tab])

Heap access commands look at the stack to find the address of items to be stored or retrieved. To store an item, push the address then the value and run the store command. To retrieve an item, push the address and run the retrieve command, which will place the value stored in the location at the top of the stack.

| Instruction | Parameters | Meaning                             | WS Command |
|-------------|------------|-------------------------------------|------------|
| `store`     |      -     | Store                               | [Space]    |
| `retr`      |      -     | Retrieve                            | [Tab]      |

## Flow Control (IMP: [LF])

Flow control operations are also common. Subroutines are marked by labels, as well as the targets of conditional and unconditional jumps, by which loops can be implemented. Programs must be ended by means of [LF][LF][LF] so that the interpreter can exit cleanly.

| Instruction | Parameters | Meaning                                                  | WS Command     |
|-------------|------------|----------------------------------------------------------|----------------|
|   `lbl`     |  Label	   | Mark a location in the program                           | [Space][Space] |
|   `call`    |  Label	   | Call a subroutine                                        | [Space][Tab]   |
|   `jmp`     |  Label	   | Jump unconditionally to a label                          | [Space][LF]    |
|   `jmpz`    |  Label	   | Jump to a label if the top of the stack is zero          | [Tab][Space]   |
|   `jmpn`    |  Label	   | Jump to a label if the top of the stack is negative      | [Tab][Tab]     |
|   `leave`   |    -       | End a subroutine and transfer control back to the caller | [Tab][LF]      |
|   `end`     |    -	   | End the program                                          | [LF][LF]       |

## I/O (IMP: [Tab][LF])

Finally, we need to be able to interact with the user. There are IO instructions for reading and writing numbers and individual characters. With these, string manipulation routines can be written.

The read	instructions take the heap address in which to store the result from the top of the stack.

| Instruction | Parameters | Meaning                                                                     | WS Command     |
|-------------|------------|-----------------------------------------------------------------------------|----------------|
|  `printc`   |     -      | Output the character at the top of the stack                                | [Space][Space]
|  `printn`   |     -      | Output the number at the top of the stack                                   | [Space][Tab]
|  `readc`    |     -      | Read a character and place it in the location given by the top of the stack | [Tab][Space]
|  `readn`    |     -      | Read a number and place it in the location given by the top of the stack    | [Tab][Tab]
