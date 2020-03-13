%{
    #include <stdio.h>
    #include "y.tab.h"
    #define  LOG 0  // Set log to 1 to print matched tokens
%}
%%
"push"    { if(LOG){printf("tINS_STACK_PUSH\n");}      return tINS_STACK_PUSH;     }
"dup"     { if(LOG){printf("tINS_STACK_DUP\n");}       return tINS_STACK_DUP;      }
"swap"    { if(LOG){printf("tINS_STACK_SWAP\n");}      return tINS_STACK_SWAP;     }
"pop"     { if(LOG){printf("tINS_STACK_POP\n");}       return tINS_STACK_POP;      }

"add"     { if(LOG){printf("tINS_ARITHMETIC_ADD\n");}  return tINS_ARITHMETIC_ADD; }
"sub"     { if(LOG){printf("tINS_ARITHMETIC_SUB\n");}  return tINS_ARITHMETIC_SUB; }
"mul"     { if(LOG){printf("tINS_ARITHMETIC_MUL\n");}  return tINS_ARITHMETIC_MUL; }
"div"     { if(LOG){printf("tINS_ARITHMETIC_DIV\n");}  return tINS_ARITHMETIC_DIV; }
"mod"     { if(LOG){printf("tINS_ARITHMETIC_MOD\n");}  return tINS_ARITHMETIC_MOD; }

"store"   { if(LOG){printf("tINS_HEAP_STORE\n");}      return tINS_HEAP_STORE;     }
"load"    { if(LOG){printf("tINS_HEAP_LOAD\n");}       return tINS_HEAP_LOAD;      }

"lbl"     { if(LOG){printf("tINS_FLOW_LBL\n");}        return tINS_FLOW_LBL;       }
"call"    { if(LOG){printf("tINS_FLOW_CALL\n");}       return tINS_FLOW_CALL;      }
"jmp"     { if(LOG){printf("tINS_FLOW_JMP\n");}        return tINS_FLOW_JMP;       }
"jmpz"    { if(LOG){printf("tINS_FLOW_JMPZ\n");}       return tINS_FLOW_JMPZ;      }
"jmpn"    { if(LOG){printf("tINS_FLOW_JMPN\n");}       return tINS_FLOW_JMPN;      }
"leave"   { if(LOG){printf("tINS_FLOW_LEAVE\n");}      return tINS_FLOW_LEAVE;     }
"end"     { if(LOG){printf("tINS_FLOW_END\n");}        return tINS_FLOW_END;       }

"printc"  { if(LOG){printf("tINS_IO_PRINTC\n");}      return tINS_IO_PRINTC;      }
"printn"  { if(LOG){printf("tINS_IO_PRINTN\n");}      return tINS_IO_PRINTN;      }
"readc"   { if(LOG){printf("tINS_IO_READC\n");}       return tINS_IO_READC;       }
"readn"   { if(LOG){printf("tINS_IO_READN\n");}       return tINS_IO_READN;       }

[\t ]*[\n] { if(LOG){printf("tLABEL_OR_NUMBER\n");}    return tLABEL_OR_NUMBER;    }
.          { if(LOG){printf(".\n");}                   return tANYTHING;           }
