import itertools


def question2(a):
    """
    Find the longest palindromic substring contained in the given string

    :param a: String
    :return: Longest palindrome
    """

    # If string is empty or has one character then it is a palindrome
    if len(a) < 2:
        return a
    else:
        # Find the substrings that start and end with same character
        a_dict = {}
        for index, letter in enumerate(a):
            if letter in a_dict.keys():
                a_dict[letter].append(index)
            else:
                a_dict[letter] = [index]

        checker_list_indices = []
        palindrome_list = []

        for letter, indices in a_dict.items():
            if len(indices) > 1:
                checker_list_indices.append(
                    list(itertools.combinations(indices, 2)))

        for indices in checker_list_indices:
            indices = list(indices[0])
            input_string = a[indices[0]:indices[1] + 1]
            if palindrome_checker(input_string):
                palindrome_list.append(input_string)

        longest_palindrome = "-"
        max_length = 0
        for word in palindrome_list:
            if len(word) > max_length:
                max_length = len(word)
                longest_palindrome = word
            elif len(word) == max_length:
                longest_palindrome += ", " + word

        return longest_palindrome


def palindrome_checker(s):
    """
    Checks if the given string is a palindrome or not

    :param s: String
    :return: Boolean
    """

    if len(s) < 1:
        return True
    elif s[0] == s[-1]:
        return palindrome_checker(s[1:-1])
    else:
        return False


a = "committee"
print("Longest Palindrome for " + a + ": " + question2(a))

a = "motor"
print("Longest Palindrome for " + a + ": " + question2(a))

a = "forgeeksskeegfor"
print("Longest Palindrome for " + a + ": " + question2(a))

a = ""
print("Longest Palindrome for " + a + ": " + question2(a))

a = "a"
print("Longest Palindrome for " + a + ": " + question2(a))

a = "ab"
print("Longest Palindrome for " + a + ": " + question2(a))
