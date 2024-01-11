#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  Size: %ld\n", size);
	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str ? str : "(nil)");

	printf("  first %ld bytes:", size + 1 < 10 ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; ++i)
	{

		printf(" %02hhx", str[i]);
	}
	printf("\n");
}
