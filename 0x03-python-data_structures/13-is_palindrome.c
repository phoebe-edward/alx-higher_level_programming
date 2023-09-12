#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer to list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int n = 0;
	int *array, *array2;
	int i, j;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		n++;
		current = current->next;
	}
	array  = malloc(sizeof(int) * n);
	if (array == NULL)
		return (0);
	current = *head;
	for (i = 0; i < n; i++)
	{
		array[i] = current->n;
		current = current->next;
	}
	array2 = malloc(sizeof(int) * n);
	if (array2 == NULL)
		return (0);
	for (j = n - 1, i = 0; j >= 0; j--, i++)
	{
		array2[i] = array[j];
	}
	for (i = 0; i < n; i++)
	{
		if (array[i] != array2[i])
			return (0);
	}
	return (1);
}
