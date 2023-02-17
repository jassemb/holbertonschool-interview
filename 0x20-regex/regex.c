#include "regex.h"

/**
 * regex_match - checks whether a given pattern matches a given string
 *
 * @str: string to be scanned
 * @pattern: regular expression
 * Return: 1 if the pattern matches the string, otherwise 0
 */
int regex_match(char const *str, char const *pattern)
{
    if (*str == '\0' && *pattern == '\0')
        return (1);
    if (*str == *pattern && *pattern != '*')
        return (regex_match(str + 1, pattern + 1));
    if (*pattern == '*')
    {
        if (*(pattern + 1) != '*' && *(pattern + 1) != '\0')
        {
            if (*str == '\0')
                return (0);
            return (regex_match(str + 1, pattern) || regex_match(str, pattern + 1));
        }
        return (regex_match(str, pattern + 1));
    }
    return (0);
}
