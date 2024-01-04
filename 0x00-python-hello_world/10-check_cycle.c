#include "lists.h"

/**
 * check_cycle - checks if a linked list has a loop
 * @list: this is pointer to the head of the linked list
 *
 * Return: 1: if linked list have a loop
 *	0: if not
 **/

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	slow_ptr = fast_ptr = list;

	if (list == NULL)
		return (0);

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}
	return (0);
}
