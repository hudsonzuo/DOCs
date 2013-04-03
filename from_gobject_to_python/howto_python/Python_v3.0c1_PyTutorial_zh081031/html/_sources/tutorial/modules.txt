.. _tut-modules:

*******
Modules 模块
*******

If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.  This
is known as creating a *script*.  As your program gets longer, you may want to
split it into several files for easier maintenance.  You may also want to use a
handy function that you've written in several programs without copying its
definition into each program.

如果你从Python解释器退出再进入，那么你定义的所有的方法和变量就都消失了。所以，如果你想写一个能
保存长一点的程序，你最好使用一个文本编辑器保存这些代码，把保存好的文件作为Python解释器的输入。
这就是传说中的*脚本*。当你的程序能够长时间保存了，你就更加希望把他们（按照某种形式）拆分以便于
管理。你可能还需要有个办法，在不同的程序中方便的调用，而不是把一坨代码拷来拷去。

To support this, Python has a way to put definitions in a file and use them in a
script or in an interactive instance of the interpreter. Such a file is called a
*module*; definitions from a module can be *imported* into other modules or into
the *main* module (the collection of variables that you have access to in a
script executed at the top level and in calculator mode).

为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用。这个
文件被称为*模块*，模块中的定义可以被*导入*到其他的模块或者*主*模块（*主*模块是执行脚本的最上层
或计算模式下的一组可访问变量的集合）

A module is a file containing Python definitions and statements.  The file name
is the module name with the suffix :file:`.py` appended.  Within a module, the
module's name (as a string) is available as the value of the global variable
``__name__``.  For instance, use your favorite text editor to create a file
called :file:`fibo.py` in the current directory with the following contents::

模块就是拥有 Python 定义和声明的文件。文件名就是模块名称，以 :file:`.py` 结尾。针对一个模块，
模块的名称（字符串）和这个模块提供的全局变量 ``__name__`` 是一样的。例如，用你贴心的编辑器在
当前目录创建一个叫做 :file:`fibo.py` 的文件，内容如下::

   # Fibonacci numbers module
   # 斐波那契数 模块

   def fib(n):    # write Fibonacci series up to n
       a, b = 0, 1
       while b < n:
           print(b, end=' ')
           a, b = b, a+b

   def fib2(n): # return Fibonacci series up to n
       result = []
       a, b = 0, 1
       while b < n:
           result.append(b)
           a, b = b, a+b
       return result

Now enter the Python interpreter and import this module with the following
command::

现在进入 Python 解释器，通过如下命令导入这个模块

   >>> import fibo

This does not enter the names of the functions defined in ``fibo``  directly in
the current symbol table; it only enters the module name ``fibo`` there. Using
the module name you can access the functions::

这并没有把``fibo``里面定义的方法名称直接导入符号表，他只是把 ``fibo`` 这个模块放在这了。
你可以通过模块的名称来使用这些方法::

   >>> fibo.fib(1000)
   1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
   >>> fibo.fib2(100)
   [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
   >>> fibo.__name__
   'fibo'

If you intend to use a function often you can assign it to a local name::

你也可以用一个本地的名字来存放某个方法，这样用起来会比较方便。

   >>> fib = fibo.fib
   >>> fib(500)
   1 1 2 3 5 8 13 21 34 55 89 144 233 377


.. _tut-moremodules:

More on Modules 深入模块
===============



A module can contain executable statements as well as function definitions.
These statements are intended to initialize the module. They are executed only
the *first* time the module is imported somewhere. [#]_

模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在*第一
次*被导入时才会被执行。 [#]_

Each module has its own private symbol table, which is used as the global symbol
table by all functions defined in the module. Thus, the author of a module can
use global variables in the module without worrying about accidental clashes
with a user's global variables. On the other hand, if you know what you are
doing you can touch a module's global variables with the same notation used to
refer to its functions, ``modname.itemname``.

每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用。所以，模块的作者可以放心大
胆的在模块内部使用这些全局变量，而不用担心把其他用户的全局变量搞花。从另一个方面，当你确实知道你在
做什么的话，你也可以通过``modname.itemname``这样的表示法来访问模块内的函数。

Modules can import other modules.  It is customary but not required to place all
:keyword:`import` statements at the beginning of a module (or script, for that
matter).  The imported module names are placed in the importing module's global
symbol table.

模块是可以导入其他模块的。在一个模块（或者脚本，或者其他地方）的最前面使用 :keyword:`import` 
来导入一个模块，当然这只是一个惯例，而不是强制的。被导入的模块的名称将被放入当前操作的模块的符号表中。

There is a variant of the :keyword:`import` statement that imports names from a
module directly into the importing module's symbol table.  For example::

还有一种导入的方法，可以使用:keyword:`import`直接把模块内（函数，变量的）名称导入到当前操
作模块。比如::

   >>> from fibo import fib, fib2
   >>> fib(500)
   1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the
local symbol table (so in the example, ``fibo`` is not defined).

这种导入的方法不会把被导入的模块的名称放在当前的字符表中（所以在这个例子里面，``fibo``这个名称
是没有定义的）。

There is even a variant to import all names that a module defines::

这还有一种方法，可以一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表::

   >>> from fibo import *
   >>> fib(500)
   1 1 2 3 5 8 13 21 34 55 89 144 233 377

This imports all names except those beginning with an underscore (``_``).
In most cases Python programmers do not use this facility since it introduces 
an unknown set of names into the interpreter, possibly hiding some things 
you have already defined.

这将把所有的名字都导入进来，但是那些由单一下划线（``_``）开头的名字不在此例。大多数情况，
Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。


.. _tut-modulesasscripts:

Executing modules as scripts 像脚本一样运行模块
----------------------------


When you run a Python module with ::

使用下面的命令运行一个 Python 模块::

   python fibo.py <arguments>

the code in the module will be executed, just as if you imported it, but with
the ``__name__`` set to ``"__main__"``.  That means that by adding this code at
the end of your module::

如果你的模块里面的代码就会执行，就好像你导入他们一样，``__name__`` 会赋值为 
``"__main__"``。也就是说，你在模块的最下面加上如下代码::

   if __name__ == "__main__":
       import sys
       fib(int(sys.argv[1]))

you can make the file usable as a script as well as an importable module,
because the code that parses the command line only runs if the module is
executed as the "main" file::

这个文件可以当作一个脚本来使用。而这部分代码只有在这个模块被当作"主"程序执行时才会被执行::

   $ python fibo.py 50
   1 1 2 3 5 8 13 21 34

If the module is imported, the code is not run::

如果这个模块是被导入的，那么这些代码是不被执行的::

   >>> import fibo
   >>>

This is often used either to provide a convenient user interface to a module, or
for testing purposes (running the module as a script executes a test suite).

模块经常通过这种写法来提供一些方便的接口，或者用来测试（直接运行脚本，会执行一个/组测试用例）。


.. _tut-searchpath:

The Module Search Path 模块的搜索路径
--------------

.. index:: triple: module; search; path

When a module named :mod:`spam` is imported, the interpreter searches for a file
named :file:`spam.py` in the current directory, and then in the list of
directories specified by the environment variable :envvar:`PYTHONPATH`.  This
has the same syntax as the shell variable :envvar:`PATH`, that is, a list of
directory names.  When :envvar:`PYTHONPATH` is not set, or when the file is not
found there, the search continues in an installation-dependent default path; on
Unix, this is usually :file:`.:/usr/local/lib/python`.

当试图导入一个叫做 :mod:`spam` 的模块，解释器会首先在当前目录搜索一个叫做 :file:`spam.py` 
的文件，然后会依次寻找定义在环境变量 :envvar:`PYTHONPATH` 中的所有目录。定义
:envvar:`PYTHONPATH`的语法和定义环境变量:envvar:`PATH`一样，都是一系列目录的列表。如果
:envvar:`PYTHONPATH`没有定义，或者按照上面的路径没有找到这个文件，那么解释器会继续在Python
安装时定义的默认目录来寻找。在Unix中，通常都是在:file:`.:/usr/local/lib/python`。

Actually, modules are searched in the list of directories given by the variable
``sys.path`` which is initialized from the directory containing the input script
(or the current directory), :envvar:`PYTHONPATH` and the installation- dependent
default.  This allows Python programs that know what they're doing to modify or
replace the module search path.  Note that because the directory containing the
script being run is on the search path, it is important that the script not have
the same name as a standard module, or Python will attempt to load the script as
a module when that module is imported. This will generally be an error.  See
section :ref:`tut-standardmodules` for more information.

实际上，这些模块都是在变量 ``sys.path`` 定义的目录里寻找。``sys.path`` 包含了输入脚本的目录
（或者说当前目录），:envvar:`PYTHONPATH` 和安装时候的默认目录。Python 程序员可以去修改这个
搜索路径。注意，因为被执行的脚本所在的目录也在模块的搜索路径中，那么被执行的脚本的名字一定要和标
准的模块名称区别开来。这非常重要，否则当要导入标准模块的时候，Python 会试图导入这个脚本。这会导
致错误的发生。请参阅 :ref:`tut-standardmodules` 章节获取更多信息。

.. %
    Do we need stuff on zip files etc. ? DUBOIS
	我们是不是考虑一下从zip抑或其他文件里面导入模块？

"Compiled" Python files “编译的”Python文件
------------------

As an important speed-up of the start-up time for short programs that use a lot
of standard modules, if a file called :file:`spam.pyc` exists in the directory
where :file:`spam.py` is found, this is assumed to contain an
already-"byte-compiled" version of the module :mod:`spam`. The modification time
of the version of :file:`spam.py` used to create :file:`spam.pyc` is recorded in
:file:`spam.pyc`, and the :file:`.pyc` file is ignored if these don't match.

在一个名为 :file:`spam.py` 的文件启动时候，Python 会在同一个目录寻找一个叫 :file:`spam.pyc` 
的文件并且运行，这是一个重要的启动提速方式，尤其是你使用了大量的标准组件。 :file:`spam.pyc` 是
模块 :mod:`spam` 的“字节编译”的版本。文件 :file:`spam.py` 的修改时间将被记录在 
:file:`spam.pyc` 当中，如果当前的修改时间和记录的时间不一致，那么 :file:`spam.pyc` 
就会被忽略掉。

Normally, you don't need to do anything to create the :file:`spam.pyc` file.
Whenever :file:`spam.py` is successfully compiled, an attempt is made to write
the compiled version to :file:`spam.pyc`.  It is not an error if this attempt
fails; if for any reason the file is not written completely, the resulting
:file:`spam.pyc` file will be recognized as invalid and thus ignored later.  The
contents of the :file:`spam.pyc` file are platform independent, so a Python
module directory can be shared by machines of different architectures.

通常你不用操心如何去创建 :file:`spam.pyc`。每次 :file:`spam.py` 成功的编译之后，这个编译好
的内容便写入 :file:`spam.pyc` 。这不会有任何的问题，如果在生成 :file:`spam.pyc`时候发生了
任何的错误，那么这个文件将会被识别为不可用的，并接会被忽略。:file:`spam.pyc` 的内容是操作系
统无关的，所以 Python 的模块目录可以在不同的体系架构中共享。

Some tips for experts:

专家提醒：

* When the Python interpreter is invoked with the :option:`-O` flag, optimized
  code is generated and stored in :file:`.pyo` files.  The optimizer currently
  doesn't help much; it only removes :keyword:`assert` statements.  When
  :option:`-O` is used, *all* :term:`bytecode` is optimized; ``.pyc`` files are
  ignored and ``.py`` files are compiled to optimized bytecode.
  
* 当采用 :option:`-O` 参数来启动 Python 的解析器时，Python 会生成优化的代码，并且存入 
:file:`.pyo`文件中。当前的优化器只能去掉采用:keyword:`assert`标记的语句，除此之外就没
什么用了。当:option:`-O`参数启用，*所有*:term:`字节码`都会被优化，忽略``.pyc``文件，
并且所有的``.py``文件都被优化成为字节码。

* Passing two :option:`-O` flags to the Python interpreter (:option:`-OO`) will
  cause the bytecode compiler to perform optimizations that could in some rare
  cases result in malfunctioning programs.  Currently only ``__doc__`` strings are
  removed from the bytecode, resulting in more compact :file:`.pyo` files.  Since
  some programs may rely on having these available, you should only use this
  option if you know what you're doing.
  
* Python解析器使用两个 :option:`-O` 参数（:option:`-OO`）将采用字节码编译以便提高性能，不
过在一些罕见的情况下会导致程序执行异常。暂时这个工作只会把字节码中的 ```__doc__`` 字符串去掉，
字节码也会更加紧凑，然后存到 :file:`.pyo` 文件中。虽然很多的程序都相信这些优化工作，但是还是
建议你在做之前，确认一下自己是在干什么。

* A program doesn't run any faster when it is read from a :file:`.pyc` or
  :file:`.pyo` file than when it is read from a :file:`.py` file; the only thing
  that's faster about :file:`.pyc` or :file:`.pyo` files is the speed with which
  they are loaded.
  
* 程序并不会因为读取 :file:`.pyc` 或者 :file:`.pyo` 文件而比 :file:`.py` 文件运行的更快。
唯一会提升的只是他们加载的速度。

* When a script is run by giving its name on the command line, the bytecode for
  the script is never written to a :file:`.pyc` or :file:`.pyo` file.  Thus, the
  startup time of a script may be reduced by moving most of its code to a module
  and having a small bootstrap script that imports that module.  It is also
  possible to name a :file:`.pyc` or :file:`.pyo` file directly on the command
  line.
  
* 在命令行中直接运行的脚本文件不会把编译的字节码写入 :file:`.pyc` 或 :file:`.pyo` 中。所以，
你应该把大部分的代码转移到你的模块当中，用一个短小的启动脚本来导入它们。或者把这个脚本的 
:file:`.pyc` 或 :file:`.pyo` 文件直接放在要执行的目录中也可以。

* It is possible to have a file called :file:`spam.pyc` (or :file:`spam.pyo`
  when :option:`-O` is used) without a file :file:`spam.py` for the same module.
  This can be used to distribute a library of Python code in a form that is
  moderately hard to reverse engineer.

* 你还可以在提供一个模块的时候只提供类似 :file:`spam.pyc` （或者通过 :option:`-O` 生成的 
:file:`spam.pyo` ）文件，而没有 :file:`spam.py` 。这主要是为了把你的 Python 文件当作库
文件来发布，目的嘛，还不是为了让那些反向工程者多费一些脑细胞。

  .. index:: module: compileall

* The module :mod:`compileall` can create :file:`.pyc` files (or :file:`.pyo`
  files when :option:`-O` is used) for all modules in a directory.
  
* 这个叫做 :mod:`compileall` 的组件可以帮助你把一个目录中的所有模块都编译成为 
:file:`.pyc` （或者用 :option:`-O` 来生成 :file:`.pyo` ）

* If using Python in a parallel processing system with a shared file system,
  you need to patch Python to disable the creation of the compiled files 
  because otherwise the multiple Python interpreters will encounter race 
  conditions in creating them.
  
* 如果你的 Python 程序存放在一个共享的文件系统，供并行处理的系统使用，那么你应该告诉 Python 
不要创建编译的字节码文件。因为这会让多个 Python 解析器在创建文件时候发生资源竞争。


.. _tut-standardmodules:

Standard Modules    标准组件
================

.. index:: module: sys

Python comes with a library of standard modules, described in a separate
document, the Python Library Reference ("Library Reference" hereafter).  Some
modules are built into the interpreter; these provide access to operations that
are not part of the core of the language but are nevertheless built in, either
for efficiency or to provide access to operating system primitives such as
system calls.  The set of such modules is a configuration option which also
depends on the underlying platform For example, the :mod:`winreg` module is only
provided on Windows systems. One particular module deserves some attention:
:mod:`sys`, which is built into every Python interpreter.  The variables
``sys.ps1`` and ``sys.ps2`` define the strings used as primary and secondary
prompts:

Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的“库参考文档”）。
有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统
级调用也没问题。这些组件会根据不同的操作系统进行不同形式的配置，比如 :mod:`winreg` 这个模块就
只会提供给 Windows 系统。应该注意到这有一个特别的模块 :mod:`sys` ，它内置在每一个 Python 
解析器中。变量 ``sys.ps1`` 和 ``sys.ps2`` 定义了主提示符和副提示符所对应的字符串:

.. % 

::

   >>> import sys
   >>> sys.ps1
   '>>> '
   >>> sys.ps2
   '... '
   >>> sys.ps1 = 'C> '
   C> print('Yuck!')
   Yuck!
   C>


These two variables are only defined if the interpreter is in interactive mode.

只有在交互式模式中，这两个变量才有定义。

The variable ``sys.path`` is a list of strings that determines the interpreter's
search path for modules. It is initialized to a default path taken from the
environment variable :envvar:`PYTHONPATH`, or from a built-in default if
:envvar:`PYTHONPATH` is not set.  You can modify it using standard list
operations::

我们说过，解释器从 ``sys.path`` 搜索模块，``sys.path`` 是一个存放着所有路径的字符串列表。
如果定义了环境变量 :envvar:`PYTHONPATH` ，那么从这里构建 ``sys.path`` ，否则使用一个内
置的默认值。你可以使用标准用的列表操作来改变这个列表。

   >>> import sys
   >>> sys.path.append('/ufs/guido/lib/python')


.. _tut-dir:

The :func:`dir` Function    :func:`dir` 函数
========================

The built-in function :func:`dir` is used to find out which names a module
defines.  It returns a sorted list of strings::

内置的函数 :func:`dir` 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

   >>> import fibo, sys
   >>> dir(fibo)
   ['__name__', 'fib', 'fib2']
   >>> dir(sys)
   ['__displayhook__', '__doc__', '__excepthook__', '__name__', '__stderr__',
    '__stdin__', '__stdout__', '_getframe', 'api_version', 'argv', 
    'builtin_module_names', 'byteorder', 'callstats', 'copyright',
    'displayhook', 'exc_info', 'excepthook',
    'exec_prefix', 'executable', 'exit', 'getdefaultencoding', 'getdlopenflags',
    'getrecursionlimit', 'getrefcount', 'hexversion', 'maxint', 'maxunicode',
    'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache',
    'platform', 'prefix', 'ps1', 'ps2', 'setcheckinterval', 'setdlopenflags',
    'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout',
    'version', 'version_info', 'warnoptions']

Without arguments, :func:`dir` lists the names you have defined currently::

如果没有给定参数，那么 :func:`dir` 函数会罗列出当前定义的所有名称::

   >>> a = [1, 2, 3, 4, 5]
   >>> import fibo
   >>> fib = fibo.fib
   >>> dir()
   ['__builtins__', '__doc__', '__file__', '__name__', 'a', 'fib', 'fibo', 'sys']

Note that it lists all types of names: variables, modules, functions, etc.

注意，它会把所有的名称都列出来: 变量，模块，函数等等。

.. index:: module: builtins

:func:`dir` does not list the names of built-in functions and variables.  If you
want a list of those, they are defined in the standard module
:mod:`builtins`::

:func:`dir` 函数并不会列出内置的函数和变量的名称，如果你坚持你想得到它们，那么你去问一个叫做 
:mod:`builtins` 的标准模块好了::

   >>> import builtins
   >>> dir(builtins)

   ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'Buffer
   Error', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Excep   
   tion', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError   
   ', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError',   
    'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImp   
   lemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecatio   
   nWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StopIteration',   
   'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True',   
    'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', '   
   UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueE   
   rror', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__'   
   , '__import__', '__name__', 'abs', 'all', 'any', 'basestring', 'bin', 'bool', 'b   
   uffer', 'bytes', 'chr', 'chr8', 'classmethod', 'cmp', 'compile', 'complex', 'cop   
   yright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'ex   
   ec', 'exit', 'filter', 'float', 'frozenset', 'getattr', 'globals', 'hasattr', 'h   
   ash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', '   
   len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'o   
   bject', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr   
   ', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'st   
   r', 'str8', 'sum', 'super', 'trunc', 'tuple', 'type', 'vars', 'zip']   

.. _tut-packages:

Packages    包
========

Packages are a way of structuring Python's module namespace by using "dotted
module names".  For example, the module name :mod:`A.B` designates a submodule
named ``B`` in a package named ``A``.  Just like the use of modules saves the
authors of different modules from having to worry about each other's global
variable names, the use of dotted module names saves the authors of multi-module
packages like NumPy or the Python Imaging Library from having to worry about
each other's module names.

包是一种管理 Python 模块命名空间的形式，采用“点模块名称”。比如一个模块的名称是 :mod:`A.B`，
那么他表示一个包 ``A`` 中的子模块 ``B`` 。就好像使用模块的时候，你不用担心不同模块之间的全局
变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。这样不同的作者都可
以提供 NumPy 模块，或者是 Python 图形库。

Suppose you want to design a collection of modules (a "package") for the uniform
handling of sound files and sound data.  There are many different sound file
formats (usually recognized by their extension, for example: :file:`.wav`,
:file:`.aiff`, :file:`.au`), so you may need to create and maintain a growing
collection of modules for the conversion between the various file formats.
There are also many different operations you might want to perform on sound data
(such as mixing, adding echo, applying an equalizer function, creating an
artificial stereo effect), so in addition you will be writing a never-ending
stream of modules to perform these operations.  Here's a possible structure for
your package (expressed in terms of a hierarchical filesystem)::

不妨假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个“包”）。现存很多种不同的音频文件
格式（基本上都是通过后缀名区分的，例如： :file:`.wav`，:file:`.aiff`，:file:`.au`，），所
以你需要有一组不断增加的模块，用来在不同的格式之间转换。并且针对这些音频数据，还有很多不同的操作
（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所你还需要一组怎么也写不完的模块来处
理这些操作。这里给出了一种可能的包结构（在分层的文件系统中）::



   sound/                          Top-level package                         最顶层包
         __init__.py               Initialize the sound package              包声明和加载文件
         formats/                  Subpackage for file format conversions    文件格式相关的子包
                 __init__.py
                 wavread.py
                 wavwrite.py
                 aiffread.py
                 aiffwrite.py
                 auread.py
                 auwrite.py
                 ...
         effects/                  Subpackage for sound effects              音效相关的子包
                 __init__.py
                 echo.py
                 surround.py
                 reverse.py
                 ...
         filters/                  Subpackage for filters                    滤镜相关的子包
                 __init__.py
                 equalizer.py
                 vocoder.py
                 karaoke.py
                 ...

When importing the package, Python searches through the directories on
``sys.path`` looking for the package subdirectory.

在导入一个包的时候，Python 会根据 ``sys.path`` 中的目录来寻找这个包中包含的子目录。

The :file:`__init__.py` files are required to make Python treat the directories
as containing packages; this is done to prevent directories with a common name,
such as ``string``, from unintentionally hiding valid modules that occur later
on the module search path. In the simplest case, :file:`__init__.py` can just be
an empty file, but it can also execute initialization code for the package or
set the ``__all__`` variable, described later.

目录只有包含一个叫做 :file:`__init__.py` 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字
（比如叫做``string``）不小心的影响搜索路径中的有效模块。最简单的情况，放一个空的
:file:`__init__.py`就可以了。当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的）
``__all__``变量赋值。

Users of the package can import individual modules from the package, for
example::

用户可以每次只导入一个包里面的特定模块，比如::

   import sound.effects.echo

This loads the submodule :mod:`sound.effects.echo`.  It must be referenced with
its full name. ::

这将会导入子模块:mod:`song.effects.echo`。 他必须使用全名去访问。::

   sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

An alternative way of importing the submodule is::

还有一种导入子模块的方法是::

   from sound.effects import echo

This also loads the submodule :mod:`echo`, and makes it available without its
package prefix, so it can be used as follows::

这同样会导入子模块:mod:`echo`，并且他不需要那些冗长的前缀，所以他可以这样使用::

   echo.echofilter(input, output, delay=0.7, atten=4)

Yet another variation is to import the desired function or variable directly::

还有一种变化就是直接导入一个函数或者变量::

   from sound.effects.echo import echofilter

Again, this loads the submodule :mod:`echo`, but this makes its function
:func:`echofilter` directly available::

同样的，这种方法会导入子模块:mod:`echo`，并且可以直接使用他的:func:`echofilter`函数::

   echofilter(input, output, delay=0.7, atten=4)

Note that when using ``from package import item``, the item can be either a
submodule (or subpackage) of the package, or some  other name defined in the
package, like a function, class or variable.  The ``import`` statement first
tests whether the item is defined in the package; if not, it assumes it is a
module and attempts to load it.  If it fails to find it, an :exc:`ImportError`
exception is raised.

注意当使用``from package import item``这种形式的时候，对应的item既可以是包里面的子模块
（子包），或者包里面定义的其他名称，比如函数，类或者变量。``import``语法会首先把item当作一
个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:`ImportError`
异常被抛出了。

Contrarily, when using syntax like ``import item.subitem.subsubitem``, each item
except for the last must be a package; the last item can be a module or a
package but can't be a class or function or variable defined in the previous
item.

反之，如果使用形如``import item.subitem.subsubitem``这种导入形式，除了最后一项，都必须
是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。


.. _tut-pkg-import-star:

Importing \* From a Package    导入一个包中的\*
---------------------------

.. index:: single: __all__

Now what happens when the user writes ``from sound.effects import *``?  Ideally,
one would hope that this somehow goes out to the filesystem, finds which
submodules are present in the package, and imports them all.  Unfortunately,
this operation does not work very well on Windows platforms, where the
filesystem does not always have accurate information about the case of a
filename!  On these platforms, there is no guaranteed way to know whether a file
:file:`ECHO.PY` should be imported as a module :mod:`echo`, :mod:`Echo` or
:mod:`ECHO`.  (For example, Windows 95 has the annoying practice of showing all
file names with a capitalized first letter.)  The DOS 8+3 filename restriction
adds another interesting problem for long module names.

设想一下，如果我们使用``from sound.effects import *``会发生什么？ 只是想想嘛。Python
会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。但是很不幸，这个方法在
Windows平台上工作的就不是非常好，因为Windows是一个大小写不区分的系统。在这类平台上，没有人敢
担保一个叫做 :file:`ECHO.py` 的文件导入为模块:mod:`echo`还是:mod:`Echo`甚至:mod:`ECHO`。
（例如，Windows 95就很讨厌的把每一个文件的首字母大写显示。）而且 DOS 的 8+3 命名规则对长模
块名称的处理会把问题搞得更纠结。

.. % The \code{__all__} Attribute

The only solution is for the package author to provide an explicit index of the
package.  The import statement uses the following convention: if a package's
:file:`__init__.py` code defines a list named ``__all__``, it is taken to be the
list of module names that should be imported when ``from package import *`` is
encountered.  It is up to the package author to keep this list up-to-date when a
new version of the package is released.  Package authors may also decide not to
support it, if they don't see a use for importing \* from their package.  For
example, the file :file:`sounds/effects/__init__.py` could contain the following
code::

为了解决这个问题，只能烦劳包作者提供一个精确的包的索引了。导入语句遵循如下规则：如果包定义文件 
:file:`__init__.py` 存在一个叫做 ``__all__`` 的列表变量，那么在使用 ``from package 
import *`` 的时候就把这个列表中的所有名字作为包内容导入。作为包的作者，可别忘了在更新包之后
保证 ``__all__`` 也更新了啊。你说我就不这么做，我就不使用导入*这种用法，好吧，没问题，谁让
你是老板呢。这里有一个例子，在:file:`sounds/effects/__init__.py`中包含如下代码::

   __all__ = ["echo", "surround", "reverse"]

This would mean that ``from sound.effects import *`` would import the three
named submodules of the :mod:`sound` package.

这表示当你使用``from sound.effects import *``这种用法时，你只会导入包里面这三个子模块。

If ``__all__`` is not defined, the statement ``from sound.effects import *``
does *not* import all submodules from the package :mod:`sound.effects` into the
current namespace; it only ensures that the package :mod:`sound.effects` has
been imported (possibly running any initialization code in :file:`__init__.py`)
and then imports whatever names are defined in the package.  This includes any
names defined (and submodules explicitly loaded) by :file:`__init__.py`.  It
also includes any submodules of the package that were explicitly loaded by
previous import statements.  Consider this code::

如果``__all__``真的而没有定义，那么使用``from sound.effects import *``这种语法的时候，
就*不会*导入包:mod:`sound.effects`里的任何子模块。他只是把包:mod:`sound.effects`和它
里面定义的所有内容导入进来（可能运行:file:`__init__.py`里定义的初始化代码）。这会把
:file:`__init__.py`里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有
明确指定的模块。看下这部分代码::

   import sound.effects.echo
   import sound.effects.surround
   from sound.effects import *

In this example, the echo and surround modules are imported in the current
namespace because they are defined in the :mod:`sound.effects` package when the
``from...import`` statement is executed.  (This also works when ``__all__`` is
defined.)

这个例子中，在执行``from...import``前，包:mod:`sound.effects`中的echo和surround模
块都被导入到当前的命名空间中了。（当然如果定义了``__all__``就更没问题了。）

Note that in general the practice of importing ``*`` from a module or package is
frowned upon, since it often causes poorly readable code. However, it is okay to
use it to save typing in interactive sessions, and certain modules are designed
to export only names that follow certain patterns.

通常我们并不主张使用``*``这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。不过
这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。

Remember, there is nothing wrong with using ``from Package import
specific_submodule``!  In fact, this is the recommended notation unless the
importing module needs to use submodules with the same name from different
packages.

记住，使用``from Package import specific_submodule``这种方法永远不会有错。事实上，
这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。


Intra-package References    包内引用
------------------------

The submodules often need to refer to each other.  For example, the
:mod:`surround` module might use the :mod:`echo` module.  In fact, such
references are so common that the :keyword:`import` statement first looks in the
containing package before looking in the standard module search path. Thus, the
:mod:`surround` module can simply use ``import echo`` or ``from echo import
echofilter``.  If the imported module is not found in the current package (the
package of which the current module is a submodule), the :keyword:`import`
statement looks for a top-level module with the given name.

子模块经常会相互引用，比如:mod:`surround`模块可能会用到:mod:`echo`模块。实际上，这
种引用是最常见的，而:keyword:`module`语句会首先查找同目录下是否有期望的模块，如果没
有再按照标准的模块搜索方式进行。所以在:mod:`surround`模块内部可以简单的使用``import 
echo``或者``from echo import echofilter``。如果在当前包（就是把本模块当成子模块
的那个包）中没有找到期望的模块，那么:keyword:`import`会从最顶端开始寻找。

When packages are structured into subpackages (as with the :mod:`sound` package
in the example), you can use absolute imports to refer to submodules of siblings
packages.  For example, if the module :mod:`sound.filters.vocoder` needs to use
the :mod:`echo` module in the :mod:`sound.effects` package, it can use ``from
sound.effects import echo``.

如果在结构中包是一个子包（比如这个例子中对于包:mod:`sound`来说），而你又想导入兄弟包
（同级别的包）你就得使用导入绝对的路径来导入。比如，如果模块:mod:`sound.filters.vocoder`
要使用包:mod:`sound.effects`中的模块:mod:`echo`，你就要写成
``from sound.effects import echo``。

Starting with Python 2.5, in addition to the implicit relative imports described
above, you can write explicit relative imports with the ``from module import
name`` form of import statement. These explicit relative imports use leading
dots to indicate the current and parent packages involved in the relative
import. From the :mod:`surround` module for example, you might use::

从 Python2.5 开始，上述的那种隐含的相对路径中的导入，可以被显式的相对路径来导入，
使用``from module import name``的方法。这种显式的相对路径导入使用一个点来表示
当前模块所属的包。我们以:mod:`surround`模块的位置为例，你可以使用::

   from . import echo
   from .. import formats
   from ..filters import equalizer

Note that both explicit and implicit relative imports are based on the name of
the current module. Since the name of the main module is always ``"__main__"``,
modules intended for use as the main module of a Python application should
always use absolute imports.

无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是``"__main__"``，
一个Python应用程序的主模块，应当总是使用绝对路径引用。


Packages in Multiple Directories    跨目录的包
--------------------------------

Packages support one more special attribute, :attr:`__path__`.  This is
initialized to be a list containing the name of the directory holding the
package's :file:`__init__.py` before the code in that file is executed.  This
variable can be modified; doing so affects future searches for modules and
subpackages contained in the package.

包还提供一个额外的属性，:attr:`__path__`。这是一个目录列表，里面每一个包含的目录
都有为这个包服务的:file:`__init__.py`，你得在其他:file:`__init__.py`被执行
前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。

While this feature is not often needed, it can be used to extend the set of
modules found in a package.

这个功能并不常用，一般用来扩展包里面的模块。


.. rubric:: Footnotes

.. [#] In fact function definitions are also 'statements' that are 'executed'; the
   execution enters the function name in the module's global symbol table.

.. [#] 事实上函数的定义也是一种“可执行的声明”，执行时候从模块的全局符号表来寻找函数的名称。
