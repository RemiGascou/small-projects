.PHONY: all clean compile

CC := gcc
CCFLAGS := -O0 -m64 -g -fno-stack-protector
OUTBINARY := vulnerable_binary
SRCFILES := vulnerable_binary.c

all : compile

compile :
	$(CC) $(CCFLAGS) $(SRCFILES) -o $(OUTBINARY)

clean :
	@if [ -f "${OUTBINARY}" ]; then rm "${OUTBINARY}"; fi
