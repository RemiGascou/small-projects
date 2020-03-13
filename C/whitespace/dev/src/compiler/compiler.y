%{
    #include <stdio.h>
    #include "labelparser.h"

    int yylex(void);
    void yyerror(const char* error);
%}

%define parse.error verbose /* pour récupérer des détails sur les erreurs avec yacc -v ./compiler/compiler.y */


/* Keywords */
/* Stack */
%token tINS_STACK_PUSH
%token tINS_STACK_POP
%token tINS_STACK_DUP
%token tINS_STACK_SWAP

/* Arithmetic */
%token tINS_ARITHMETIC_ADD
%token tINS_ARITHMETIC_SUB
%token tINS_ARITHMETIC_MUL
%token tINS_ARITHMETIC_DIV
%token tINS_ARITHMETIC_MOD

/* Heap Access */
%token tINS_HEAP_STORE
%token tINS_HEAP_LOAD


/* Flow Control */
%token tINS_FLOW_LBL
%token tINS_FLOW_CALL
%token tINS_FLOW_JMP
%token tINS_FLOW_JMPZ
%token tINS_FLOW_JMPN
%token tINS_FLOW_LEAVE
%token tINS_FLOW_END

/* IO */
%token tINS_IO_PRINTC
%token tINS_IO_PRINTN
%token tINS_IO_READC
%token tINS_IO_READN

%token tLABEL_OR_NUMBER

%token tANYTHING

/* Priorité des opérateurs pour l'arithmétique (priorité croissante) */
// %left tPLUS tMINUS
// %left tDIV tMUL


%start entry_point;

%%
entry_point           : Instructions;
Instructions          : Instruction | Instruction Instructions;
Instruction           : IMP_Stack
                      | IMP_Arithmetic
                      | IMP_Heap
                      | IMP_Flow_Control
                      | IMP_IO
                      | tANYTHING
		              ;



IMP_Stack             : INS_Stack_Push
                      | INS_Stack_Pop
                      | INS_Stack_Dup
                      | INS_Stack_Swap
		              ;

INS_Stack_Push        : tINS_STACK_PUSH;
INS_Stack_Pop         : tINS_STACK_POP;
INS_Stack_Dup         : tINS_STACK_DUP;
INS_Stack_Swap        : tINS_STACK_SWAP;



IMP_Arithmetic        : INS_Arithmetic_ADD
                      | INS_Arithmetic_SUB
                      | INS_Arithmetic_MUL
                      | INS_Arithmetic_DIV
                      | INS_Arithmetic_MOD
		      ;

INS_Arithmetic_ADD    : tINS_ARITHMETIC_ADD;
INS_Arithmetic_SUB    : tINS_ARITHMETIC_SUB;
INS_Arithmetic_MUL    : tINS_ARITHMETIC_MUL;
INS_Arithmetic_DIV    : tINS_ARITHMETIC_DIV;
INS_Arithmetic_MOD    : tINS_ARITHMETIC_MOD;



IMP_Heap              : INS_Heap_STORE
                      | INS_Heap_LOAD
		      ;

INS_Heap_STORE        : tINS_HEAP_STORE;
INS_Heap_LOAD         : tINS_HEAP_LOAD;




IMP_Flow_Control      : INS_Flow_LBL
                      | INS_Flow_CALL
                      | INS_Flow_JMP
                      | INS_Flow_JMPZ
                      | INS_Flow_JMPN
                      | INS_Flow_LEAVE
                      | INS_Flow_END
		      ;

INS_Flow_LBL          : tINS_FLOW_LBL  tLABEL_OR_NUMBER;
INS_Flow_CALL         : tINS_FLOW_CALL tLABEL_OR_NUMBER;
INS_Flow_JMP          : tINS_FLOW_JMP  tLABEL_OR_NUMBER;
INS_Flow_JMPZ         : tINS_FLOW_JMPZ tLABEL_OR_NUMBER;
INS_Flow_JMPN         : tINS_FLOW_JMPN tLABEL_OR_NUMBER;
INS_Flow_LEAVE        : tINS_FLOW_LEAVE ;
INS_Flow_END          : tINS_FLOW_END ;


IMP_IO                : INS_IO_PrintC
                      | INS_IO_PrintN
                      | INS_IO_ReadC
                      | INS_IO_ReadN
                      ;

INS_IO_PrintC         : tINS_IO_PRINTC;
INS_IO_PrintN         : tINS_IO_PRINTN;
INS_IO_ReadC          : tINS_IO_READC;
INS_IO_ReadN          : tINS_IO_READN;
%%

void yyerror(const char* error) {
    printf("ERROR: %s\n", error);
}

/* int main(int argc, char const **argv) {
    yyparse();
    return 0;
} */
