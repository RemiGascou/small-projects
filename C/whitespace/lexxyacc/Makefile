LEXFILE=lexicograph.l
YACCFILE=compiler.y
# TESTFILE=testfile.c
OUTBINARY=compiler
OUTBINARY_LEX=lexicograph
OUTDIR=./compiler/

all: compile

compile: mk_yacc_tab mk_lex_yy
	gcc ${OUTDIR}y.tab.c ${OUTDIR}lex.yy.c -o ${OUTDIR}${OUTBINARY} -ly -ll

mk_yacc_tab: ${OUTDIR}${YACCFILE}
	yacc -d ${OUTDIR}${YACCFILE} -o ${OUTDIR}y.tab.c

mk_lex_yy: ${OUTDIR}${LEXFILE}
	flex -o ${OUTDIR}lex.yy.c ${OUTDIR}${LEXFILE}

clean:
	@if [ -f ${OUTDIR}y.tab.c ] ;		then rm ${OUTDIR}y.tab.c ; 	fi;
	@if [ -f ${OUTDIR}y.tab.h ] ;		then rm ${OUTDIR}y.tab.h ; 	fi;
	@if [ -f ${OUTDIR}lex.yy.c ] ;		then rm ${OUTDIR}lex.yy.c ; 	fi;
	@if [ -f ${OUTDIR}${OUTBINARY} ] ;	then rm ${OUTDIR}${OUTBINARY}; fi;
	@if [ -f ${OUTDIR}${OUTBINARY_LEX} ] ;	then rm ${OUTDIR}${OUTBINARY_LEX}; fi;
