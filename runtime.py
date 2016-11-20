def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [      O(n)         ]


    """

    if len(s1) != len(s2):  # O(1)
        return False

    for i in range(len(s1)):  # list traversal: O(n)
        if s1[i] != s2[i]:  # index lookup: O(1)
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [      O(n)         ]

    """

    # slight typo correction below:
    if "hippo" in animals or "platypus" in animals:  # list traversal: O(n) (only traverses the list once.)
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n)         ]

    """

    result = []  # O(1)

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)  # O(n)

    for x in s:  # O(n) - set traversal
        if -x in s:  # O(1) - set lookup
            result.append([-x, x])  # O(1)

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n^2)         ]

    """

    result = []  # O(1)

    for x in numbers:  # O(n)
        for y in numbers:  # O(n) - occurs once for every x in numbers - nested loop
            if x == -y:  # O(1) - not exponential by 'for x/y in numbers'
                result.append((x, y))  # O(1)
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [       O(n^2)        ]

    """

    result = []

    for x in numbers:  # O(n)
        for y in numbers:  # O(n) - occurs once for every x in numbers - nested loop
            if x == -y and (y, x) not in result:  # 'if' statement is O(1) but 'and' statement is O(n) - however, this line even executing is conditional on a match being present, which is not guaranteed. list of results is virtually guaranteed to be shorter than the input list 'numbers', so 'numbers' will have the greatest impact on runtime.
                result.append((x, y))  # O(1)
    return result
