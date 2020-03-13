#include <stdio.h>

/*
 * This is a WhiteSpace asm compiler
 *           wasm to ws
 */

// -h Displays help.
// -o [outfile] (Default : out.ws)

int yyparse();

int main(int argc, char const *argv[]) {
    if (argc < 2 || argc > 5) {
        printf("Usage : %s program.ws -h -o [outfile]\n", argv[0]);
    } else {
        yyparse();
    }
    return 0;
}
