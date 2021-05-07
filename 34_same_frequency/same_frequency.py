def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    freq1 = {}
    freq2 = {}
    new_num1 = [val for val in str(num1)]
    new_num2 = [val for val in str(num2)]
    for val in new_num1:
        if (val in freq1):
            freq1[val] += 1
        else:
            freq1[val] = 1
    for val in new_num2:
        if (val in freq2):
            freq2[val] += 1
        else:
            freq2[val] = 1
    if freq1 == freq2:
        return True
    else:
        return False
