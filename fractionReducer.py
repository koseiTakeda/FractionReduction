# reduce fraction from 2 given integers representing the numerator and denominator
# return 2 integers. For example, given the values 9 and 12 would return 3 and 4
# example : reducer(-30030, 461370)


def reducer(numerator, denominator):
    """
    reduce fraction of 2 int

    :param numerator: int
    :param denominator: int
    :return: int, int
    """

    # we want to work on positive int
    numerReduced = abs(numerator)
    denomReduced = abs(denominator)

    # which one is the smallest and check if they can divide by themself
    smallestNum = denomReduced
    if denomReduced < numerReduced:
        smallestNum = numerReduced

    # divide from the smallestNum
    while smallestNum > 1:
        if not numerReduced % smallestNum and not denomReduced % smallestNum:
            numerReduced = int(numerReduced / smallestNum)
            denomReduced = int(denomReduced / smallestNum)
            smallestNum = denomReduced
            if numerReduced < denomReduced:
                smallestNum = numerReduced
        smallestNum -= 1

    if numerator < 0:
        numerReduced *= -1

    if denominator < 0:
        denomReduced *= -1

    return numerReduced, denomReduced
