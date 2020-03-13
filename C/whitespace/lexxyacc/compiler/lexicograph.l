%{
    #include <stdio.h>
    #include "y.tab.h"
    #define  LOG 0  // Set log to 1 to print matched tokens
%}
%%
"\t"   { if(LOG){ECHO;}return tCONST;}





[0-9]+    { if(LOG){ECHO;}/*printf("tNB:%d\n",atoi(yytext));*/ yylval.entier=atoi(yytext); return tNB;}
[A-Za-z][A-Za-z_0-9]* { if(LOG){ECHO;}yylval.str=strdup(yytext); /*printf("tID:%s\n",yytext);*/ return tID;}
[/]{2}[\t A-Za-z_0-9]*[\n] { if(LOG){printf("tCOMMENT : %s",yytext);}}
.  {printf("something \n");}
