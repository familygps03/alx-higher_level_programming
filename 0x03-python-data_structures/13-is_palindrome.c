#include <stdio.h>
#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct listint_s {
 *     int n;
 *     struct listint_s *next;
 * };
 * typedef struct listint_s listint_t;
 */

/**
 * reverse_list - Reverse a linked list.
 * @head: Pointer to the head of the list.
 *
 * This function reverses a linked list in-place.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL)
	{

	next = current->next;

	current->next = prev;

	prev = current;

	current = next;

	}
return (prev);
}

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
	return (1);
	}

	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
	fast = fast->next->next;
	prev_slow = slow;
	slow = slow->next;
	}
	if (fast != NULL)
	{
	slow = slow->next;
	}
	second_half = reverse_list(slow);
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
		return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
		}
		prev_slow->next = reverse_list(prev_slow->next);
		return (1);
}
