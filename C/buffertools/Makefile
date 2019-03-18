OUTBINARY=dump
CC=gcc
FLAGS=-Wall
CSOURCE=dump.c
CLIBS=buffertools.c

all : clean build

build:
	${CC} ${FLAGS} ${CSOURCE} ${CLIBS} -o ${OUTBINARY}

clean:
	@if [ -f ${OUTBINARY} ] ;	then rm ${OUTBINARY}; fi;
