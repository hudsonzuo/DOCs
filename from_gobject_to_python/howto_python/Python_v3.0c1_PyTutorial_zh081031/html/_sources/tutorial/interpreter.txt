.. _tut-using:

****************************
Using the Python Interpreter 使用 Python 解释器
****************************


.. _tut-invoking:

Invoking the Interpreter 调用 Python 解释器
========================

The Python interpreter is usually installed as :file:`/usr/local/bin/python` on
those machines where it is available; putting :file:`/usr/local/bin` in your
Unix shell's search path makes it possible to start it by typing the command ::

Python 解释器通常安装在目标机器的 :file:`/usr/local/bin/python` 目录下。
将 :file:`/usr/local/bin` 目录放进你的 Unix Shell 的搜索路径里，确保它可以通过输入

   python

to the shell.  Since the choice of the directory where the interpreter lives is
an installation option, other places are possible; check with your local Python
guru or system administrator.  (E.g., :file:`/usr/local/python` is a popular
alternative location.)

启动。因为安装路径是可选的，所以也可能安装在其它位置，你可以与安装 Python 的用户或系统管理员
联系.（例如，:file:`/usr/local/python` 就是一个很常见的选择）

On Windows machines, the Python installation is usually placed in
:file:`C:\Python30`, though you can change this when you're running the
installer.  To add this directory to your path,  you can type the following
command into the command prompt in a DOS box::

在 Windows 机器上， Python 通常安装在 :file:`C:\Python30` 目录。当然，我们可以在运行
安装程序的时候改变它。需要把这个目录加入到我们的 Path 中的话，可以像下面这样在 DOS 窗中输入命令行：

   set path=%path%;C:\python30

Typing an end-of-file character (:kbd:`Control-D` on Unix, :kbd:`Control-Z` on
Windows) at the primary prompt causes the interpreter to exit with a zero exit
status.  If that doesn't work, you can exit the interpreter by typing the
following commands: ``import sys; sys.exit()``.

输入一个文件结束符（ UNIX 上是 :kbd:`Control-D` ， Windows 上是 :kbd:`Control-Z` ）
解释器会以0值退出。如果没有起作用，你可以输入以下命令退出：``import sys; sys.exit()`` 。

The interpreter's line-editing features usually aren't very sophisticated.  On
Unix, whoever installed the interpreter may have enabled support for the GNU
readline library, which adds more elaborate interactive editing and history
features. Perhaps the quickest check to see whether command line editing is
supported is typing Control-P to the first Python prompt you get.  If it beeps,
you have command line editing; see Appendix :ref:`tut-interacting` for an
introduction to the keys.  If nothing appears to happen, or if ``^P`` is echoed,
command line editing isn't available; you'll only be able to use backspace to
remove characters from the current line.

解释器的行编辑功能并不复杂，装在 UNIX 上的解释器可能会有 GNU readline 库支持，这样就可以额外
得到精巧的交互编辑和历史记录功能。可能确认命令行编辑器支持能力最方便的方式是在主提示符下输入 
Control-P ，如果有嘟嘟声（计算机扬声器），说明你可以使用命令行编辑功能，从 :ref:`tut-interacting` 
可以查到快捷键的介绍。如果什么也没有发声，或者 ``^P`` 显示了出来，说明命令行编辑功能不可用，
你只有用退格键输入的命令了。

The interpreter operates somewhat like the Unix shell: when called with standard
input connected to a tty device, it reads and executes commands interactively;
when called with a file name argument or with a file as standard input, it reads
and executes a *script* from that file.

解释器的操作有些像 UNIX Shell ：使用终端设备作为标准输入来调用它时，解释器交互的解读和执行命令，
通过文件名参数或以文件作为标准输入时，它从文件中解读并执行脚本。

A second way of starting the interpreter is ``python -c command [arg] ...``,
which executes the statement(s) in *command*, analogous to the shell's
:option:`-c` option.  Since Python statements often contain spaces or other
characters that are special to the shell, it is best to quote  *command* in its
entirety with double quotes.

启动解释器的第二个方法是 ``python -c command [arg] ...`` ，这种方法可以在 *命令行* 
中直接执行语句，等同于 Shell 的 -c 选项。因为 Python 语句通常会包括空格之类的特殊字符，
所以最好把整个 *命令* 用双引号包起来。

Some Python modules are also useful as scripts.  These can be invoked using
``python -m module [arg] ...``, which executes the source file for *module* as
if you had spelled out its full name on the command line.

有一些 Python 模块也可以当作脚本使用。它们可以通过 ``python -m module [arg] ...`` 
调用，这如同在命令行中给出其完整文件名来运行一样。

Note that there is a difference between ``python file`` and ``python <file``.
In the latter case, input requests from the program, such as calling
``sys.stdin.read()``, are satisfied from *file*.  Since this file has already
been read until the end by the parser before the program starts executing, the
program will encounter end-of-file immediately.  In the former case (which is
usually what you want) they are satisfied from whatever file or device is
connected to standard input of the Python interpreter.

注意 ``python file`` 和 ``python <file`` 是有区别的。对于后一种情况，程序类似于调用 
``sys.stdin.read()`` ，来自于确定的文件。因为在解析器开始执行之前，文件已经完全读入，
所以程序指向文件尾。在前一种（这通常是我们需要的），它们可能是任意联接到解释器的标准输入，
无论它们是文件还是其它设备。

When a script file is used, it is sometimes useful to be able to run the script
and enter interactive mode afterwards.  This can be done by passing :option:`-i`
before the script.  (This does not work if the script is read from standard
input, for the same reason as explained in the previous paragraph.)

使用脚本文件时，经常会运行脚本然后进入交互模式。这也可以通过在脚本之前加上 :option:`-i` 
参数来实现。（如果脚本来自标准输入，就不能这样执行，与前一段提到的原因一样。）

.. _tut-argpassing:

Argument Passing 参数传递
----------------

When known to the interpreter, the script name and additional arguments
thereafter are passed to the script in the variable ``sys.argv``, which is a
list of strings.  Its length is at least one; when no script and no arguments
are given, ``sys.argv[0]`` is an empty string.  When the script name is given as
``'-'`` (meaning  standard input), ``sys.argv[0]`` is set to ``'-'``.  When
:option:`-c` *command* is used, ``sys.argv[0]`` is set to ``'-c'``.  When
:option:`-m` *module* is used, ``sys.argv[0]``  is set to the full name of the
located module.  Options found after  :option:`-c` *command* or :option:`-m`
*module* are not consumed  by the Python interpreter's option processing but
left in ``sys.argv`` for  the command or module to handle.

调用解释器时，脚本名和附加参数传入一个名为 ``sys.argv`` 的字符串列表。没有给定脚本和参数时，
它至少有一个元素：``sys.argv[0]`` ，此时它是一个空字符串，脚本名指定为 ``'-'`` （表示标准
输入）时，``sys.argv`` 。使用 :option:`-c` *命令* 时，``sys.argv[0] 被设定为 `-c` 。
使用 :option:`-m` *模块*时，``sys.argv[0]`` 被设定为指定为模块的全名。 :option:`-c` 
*command* 或 :option:`-m` 之后的参数不会被 Python 解释器的选项处理机制所截获，而是留在 
``sys.argv`` 中，供脚本命令操作。

.. _tut-interactive:

Interactive Mode 交互模式
----------------

When commands are read from a tty, the interpreter is said to be in *interactive
mode*.  In this mode it prompts for the next command with the *primary prompt*,
usually three greater-than signs (``>>>``); for continuation lines it prompts
with the *secondary prompt*, by default three dots (``...``). The interpreter
prints a welcome message stating its version number and a copyright notice
before printing the first prompt::

从 tty 读取命令时，我们称解释器工作于交互模式。这种模式下它根据主提示符来执行，主提示符通常标
识为三个大于号（``>>>``）；后续的部分被称为从属提示符，由三个点标识（``...``）。在第一行之
前，解释器打印欢迎信息，版本号和授权提示：

   $ python
   Python 3.0a1 (py3k, Sep 12 2007, 12:21:02)
   [GCC 3.4.6 20060404 (Red Hat 3.4.6-8)] on linux2
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

.. XXX update for final release of Python 3.0

Continuation lines are needed when entering a multi-line construct. As an
example, take a look at this :keyword:`if` statement::

输入多行结构时需要从属提示符了，例如，下面这个 if 语句：

   >>> the_world_is_flat = 1
   >>> if the_world_is_flat:
   ...     print("Be careful not to fall off!")
   ... 
   Be careful not to fall off!


.. _tut-interp:

The Interpreter and Its Environment 解释器及其环境
===================================


.. _tut-error:

Error Handling 错误处理
--------------

When an error occurs, the interpreter prints an error message and a stack trace.
In interactive mode, it then returns to the primary prompt; when input came from
a file, it exits with a nonzero exit status after printing the stack trace.
(Exceptions handled by an :keyword:`except` clause in a :keyword:`try` statement
are not errors in this context.)  Some errors are unconditionally fatal and
cause an exit with a nonzero exit; this applies to internal inconsistencies and
some cases of running out of memory.  All error messages are written to the
standard error stream; normal output from executed commands is written to
standard output.

有错误发生时，解释器打印一个错误信息和栈跟踪器。交互模式下，它返回主提示符，如果从文件输入执行，
它在打印栈跟踪器后以非零状态退出。（异常由 :keyword:`try` 语句的 :keyword:`except` 子
句捕获 ）。一些非常致命的错误会导致非零状态下退出，这通常由内部矛盾和内存溢出造成，所有的错误
信息都写入标准错误流；命令中执行的普通输出写入标准输出。

Typing the interrupt character (usually Control-C or DEL) to the primary or
secondary prompt cancels the input and returns to the primary prompt. [#]_
Typing an interrupt while a command is executing raises the
:exc:`KeyboardInterrupt` exception, which may be handled by a :keyword:`try`
statement.

在主提示符或从属提示符输入中断符（通常是 Control-C 或者 DEL）就会取消当前输入，回到主命令行。 
[#]_ 执行命令行时输入一个中断符会抛出一个 :exc: `KeyboardInterrupt` 异常，它可以
被 :keyword:`try` 语句截获。

.. _tut-scripts:

Executable Python Scripts 执行 Python 脚本
-------------------------

On BSD'ish Unix systems, Python scripts can be made directly executable, like
shell scripts, by putting the line ::

BSD 类的 UNIX 系统中， Python 脚本可以像 Shell 脚本那样直接执行，只要在脚本文件
开头写一行文本来指定文件和模式：


   #! /usr/bin/env python

(assuming that the interpreter is on the user's :envvar:`PATH`) at the beginning
of the script and giving the file an executable mode.  The ``#!`` must be the
first two characters of the file.  On some platforms, this first line must end
with a Unix-style line ending (``'\n'``), not a Mac OS (``'\r'``) or Windows
(``'\r\n'``) line ending.  Note that the hash, or pound, character, ``'#'``, is
used to start a comment in Python.

(要确认 Python 解释器在用户的 :envvar:`PATH` 路径中)文件前必须有 ``#!``两个字符，
在某些平台上，第一行必须以 UNIX 风格的行结束符（``'\n'``）结束，不能用 Mac 或 
Windows （``'\r'``）的行结束符。注意 ``'\r'`` 是 Python 的注释起始符。

The script can be given an executable mode, or permission, using the
:program:`chmod` command::

脚本可以通过 `chmod` 命令指定执行模式和权限。

   $ chmod +x myscript.py


Source Code Encoding 源程序编码
--------------------

By default, Python source files are treated as encoded in UTF-8.  In that
encoding, characters of most languages in the world can be used simultaneously
in string literals, identifiers and comments --- although the standard library
only uses ASCII characters for identifiers, a convention that any portable code
should follow.  To display all these characters properly, your editor must
recognize that the file is UTF-8, and it must use a font that supports all the
characters in the file.

默认情况下， Python 源码文件以 UTF-8 编码。

It is also possible to specify a different encoding for source files.  In order
to do this, put one more special comment line right after the ``#!`` line to
define the source file encoding::

也可以为源码文件指定不同的编码。为此，要在 ``#!`` 行后面指定一个特殊的注释行，以定义源码文件的编码:

   # -*- coding: encoding -*- 

With that declaration, everything in the source file will be treated as having
the encoding *encoding* instead of UTF-8.  The list of possible encodings can be
found in the Python Library Reference, in the section on :mod:`codecs`.

源码文件中的一切都会依此定义编码为 *encoding* 而非 UTF-8 。在 Python 
库参考手册的 :mod: `编码` 一节可以找到所有可用的编码。

For example, if your editor of choice does not support UTF-8 encoded files and
insists on using some other encoding, say Windows-1252, you can write::

例如，如果你使用的编辑器不支持 UTF-8 编码，但是支持另一种称为 Windows-1252 的编码，你可以在源码中写上：

   # -*- coding: cp-1252 -*-

and still use all characters in the Windows-1252 character set in the source
files.  The special encoding comment must be in the *first or second* line
within the file.

这样就可以在源码文件中使用 Windows-1252 字符集。这个附加的编码注释必须在代码文件的 *第一或第二行* 。

.. _tut-startup:

The Interactive Startup File 交互式启动文件
----------------------------

When you use Python interactively, it is frequently handy to have some standard
commands executed every time the interpreter is started.  You can do this by
setting an environment variable named :envvar:`PYTHONSTARTUP` to the name of a
file containing your start-up commands.  This is similar to the :file:`.profile`
feature of the Unix shells.

使用 Python 解释器，我们可能需要在每次启动时执行一些命令。你可以设置一个名为 :envvar:`PYTHONSTARTUP` 
的变量，指向包含启动命令的文件。这类似于 Unix Shell 的 :file:`.profile` 文件。

.. % XXX This should probably be dumped in an appendix, since most people
.. % don't use Python interactively in non-trivial ways.

.. % XXX 这大概更适合放到一个附录中，因为大多数人不会以反常的方式使用 Python 解释器。

This file is only read in interactive sessions, not when Python reads commands
from a script, and not when :file:`/dev/tty` is given as the explicit source of
commands (which otherwise behaves like an interactive session).  It is executed
in the same namespace where interactive commands are executed, so that objects
that it defines or imports can be used without qualification in the interactive
session. You can also change the prompts ``sys.ps1`` and ``sys.ps2`` in this
file.

这个文件在解释器会话期是只读的，当 Python 从脚本中解读文件或以终端 :file:`/dev/tty` 
作为外部命令源时则不会如此（尽管它们的行为很像是处在交互会话期）。它于解释器执行的命令处
在同一个命名空间，所以由它定义或引用的一切可以在解释器中不受限制的使用。你也可以在这个文
件中改变 ``sys.ps1`` and ``sys.ps2`` 指令。

If you want to read an additional start-up file from the current directory, you
can program this in the global start-up file using code like ``if
os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())``.
If you want to use the startup file in a script, you must do this explicitly
in the script::

如果你想要在当前目录中执行附加的启动文件，可以在全局启动文件中加入类似以下的代码： ``if
os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())`` 。
如果你想要在某个脚本中使用启动文件，必须要在脚本中写入这样的语句：

   import os
   filename = os.environ.get('PYTHONSTARTUP')
   if filename and os.path.isfile(filename):
       exec(open(filename).read())


.. rubric:: Footnotes

.. [#] A problem with the GNU Readline package may prevent this. 一个GNU Readline 包的问题可能会禁止这个功能。

