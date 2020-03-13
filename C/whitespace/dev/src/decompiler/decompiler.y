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

INS_Stack_Push        : tINS_STACK_PUSH { printf("push   \n"); };
INS_Stack_Pop         : tINS_STACK_POP  { printf("pop    \n"); };
INS_Stack_Dup         : tINS_STACK_DUP  { printf("dup    \n"); };
INS_Stack_Swap        : tINS_STACK_SWAP { printf("swap   \n"); };



IMP_Arithmetic        : INS_Arithmetic_ADD
                      | INS_Arithmetic_SUB
                      | INS_Arithmetic_MUL
                      | INS_Arithmetic_DIV
                      | INS_Arithmetic_MOD
                      ;

INS_Arithmetic_ADD    : tINS_ARITHMETIC_ADD { printf("add    \n"); };
INS_Arithmetic_SUB    : tINS_ARITHMETIC_SUB { printf("sub    \n"); };
INS_Arithmetic_MUL    : tINS_ARITHMETIC_MUL { printf("mul    \n"); };
INS_Arithmetic_DIV    : tINS_ARITHMETIC_DIV { printf("div    \n"); };
INS_Arithmetic_MOD    : tINS_ARITHMETIC_MOD { printf("mod    \n"); };



IMP_Heap              : INS_Heap_STORE
                      | INS_Heap_LOAD
                      ;

INS_Heap_STORE        : tINS_HEAP_STORE { printf("store  \n"); };
INS_Heap_LOAD         : tINS_HEAP_LOAD  { printf("load   \n"); };




IMP_Flow_Control      : INS_Flow_LBL
                      | INS_Flow_CALL
                      | INS_Flow_JMP
                      | INS_Flow_JMPZ
                      | INS_Flow_JMPN
                      | INS_Flow_LEAVE
                      | INS_Flow_END
                      ;

INS_Flow_LBL          : tINS_FLOW_LBL   { printf("lbl    "); } tLABEL_OR_NUMBER { printf(" ...\n"); };
INS_Flow_CALL         : tINS_FLOW_CALL  { printf("call   "); } tLABEL_OR_NUMBER { printf(" ...\n"); };
INS_Flow_JMP          : tINS_FLOW_JMP   { printf("jmp    "); } tLABEL_OR_NUMBER { printf(" ...\n"); };
INS_Flow_JMPZ         : tINS_FLOW_JMPZ  { printf("jmpz   "); } tLABEL_OR_NUMBER { printf(" ...\n"); };
INS_Flow_JMPN         : tINS_FLOW_JMPN  { printf("jmpn   "); } tLABEL_OR_NUMBER { printf(" ...\n"); };
INS_Flow_LEAVE        : tINS_FLOW_LEAVE { printf("leave  \n"); };
INS_Flow_END          : tINS_FLOW_END   { printf("end    \n"); };


IMP_IO                : INS_IO_PrintC
                      | INS_IO_PrintN
                      | INS_IO_ReadC
                      | INS_IO_ReadN
                      ;

INS_IO_PrintC         : tINS_IO_PRINTC { printf("printc \n"); };
INS_IO_PrintN         : tINS_IO_PRINTN { printf("printn \n"); };
INS_IO_ReadC          : tINS_IO_READC  { printf("readc  \n"); };
INS_IO_ReadN          : tINS_IO_READN  { printf("readn  \n"); };
%%

void yyerror(const char* error) {
    printf("\r\x1b[1;91mError :\x1b[0m %s\n", error);
}

void yywarn(const char* error) {
    printf("\r\x1b[1;95mWarn :\x1b[0m %s\n", error);
}

int main(int argc, char const **argv) {
    yyparse();
    return 0;
}
