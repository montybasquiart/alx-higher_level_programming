#  0x00-python-hello_world

## Resources
Read or watch:

 * [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
 * [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)

## A README file describing what each script is doing

```
Zen

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
##
0. Run Python file - [0-run](./0-run) - A Shell script that runs a Python script.
   * The Python file name will be saved in the environment variable $PYFILE
##
1. Run inline - [1-run_inline](./1-run_inline) - A Shell script that runs Python code.
   * The Python code will be saved in the environment variable $PYCODE
##
2. Hello, print - [2-print.py](./2-print.py) - A Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
   * Use the function print
##
3. Print integer - [3-print_number.py](./3-print_number.py) - A script to print the integer stored in the variable number, followed by Battery street, followed by a new line.
   * You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
   * The output of the script should be:
   * the number, followed by Battery street,
   * followed by a new line
   * You are not allowed to cast the variable number into a string
   * Your code must be 3 lines long
   * You have to use f-strings [tips](https://realpython.com/python-f-strings/)
##
4. Print float - [4-print_float.py](./4-print_float.py) - A script to print the float stored in the variable number with a precision of 2 digits.
   * You can find the source code here
    * The output of the program should be:
    	* Float:, followed by the float with only 2 digits
	* followed by a new line
    * You are not allowed to cast number to string
    * You have to use f-strings
##
5. Print string - [5-print_string.py](./5-print_string.py) - A script to print 3 times a string stored in the variable str, followed by its first 9 characters.
You can find the source code here
    * The output of the program should be:
    * 3 times the value of str
    * followed by a new line
    * followed by the 9 first characters of str
    * followed by a new line
    * You are not allowed to use any loops or conditional statement
    * Your program should be maximum 5 lines long
##
6. Play with strings - [6-concat.py](./6-concat.py) - A script to print Welcome to Holberton School! using this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
   * You can find the source code here
   * You are not allowed to use any loops or conditional statements.
   * You have to use the variables str1 and str2 in your new line of code
   * Your program should be exactly 5 lines long
##
7. Copy - Cut - Paste - [7-edges.py](./7-edges.py) - Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
   * You can find the source code [here](./https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
   * You are not allowed to use any loops or conditional statements 
   * Your program should be exactly 8 lines long
   * word_first_3 should contain the first 3 letters of the variable word
   * word_last_2 should contain the last 2 letters of the variable word
   * middle_word should contain the value of the variable word without the first and last letters
##
8. Create a new sentence - [8-concat_edges.py](./8-concat_edges.py) - A script to print object-oriented programming with Python, followed by a new line.
   * You can find the source code [here](./https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
   * You are not allowed to use any loops or conditional statements
   * Your program should be exactly 5 lines long
   * You are not allowed to create new variables
   * You are not allowed to use string literals

9. Easter Egg - [9-easter_egg.py](./9-easter_egg.py) - A Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

   * Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
##
10. Linked list cycle - [10-check_cycle.c](./10-check_cycle.c) - Technical interview preparation:

    * You are not allowed to google anything
    * Whiteboard first
    * This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
* Write a function in C that checks if a singly linked list has a cycle in it.

    * Prototype: int check_cycle(listint_t *list);
    * Return: 0 if there is no cycle, 1 if there is a cycle
* Requirements:
    * Only these functions are allowed: write, printf, putchar, puts, malloc, free
##
11. Hello, write - [100-write.py](./100-write.py) - A Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

    * Use the function write from the sys module
    * You are not allowed to use print
    * Your script should print to stderr
    * Your script should exit with the status code 1
##
12. Compile - [101-compile](./101-compile) - A script that compiles a Python script file.

    * The Python file name will be stored in the environment variable $PYFILE

    * The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
##
13. ByteCode -> Python #1 - [102-magic_calculation.py](./102-magic_calculation.py) - A Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:



