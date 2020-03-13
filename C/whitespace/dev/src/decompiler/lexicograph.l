%{
    #include <stdio.h>
    #include "y.tab.h"
    #define  LOG 0  // Set log to 1 to print matched tokens
%}
%%
"  "      { if(LOG){printf("tINS_STACK_PUSH\n");}      return tINS_STACK_PUSH;     }
" \n "    { if(LOG){printf("tINS_STACK_DUP\n");}       return tINS_STACK_DUP;      }
" \n\t"   { if(LOG){printf("tINS_STACK_SWAP\n");}      return tINS_STACK_SWAP;     }
" \n\n"   { if(LOG){printf("tINS_STACK_POP\n");}       return tINS_STACK_POP;      }

"\t   "   { if(LOG){printf("tINS_ARITHMETIC_ADD\n");}  return tINS_ARITHMETIC_ADD; }
"\t  \t"  { if(LOG){printf("tINS_ARITHMETIC_SUB\n");}  return tINS_ARITHMETIC_SUB; }
"\t  \n"  { if(LOG){printf("tINS_ARITHMETIC_MUL\n");}  return tINS_ARITHMETIC_MUL; }
"\t \t "  { if(LOG){printf("tINS_ARITHMETIC_DIV\n");}  return tINS_ARITHMETIC_DIV; }
"\t \t\t" { if(LOG){printf("tINS_ARITHMETIC_MOD\n");}  return tINS_ARITHMETIC_MOD; }

"\t\t "   { if(LOG){printf("tINS_HEAP_STORE\n");}      return tINS_HEAP_STORE;     }
"\t\t\t"  { if(LOG){printf("tINS_HEAP_LOAD\n");}       return tINS_HEAP_LOAD;      }

"\n  "    { if(LOG){printf("tINS_FLOW_LBL\n");}        return tINS_FLOW_LBL;       }
"\n \t"   { if(LOG){printf("tINS_FLOW_CALL\n");}       return tINS_FLOW_CALL;      }
"\n \n"   { if(LOG){printf("tINS_FLOW_JMP\n");}        return tINS_FLOW_JMP;       }
"\n\t "   { if(LOG){printf("tINS_FLOW_JMPZ\n");}       return tINS_FLOW_JMPZ;      }
"\n\t\t"  { if(LOG){printf("tINS_FLOW_JMPN\n");}       return tINS_FLOW_JMPN;      }
"\n\t\n"  { if(LOG){printf("tINS_FLOW_LEAVE\n");}      return tINS_FLOW_LEAVE;     }
"\n\n\n"  { if(LOG){printf("tINS_FLOW_END\n");}        return tINS_FLOW_END;       }

"\t\n  "   { if(LOG){printf("tINS_IO_PRINTC\n");}      return tINS_IO_PRINTC;      }
"\t\n \t"  { if(LOG){printf("tINS_IO_PRINTN\n");}      return tINS_IO_PRINTN;      }
"\t\n\t "  { if(LOG){printf("tINS_IO_READC\n");}       return tINS_IO_READC;       }
"\t\n\t\t" { if(LOG){printf("tINS_IO_READN\n");}       return tINS_IO_READN;       }

[\t ]*[\n] { if(LOG){printf("tLABEL_OR_NUMBER\n");}    return tLABEL_OR_NUMBER;    }
.          { if(LOG){printf(".\n");}                   return tANYTHING;           }
