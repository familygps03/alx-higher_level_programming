#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted list.
 * @head: Pointer to the list.
 * @number: Number to add.
 * Return: Address of the added node, otherwise NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev_node, *current_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	prev_node = NULL;
	current_node = *head;

	while (current_node != NULL && current_node->n < number)
	{
		prev_node = current_node;
		current_node = current_node->next;
	}

	new_node->next = current_node;

	if (prev_node != NULL)
		prev_node->next = new_node;
	else
		*head = new_node;

	return (new_node);
}
