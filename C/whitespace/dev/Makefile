.PHONY: all clean compile

SRCDIR=./src
BINDIR=./bin

LEXFILE=lexicograph.l
YACCFILE=compiler.y
# TESTFILE=testfile.c
OUT_COMPILER=compiler
OUT_DECOMPILER=decompiler
OUT_LEX=lexicograph

CC := gcc
CCFLAGS := -Wall

all : clean compile

compile : mk_compiler clean mk_decompiler mk_interpreter
	@#gcc ${SRCDIR}/lib/labelparser.c -o ${BINDIR}/labelparser

clean :
	 @if [ -f "${BINDIR}/wscc" ]; then rm "${BINDIR}/wscc"; fi
	 @if [ -f "${BINDIR}/ws" ]; then   rm "${BINDIR}/ws";   fi
	 @if [ -f ${BINDIR}/y.tab.c ] ;		then rm ${BINDIR}/y.tab.c ; 	fi;
	 @if [ -f ${BINDIR}/y.tab.h ] ;		then rm ${BINDIR}/y.tab.h ; 	fi;
	 @if [ -f ${BINDIR}/lex.yy.c ] ;		then rm ${BINDIR}/lex.yy.c ; fi;
	 @if [ -f ${BINDIR}/${OUT_COMPILER} ] ;	then rm ${BINDIR}/${OUT_COMPILER}; fi;
	 @if [ -f ${BINDIR}/${OUT_DECOMPILER} ] ;	then rm ${BINDIR}/${OUT_DECOMPILER}; fi;
	 @if [ -f ${BINDIR}/${OUT_LEX} ] ;	then rm ${BINDIR}/${OUT_LEX}; fi;

mk_interpreter:
	@# @echo "==[INTERPRETER]==================================================="
	@# @$(CC) $(CCFLAGS) ${SRCDIR}/ws.c -o ${BINDIR}/ws
	@# @echo "  CC  CCFLAGS ${SRCDIR}/ws.c -o ${BINDIR}/ws"
	@# @$(CC) $(CCFLAGS) ${SRCDIR}/wscc.c -o ${BINDIR}/wscc
	@# @echo "  CC  CCFLAGS ${SRCDIR}/wscc.c -o ${BINDIR}/wscc"

mk_decompiler:
	@echo "==[DECOMPILER]===================================================="
	yacc -d ${SRCDIR}/decompiler/decompiler.y -o ${BINDIR}/y.tab.c
	flex -o ${BINDIR}/lex.yy.c ${SRCDIR}/decompiler/${LEXFILE}
	gcc ${BINDIR}/y.tab.c ${BINDIR}/lex.yy.c ${SRCDIR}/lib/labelparser.c \
		-I ${SRCDIR}/lib/ \
		-o ${BINDIR}/${OUT_DECOMPILER} -ly -ll
	@if [ -f ${BINDIR}/y.tab.c ] ;		then rm ${BINDIR}/y.tab.c ; 	fi;
	@if [ -f ${BINDIR}/y.tab.h ] ;		then rm ${BINDIR}/y.tab.h ; 	fi;
	@if [ -f ${BINDIR}/lex.yy.c ] ;		then rm ${BINDIR}/lex.yy.c ; fi;

mk_compiler:
	@echo "==[COMPILER]======================================================"
	yacc -d ${SRCDIR}/compiler/compiler.y -o ${BINDIR}/y.tab.c
	flex -o ${BINDIR}/lex.yy.c ${SRCDIR}/compiler/${LEXFILE}
	gcc ${SRCDIR}/wscc.c ${BINDIR}/y.tab.c ${BINDIR}/lex.yy.c ${SRCDIR}/lib/labelparser.c \
		-I ${SRCDIR}/lib/ \
		-o ${BINDIR}/${OUT_COMPILER} -ly -ll


	@if [ -f ${BINDIR}/y.tab.c ] ;		then rm ${BINDIR}/y.tab.c ; 	fi;
	@if [ -f ${BINDIR}/y.tab.h ] ;		then rm ${BINDIR}/y.tab.h ; 	fi;
	@if [ -f ${BINDIR}/lex.yy.c ] ;		then rm ${BINDIR}/lex.yy.c ; fi;
