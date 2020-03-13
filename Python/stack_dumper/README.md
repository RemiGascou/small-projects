# StackDumper

*Searching strings like needles in in a (hay)stack*

Utility to dump the strings in the stack of a "format string" vulnerable binary executable file.

## Usage :

```
./stack_dumper.py -h
usage: stack_dumper.py [-h] -f FILE [-q] [--csv CSV]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  String format vulnerable binary file to attack
  -q, --quiet           Quiet output
  --csv CSV             Exports findings to CSV file.
```


Quietly dumps the strings in the stack to a CSV file :

```
./stack_dumper.py --file ./vulnerable_binary
```


Quietly dumps the strings in the stack to a CSV file :

```
./stack_dumper.py --file ./vulnerable_binary --quiet --csv out.csv
```

## Example output

```
$ python3 stack_dumper.py --file vulnerable_binary

[+]====================================================
[+]           Strings stack dumper v1.0.1
[+] Searching strings like needles in in a (hay)stack
[+]====================================================

[%ebp - 1  ] e0c59760 -> AWAVI\x89\xd7AUATL\x8d%>\x06
[%ebp - 4  ] 18c827b8 -> \xb2S\x9b\x13\xfd\x7f
[%ebp - 7  ] 259dd82c -> Another one bites the dust !
[%ebp - 8  ] f449f81b -> TOUM, TOUM, TOUM
[%ebp - 9  ] 59dae805 -> A string in main(...)
```


## Developpement

### Function stack_dump

Dumps the stack from a vulnerable binary file using format strings.

Returns a list `stack` of lists `stack_entry`

A `stack_entry` list is composed ass follows : `[offset_from_ebp, adress, string_found_at_address]`

**Prototype :**

```python
def stack_dump(binfile, verbose=False, max_depth=150): [...]
```

### Function stack_to_csv

Dumps the stack from a vulnerable binary file using format strings.

Takes a list `stack` of lists `stack_entry` in input. A `stack_entry` list is composed ass follows : `[offset_from_ebp, adress, string_found_at_address]`

**Prototype :**

```python
def stack_to_csv(stack:list, outcsvfile): [...]
```


### Function cleanup_printable

Prints all printable characters as is, but non-printable characters in hexadecimal format (example : in format `\xd4`).

**Prototype :**

```python
def cleanup_printable(inputstring): [...]
```
