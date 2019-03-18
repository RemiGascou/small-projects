# buffertools

## bufferdump

```c
int bufferdump(char * buffer, int size);
```

Prints the content of the buffer. Also detects the first string (up to the first ```\0```)

## rst

```c
int rst(char * buffer, int size);
```

Fills the buffer with ```\0```.


## fill

```c
int fill(char * buffer, int size, char c);
```

Fills the buffer with the given character ```char c```.
