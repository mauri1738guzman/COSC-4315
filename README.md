COSC4315/COSC6345: A Mini-Interpreter Programmed in C++
Language: Python
1 Introduction
You will develop a mini-interpreter of an interpreted programming language. The “system” programming language is:
C++ (or pure C). The input source code will be: Python. You will create a program to evaluate list expressions, with
array-based lists (i.e. the most common list mechanism). There will also be simple arithmetic expressions.
Since Python and JavaScript are two dominating languages today, input files will have list manipulation code that will
be as similar as possible between both languages, other than minor syntax changes or different function names. In other
words, the knowledge you have on Python or JavaScript does help you solve this homework.
This “interpreter” program will be developed in C++ (but pure C is also acceptable). Notice that developing your
interpreter in an interpreted language like JavaScript, and Python itself is not acceptable since their libraries do 90% of the
work and you learn nothing. However, other compiled languages like Java or Kotlin can be considered (talk to instructor).
Theory in practice: Your program will use regular expressions to recognize identifiers (var/function names), numbers
and strings. Your program will implement a simplified context-free grammar to recognize arithmetic expressions with ’+’
(which may involve lists or integers). In order to detect and check data types you will have to perform evaluation using an
attribute grammar to extend the parse tree. Your program has to evaluate the code, line by line, exactly like the interpreter,
but your program does not have to generate intermediate or object code.

2 Input: source code file
The input is one source code file, passed as argument on the OS command line, working in the same manner as the
interpreter.

3 Requirements
The input program will contain the following statements (details in last section):

One statement per line. Therefore, semicolon is optional (not necessary).
variable assignment
Data types: integer or list. String: optional (read section below).
Data types out of scope: bool, string, real, time, classes.
Lists:
List expressions, with [] operator to access elements and + to add elements.
List arithmetic expressions, which can combine specific values simple values and list elements (one element, or
slice).
Arithmetic expressions.
The main arithmetic operator will be the ’+’ operator.
Out of scope, optional operators: * or - are optional.
if/else:
to control flow (The if condition will have only one comparison; without and/or/not). Parentheses are optional, but
unnecessary since the result will be the same. if/else can be nested up to 2 levels, either way.
Nesting: yes.
loops: no (optional).
Functions: definition and evaluation (call). One argument, simple data type.
Lists: optional.
Casting=no
You can assume there will be no function calls to convert data types (casting).
You cannot assume the program will be syntactically correct. That is, you have to detect errors (showing line
number).
4 OPTIONAL
You can develop additional language features. In order to do this you have to inform the TAs at least 2 weeks before
the deadline exactly which features you are programming. Extra credit will vary between 10 and 30 points towards this
homework to reach 100.
Choose 3 features at least:

Recursive functions OR recursive lambda expressions. This item includes defnition and evaluation.
Data types: strings, in addition to integers.
General arithmetic expressions: combining + - * / and (), with nesting.
Managing operator overloading: In the case of numbers + means addition, for strings it means concatenation and
for lists it means union.
Important warning: ’*’ is not possible for strings and lists in most languages (Python is a rare exception).
Function definitions with up to 2 arguments. Data types: integers, strings, lists. Evaluation: function call with
parameters passed by value.
General boolean expressions:and, or, notand parentheses.
while() loop, including nested loops+if/else, all of them recursively nested up to 3 levels.fordiscouraged as it is
less general.
Nested lists (list of lists) and mixed Lists, mixing data types.
OUT: Totally out of scope:
Non-linear recursion, mutual recursion, detecting potential infinite recursion
Higher order functions like currying, map() and reduce()
Casting, dynamic type conversion
Iterators
Classes, objects, garbage collection
Exceptions
Concurrency and parallelism
GUI
5 Program and output specification
The main program should be called ”minipython.cpp”. The compilation should be calling g++ by default as explained
below. If you decide to go for a larger project, using advanced C++ and C libraries you can use ’make’, but make it clear
in your readme file. One way or the other, your program should be easy to compile without errors and preferably without
warnings (-Wall).
Your program will be compiled:

g++ minipython.cpp -o ̃/bin/mini_python

Your program will behave exactly like the python interpreter (e.g. ”python3”). Call syntax from the OS prompt
(rename a.out!):

if in path or ̃/bin
minipython test1.py

default
./minipython test1.py

6 Requirements
One statement per line. Therefore, semicolon is not necessary.
In most test cases (not always), the input python program will be clean and there will be no syntax/type error.
However, in 2-3 test cases there can be minor syntax mistakes (missing parenthesis), extra statements (e.g. recursive
functions), unhandled data types (e.g. an object). In such incorrect case your program should halt and print() an
error message (short, fitting in one line).
Identifiers will be at most 10 characters.
Strings will be short: up to 5 characters.
Data type inference and checking: required.
You should store all the identifiers (variables) in some efficient data structure with access time O(1) or O(log(n));
avoidO(n)access. These include variable names. You have to create a ”binding” C++ data structure/class to track
data types and to store variable values; which must be highlighted in your README file.
You can store the list in arrays or linked lists. C++ STL can handle array resizing. If you use C arrays you can
assume some limits assuming the source code file is no more than 100 lines. You can assume lists will have no more
than 100 elements, but you should still aim to minimize RAM usage, especially for lists.
Scanning, Parsing and evaluation of source code: it is acceptable to make multiple passes, to detect identifiers,
check data types, generate an intermediate translated code representation and evaluate.
Testing: your interpreter should behave exactly like the Python interpreter and short messages in the same format.
The only exception is showing a variable with its name (use print()). A prompt is optional, but will not be used for
automated testing.
Your program should be able to display the variable content with a plain ”print(varname)”. Notice that using the
variable name alone, to display results like the Python interpreter introduces complications for parsing assignent
expressions and would push you to develop an interactive interpreter: this is discouraged as it messes some theory
principles.
Optional: You are encouraged to develop recursive C++ functions to manipulate the list and to evaluate arithmetic
expressions. You can use lambda expressions and functional libraries in C++.
Assume the list is strongly typed: all elements have the same data type. You can assign the data type of list l based
on element l[0]. In Python a list can mix data types, but in this homework we will take a stricter approach to simplify
development.
Arithmetic expression:
required: expression can have up to 20 operands combining + () [] and calling lambda functions.
optional: * - / and non-lambda function definitions and calls.
lambda calculus:
if there are two arguments there will be one arithmetic operator. the if functional expression will have only one
comparison (there are no ”and” ”or” boolean operators).
List access operators.
You need to program the [] operator to access one element or a ”slice” the list from theith element (entry [1]).
Examples: l[0] or l[1:].
The input is one .py file and it is self-contained (this source code file will not import other py files).
It is acceptable to have one variable instance, overwriting the previous ocurrence. That is, you do not have to create
new objects to avoid mutation.
You can use an existing Python parser or you can build your own. Tools like lex/flex, yacc/bison have way more
features than needed to solve this homework, but you can use them.
C++ libraries like regex are also great, but more general than needed for this homework.
You should use the Python interpreter to verify correctness of your program. You should interactively test your
program, comparing output with the interpreter. Keep in mind Python allows much more general lists than those
required in this homework.
The program is required to detect data type conflicts and print a warning or error.
There will not be ”cast” or type conversion function calls since that would require to track types in functions.
The program should not halt when encountering syntax or data type errors in the input source code.
Optional: For each variable you can store its data type and a list of lines where it was set or changed. Ths information
can be displayed in a ”varhistory.log” file to debug python code.
Your program should write error messages to a log file ”error.log” (and optionally to the screen). Your program
should not crash, halt unexpectedly or produce unhandled exceptions. Consider empty input, zeroes and inconsistent
information.
Test cases: Your program will be tested with 10 test files, going from easy to difficult. In general, each test case is
10 points off if your program produces incorrect results.
Source code: it will be checked for indentation, clarity, redundancy, efficiency and generality. It is expected you
have comments at the top giving and overview and for the most complex parts.
Your program will be executed using an automated script. Manual grading will be done only for regrading. There-
fore, make sure you follow the TAs instructions. Failure to follow instructions will result in failed test cases.
Submission: in 2 phases.
Phase 1: your program must pass simple test cases (4 test cases, simple expressions, short programs) and the grade
will be unofficial (just pass/fail). There will be a 3-day window to fix your program so that is passes. If your
program fails or you cannot submit a working program you have to talk to the instructor.
Phase 2: your program must handle any test case (10 test cases, longer, more complicated). You cannot submit in
Phase 2 if your program did not pass Phase 1. The TAs will grade your program and you will have a few days to fix
it: early resubmission encouraged for minor fixes.
Final recommendations: start immediately. Split the programming work: one person testing will be insufficient
(e.g. data type management, parsing, evaluation). It is very difficult to develop this homework in 2 weeks. It is
impossible to do it in 1 week or less. Due date will not be changed.
