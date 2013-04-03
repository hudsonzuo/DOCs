.. _tut-brieftour:

**********************************
Brief Tour of the Standard Library 标准库概览
**********************************


.. _tut-os-interface:

Operating System Interface 操作系统接口
==========================

The :mod:`os` module provides dozens of functions for interacting with the
operating system::

:mod:`os` 模块提供了不少与操作系统相关联的函数。

   >>> import os
   >>> os.system('time 0:02')
   0
   >>> os.getcwd()      # Return the current working directory
   'C:\\Python30'
   >>> os.chdir('/server/accesslogs')

Be sure to use the ``import os`` style instead of ``from os import *``.  This
will keep :func:`os.open` from shadowing the builtin :func:`open` function which
operates much differently.

应该用 "import os" 风格而非 "from os import *"。这样可以保证随操作系统不同而有
所变化的 :func:`os.open` 不会覆盖内置函数 :func:`open`。

.. index:: builtin: help

The builtin :func:`dir` and :func:`help` functions are useful as interactive
aids for working with large modules like :mod:`os`::

在使用 :mod:`os` 这样的大型模块时内置的 :func:`dir` 和 :func:`help` 函数非常有用::

   >>> import os
   >>> dir(os)
   <returns a list of all module functions>
   >>> help(os)
   <returns an extensive manual page created from the module's docstrings>

For daily file and directory management tasks, the :mod:`shutil` module provides
a higher level interface that is easier to use::

针对日常的文件和目录管理任务，:mod:`shutil` 模块提供了一个易于使用的高级接口::

   >>> import shutil
   >>> shutil.copyfile('data.db', 'archive.db')
   >>> shutil.move('/build/executables', 'installdir')


.. _tut-file-wildcards:

File Wildcards 文件通配符
==============

The :mod:`glob` module provides a function for making file lists from directory
wildcard searches::

:mod:`glob` 模块提供了一个函数用于从目录通配符搜索中生成文件列表::

   >>> import glob
   >>> glob.glob('*.py')
   ['primes.py', 'random.py', 'quote.py']


.. _tut-command-line-arguments:

Command Line Arguments 命令行参数
======================

Common utility scripts often need to process command line arguments. These
arguments are stored in the :mod:`sys` module's *argv* attribute as a list.  For
instance the following output results from running ``python demo.py one two
three`` at the command line::

通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 :mod:`sys` 模块的 
*argv* 变量。例如在命令行中执行 "python demo.py one two three" 后可以得到
以下输出结果::

   >>> import sys
   >>> print(sys.argv)
   ['demo.py', 'one', 'two', 'three']

The :mod:`getopt` module processes *sys.argv* using the conventions of the Unix
:func:`getopt` function.  More powerful and flexible command line processing is
provided by the :mod:`optparse` module.

:mod:`getopt` 模块使用 Unix :func:`getopt` 函处理 *sys.argv*。更多的复杂命令行
处理由 :mod:`optparse` 模块提供。

.. _tut-stderr:

Error Output Redirection and Program Termination 错误输出重定向和程序终止
================================================

The :mod:`sys` module also has attributes for *stdin*, *stdout*, and *stderr*.
The latter is useful for emitting warnings and error messages to make them
visible even when *stdout* has been redirected::

sys 还有 *stdin*，*stdout* 和 *stderr* 属性，即使在 *stdout* 被重定向时，后者
也可以用于显示警告和错误信息。

   >>> sys.stderr.write('Warning, log file not found starting a new one\n')
   Warning, log file not found starting a new one

The most direct way to terminate a script is to use ``sys.exit()``.

大多脚本的定向终止都使用 "sys.exit()"。

.. _tut-string-pattern-matching:

String Pattern Matching 字符串正则匹配
=======================

The :mod:`re` module provides regular expression tools for advanced string
processing. For complex matching and manipulation, regular expressions offer
succinct, optimized solutions::

:mod:`re` 模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则
表达式提供了简洁、优化的解决方案::

   >>> import re
   >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
   ['foot', 'fell', 'fastest']
   >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
   'cat in the hat'

When only simple capabilities are needed, string methods are preferred because
they are easier to read and debug::

如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试::

   >>> 'tea for too'.replace('too', 'two')
   'tea for two'


.. _tut-mathematics:

Mathematics 数学
===========

The :mod:`math` module gives access to the underlying C library functions for
floating point math::

:mod:`math` 模块为浮点运算提供了对底层C函数库的访问::

   >>> import math
   >>> math.cos(math.pi / 4.0)
   0.70710678118654757
   >>> math.log(1024, 2)
   10.0

The :mod:`random` module provides tools for making random selections::

:mod:`random` 提供了生成随机数的工具。

   >>> import random
   >>> random.choice(['apple', 'pear', 'banana'])
   'apple'
   >>> random.sample(range(100), 10)   # sampling without replacement
   [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
   >>> random.random()    # random float
   0.17970987693706186
   >>> random.randrange(6)    # random integer chosen from range(6)
   4   

The SciPy project <http://scipy.org> has many other modules for numerical
computations.

SciPy <http://scipy.org> 项目还为数值运算提供了很多其它模块。

.. _tut-internet-access:

Internet Access 互联网访问
===============

There are a number of modules for accessing the internet and processing internet
protocols. Two of the simplest are :mod:`urllib2` for retrieving data from urls
and :mod:`smtplib` for sending mail::

有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 :mod:`urllib2` 以及用于发送电子邮件的 :mod:`smtplib`::

   >>> import urllib2
   >>> for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
   ...     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
   ...         print(line)

   <BR>Nov. 25, 09:43:32 PM EST

   >>> import smtplib
   >>> server = smtplib.SMTP('localhost')
   >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
   ... """To: jcaesar@example.org
   ... From: soothsayer@example.org
   ...
   ... Beware the Ides of March.
   ... """)
   >>> server.quit()

(Note that the second example needs a mailserver running on localhost.)

（注意第二个例子需要本地有一个在运行的邮件服务器。）

.. _tut-dates-and-times:

Dates and Times 日期和时间
===============

The :mod:`datetime` module supplies classes for manipulating dates and times in
both simple and complex ways. While date and time arithmetic is supported, the
focus of the implementation is on efficient member extraction for output
formatting and manipulation.  The module also supports objects that are timezone
aware. ::

:mod:`datetime` 模块为日期和时间处理同时提供了简单和复杂的方法。支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。该模块还支持时区处理。::

   # dates are easily constructed and formatted
   >>> from datetime import date
   >>> now = date.today()
   >>> now
   datetime.date(2003, 12, 2)
   >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
   '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

   # dates support calendar arithmetic
   >>> birthday = date(1964, 7, 31)
   >>> age = now - birthday
   >>> age.days
   14368


.. _tut-data-compression:

Data Compression 数据压缩
================

Common data archiving and compression formats are directly supported by modules
including: :mod:`zlib`, :mod:`gzip`, :mod:`bz2`, :mod:`zipfile` and
:mod:`tarfile`. ::

以下模块直接支持通用的数据打包和压缩格式：:mod:`zlib`， :mod:`gzip`， :mod:`bz`2， :mod:`zipfile`， 以及 :mod:`tarfile` 

   >>> import zlib
   >>> s = 'witch which has which witches wrist watch'
   >>> len(s)
   41
   >>> t = zlib.compress(s)
   >>> len(t)
   37
   >>> zlib.decompress(t)
   'witch which has which witches wrist watch'
   >>> zlib.crc32(s)
   226805979


.. _tut-performance-measurement:

Performance Measurement 性能度量
=======================

Some Python users develop a deep interest in knowing the relative performance of
different approaches to the same problem. Python provides a measurement tool
that answers those questions immediately.

有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。

For example, it may be tempting to use the tuple packing and unpacking feature
instead of the traditional approach to swapping arguments. The :mod:`timeit`
module quickly demonstrates a modest performance advantage::

例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多。:mod:`timeit` 证明了现代的方法更快一些。

   >>> from timeit import Timer
   >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
   0.57535828626024577
   >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
   0.54962537085770791

In contrast to :mod:`timeit`'s fine level of granularity, the :mod:`profile` and
:mod:`pstats` modules provide tools for identifying time critical sections in
larger blocks of code.

相对于 :mod:`timeit` 的细粒度，:mod:`profile` 和 :mod:`pstats` 模块提供了针对更大代码块的时间度量工具。

.. _tut-quality-control:

Quality Control 质量控制
===============

One approach for developing high quality software is to write tests for each
function as it is developed and to run those tests frequently during the
development process.

开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试。

The :mod:`doctest` module provides a tool for scanning a module and validating
tests embedded in a program's docstrings.  Test construction is as simple as
cutting-and-pasting a typical call along with its results into the docstring.
This improves the documentation by providing the user with an example and it
allows the doctest module to make sure the code remains true to the
documentation::

:mod:`doctest` 模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。通过用户提供的例子，它强
化了文档，允许 :mod:`doctest` 模块确认代码的结果是否与文档一致。

   def average(values):
       """Computes the arithmetic mean of a list of numbers.

       >>> print(average([20, 30, 70]))
       40.0
       """
       return sum(values, 0.0) / len(values)

   import doctest
   doctest.testmod()   # automatically validate the embedded tests

The :mod:`unittest` module is not as effortless as the :mod:`doctest` module,
but it allows a more comprehensive set of tests to be maintained in a separate
file::

:mod:`unittest` 模块不像 :mod:`doctest` 模块那么容易使用，不过它可以在一
个独立的文件里提供一个更全面的测试集。

   import unittest

   class TestStatisticalFunctions(unittest.TestCase):

       def test_average(self):
           self.assertEqual(average([20, 30, 70]), 40.0)
           self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
           self.assertRaises(ZeroDivisionError, average, [])
           self.assertRaises(TypeError, average, 20, 30, 70)

   unittest.main() # Calling from the command line invokes all tests


.. _tut-batteries-included:

Batteries Included 电池已备
==================

Python has a "batteries included" philosophy.  This is best seen through the
sophisticated and robust capabilities of its larger packages. For example:

Python 体现了“电池已备”哲学。Python 可以通过更大的包的来得到应付各种复杂情
况的强大能力，从这一点我们可以看出该思想的应用。例如：

* The :mod:`xmlrpclib` and :mod:`SimpleXMLRPCServer` modules make implementing
  remote procedure calls into an almost trivial task.  Despite the modules
  names, no direct knowledge or handling of XML is needed.

  :mod:`xmlrpclib` 和 :Mod:`SimpleXMLRPCServer` 模块实现了在琐碎的任务中
调用远程过程。尽管有这样的名字，其实用户不需要直接处理 XML ，也不需要这方面的知识。

* The :mod:`email` package is a library for managing email messages, including
  MIME and other RFC 2822-based message documents. Unlike :mod:`smtplib` and
  :mod:`poplib` which actually send and receive messages, the email package has
  a complete toolset for building or decoding complex message structures
  (including attachments) and for implementing internet encoding and header
  protocols.

  :mod:`email` 包是一个邮件消息管理库，可以处理 MIME 或其它基于 RFC 2822 的消息文
档。不同于实际发送和接收消息的 :mod:`smtplib` 和 :mod:`poplib` 模块，email 包有
一个用于构建或解析复杂消息结构（包括附件）以及实现互联网编码和头协议的完整工具集。

* The :mod:`xml.dom` and :mod:`xml.sax` packages provide robust support for
  parsing this popular data interchange format. Likewise, the :mod:`csv` module
  supports direct reads and writes in a common database format. Together, these
  modules and packages greatly simplify data interchange between python
  applications and other tools.

  :mod:`xml.dom` 和 :mod:`xml.sax` 包为流行的信息交换格式提供了强大的支持。同
样， :mod:`csv` 模块支持在通用数据库格式中直接读写。综合起来，这些模块和包大大简化
了 Python 应用程序和其它工具之间的数据交换。

* Internationalization is supported by a number of modules including
  :mod:`gettext`, :mod:`locale`, and the :mod:`codecs` package.

  国际化由 :mod:`gettext`， :mod:`locale`和 :mod:`codecs` 包支持


