#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list
 * @p: PyObject representing a Python list
 */

void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: PyObject representing a Python bytes object
 */

void print_python_bytes(PyObject *p);
{
	int size, i, alloc;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
		print_python_bytes(list->ob_item[i])
	}
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char size, c;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (c = 0; c < size; c++)
	{
		printf("%02hhx", bytes->ob_sval[c]);
		if (c == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
