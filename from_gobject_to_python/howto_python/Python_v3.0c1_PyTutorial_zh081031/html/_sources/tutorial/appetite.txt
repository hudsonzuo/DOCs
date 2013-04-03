.. _tut-intro:

**********************
Whetting Your Appetite 开胃菜
**********************

If you do much work on computers, eventually you find that there's some task
you'd like to automate.  For example, you may wish to perform a
search-and-replace over a large number of text files, or rename and rearrange a
bunch of photo files in a complicated way. Perhaps you'd like to write a small
custom database, or a specialized GUI application, or a simple game.

如果你要用计算机做很多工作，希望可以自动完成其中的一些任务。例如，你可能希望在大量的文本文件中进
行查找替换操作，也许是以复杂的方式重命名并整理大量图片。可能你想要编写一个小型的定制数据库，或者
一个特殊的图形界面程序，或者一个小型的游戏。

If you're a professional software developer, you may have to work with several
C/C++/Java libraries but find the usual write/compile/test/re-compile cycle is
too slow.  Perhaps you're writing a test suite for such a library and find
writing the testing code a tedious task.  Or maybe you've written a program that
could use an extension language, and you don't want to design and implement a
whole new language for your application.

如果你是一个专业的开发者，你可能不得不用到很多的C/C++/Java库工作，而且编写/编译/测试/重编译周
期太长了，可能你在可能你在给每个库编写对应的测试代码，但发现这是个烦人的活。或者你在编写一个程序，
需要用到一门扩展语言，但是你又不想重新设计和实现一套。

Python is just the language for you.

那么 Python 就是你需要的语言。

You could write a Unix shell script or Windows batch files for some of these
tasks, but shell scripts are best at moving around files and changing text data,
not well-suited for GUI applications or games. You could write a C/C++/Java
program, but it can take a lot of development time to get even a first-draft
program.  Python is simpler to use, available on Windows, MacOS X, and Unix
operating systems, and will help you get the job done more quickly.

你能够针对一些任务编写 Unix Shell 脚本或者 Windows 批处理文件，但是脚本语言最擅长移动文件
和修改文本数据，不适合 GUI 程序或游戏。你能写 C/C++/Java 程序，但是这些技本就是开发最简单
的程序也要用去大量的时间。无论在 Windows 、MacOS 或 Unix 操作系统上， Python 非常易于使
用，可以帮助你更快的完成任务。

Python is simple to use, but it is a real programming language, offering much
more structure and support for large programs than shell scripts or batch files
can offer.  On the other hand, Python also offers much more error checking than
C, and, being a *very-high-level language*, it has high-level data types built
in, such as flexible arrays and dictionaries.  Because of its more general data
types Python is applicable to a much larger problem domain than Awk or even
Perl, yet many things are at least as easy in Python as in those languages.

Python 很容易上手，但它是一门真正的编程语言，相对于 Shell ，它提供的针对大型程序的支持和结
构要多的多。另一方面，它提供了比 C 更多的错误检查，并且，作为一门 *非常高级的语言* ，它拥有
内置的高级数据结构类型，例如可变数组和字典。因为拥有更多的通用数据类型， Python 适合比 Awk 
甚至 Perl 更广泛的问题领域，在其它的很多领域， Python 至少比别的语言要易用的多。

Python allows you to split your program into modules that can be reused in other
Python programs.  It comes with a large collection of standard modules that you
can use as the basis of your programs --- or as examples to start learning to
program in Python.  Some of these modules provide things like file I/O, system
calls, sockets, and even interfaces to graphical user interface toolkits like
Tk.

Python 可以让你把自己的程序分隔成不同的模块，以便在其它的 Python 程序中重用。你可以让自己的程
序基于一个很大的标准模块集－－或者用它们做为开始学习 Python 编程的示例。这些模块中包含诸如文件 
I/O ，系统调用， sockets 甚至类似 TK 这样的图形接口。

Python is an interpreted language, which can save you considerable time during
program development because no compilation and linking is necessary.  The
interpreter can be used interactively, which makes it easy to experiment with
features of the language, to write throw-away programs, or to test functions
during bottom-up program development. It is also a handy desk calculator.

Python 是一门解释型语言，因为不需要编译和链接的时间，它可以帮你省下一些开发时间。解释器可以交
互式的使用，基于语言给定的功能，你可以写一些实验性质的程序，扔掉也无所谓。或者还可以当它是一个
随手可得的计算器。

Python enables programs to be written compactly and readably.  Programs written
in Python are typically much shorter than equivalent C,  C++, or Java programs,
for several reasons:

Python 可以写出很紧凑的，可读性很强的程序。用 Python 写的程序通常比同样的 C , C++ 或 Java 
程序要短得多，这是因为以下几个原因：

* the high-level data types allow you to express complex operations in a single
  statement;

* 高级数据结构使你可以在一个单独的语言中表达中很复杂的操作；

* statement grouping is done by indentation instead of beginning and ending
  brackets;

* 语句的组织依赖于缩进而不是 开始/结束（类似 C 族语言的 {} 符号或 Pascal 的begin/end关键字）标记块；

* no variable or argument declarations are necessary.

* 参数或变量不需要声明。

Python is *extensible*: if you know how to program in C it is easy to add a new
built-in function or module to the interpreter, either to perform critical
operations at maximum speed, or to link Python programs to libraries that may
only be available in binary form (such as a vendor-specific graphics library).
Once you are really hooked, you can link the Python interpreter into an
application written in C and use it as an extension or command language for that
application.

Python 是可扩展的：如果你会用 C 写程序，就可以很容易的为解释器添加新的 built-in 函数或模块，
或者优化性能瓶颈，使其达到最大速度，或者使 Python 能够链接到必要的二进制架构（比如某个专用的商
业图形库）。一旦你真正掌握了它，你可以将 Python 集成进由 C 写成的程序，把 Python 当做是这个
程序的扩展或命令行语言。

By the way, the language is named after the BBC show "Monty Python's Flying
Circus" and has nothing to do with nasty reptiles.  Making references to Monty
Python skits in documentation is not only allowed, it is encouraged!

顺便说一下，这个语言的名字来自于 BBC 的 “Monty Python's Flying Circus” 节目，和凶猛的
爬行类生物没有任何关系。在文档中引用 Monty Python 的典故不仅可行，而且值得鼓励！

Now that you are all excited about Python, you'll want to examine it in some
more detail.  Since the best way to learn a language is to use it, the tutorial
invites you to play with the Python interpreter as you read.

现在我们已经了解了 Python 中所有激动人心的东西，大概你想仔细的试试它了。学习一门语言最好的办法
就是使用它，如你所读到的，本文会引领你运用 Python 解释器。

.. % \section{Where From Here \label{where}}

In the next chapter, the mechanics of using the interpreter are explained.  This
is rather mundane information, but essential for trying out the examples shown
later.

下一节中，我们直接说明解释器的用法，这没有什么神秘的内容，不过有助于我们练习后面展示的例子。

The rest of the tutorial introduces various features of the Python language and
system through examples, beginning with simple expressions, statements and data
types, through functions and modules, and finally touching upon advanced
concepts like exceptions and user-defined classes.

本指南其它部分通过示例介绍了 Python 语言和系统的各种功能，开始是简单表达式，语法和数据类型，接
上来是函数和模块，最后是诸如异常和自定义类这样的高级内容。
