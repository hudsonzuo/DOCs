#include <Python.h>
PyObject* fact(PyObject* py_num)
{
  PyObject *py_arg;
  PyObject *re;
  int n=PyInt_AsLong(py_num);
  printf(" int from PyObject is:%d\n",n);
  if (n <= 1) 
     return Py_BuildValue("i",1);
  else 
     py_arg=Py_BuildValue("i",n-1);
     re=fact(py_arg);
     int re_int=PyInt_AsLong(re);
     return Py_BuildValue("i",n * re_int);
} 

