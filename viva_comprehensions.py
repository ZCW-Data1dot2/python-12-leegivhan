from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Creates a list that starts at the variable start (inclusive) and ends at the
    variable stop (exclusive). It will give you even or odd numbers, depending on
    the variable Parity.

    :param start: an int representing the start of the range
    :param stop: an int representing the end of the range
    :param parity: determines if the number is odd or even
    :return: list of integers
    """
    if parity == Parity.ODD:
        x = [value for value in range(start,stop) if value % 2 != 0]
        return x
    if parity == Parity.EVEN:
        x = [value for value in range(start,stop) if value % 2 == 0]
        return x
    # pass


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Prints key value pairs where the value is each key squared.
    Start is the beginning value, stop is the ending value and
    factorial signifies how the key will be manipulated to produce the value.


    :param start: an int representing the start of the range
    :param stop: an integer representing the end of the range
    :param strategy: determines how to manipulate the range
    :return: Dict
    """
    x = {value : strategy(value) for value in range(start, stop)}
    return x
    # pass


def gen_set(val_in: str) -> Set:
    """
    Takes a string and prints one of each lower case letter in uppercase, inside of a dictionary.

    :param val_in: Str
    :return: Set
    """
    if val_in.islower():
        a = []
        for i in val_in:
            a.append(i.upper())
        return set(a)
    elif not val_in.isupper():
        a = []
        for i in val_in:
            if i.islower():
                a.append(i.upper())
        return set(a)
    elif val_in.isupper():
        return set()
    # pass
