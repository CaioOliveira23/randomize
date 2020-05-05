#!/usr/bin/env python3
import random
import string
import sys


def replace(number_id: str):
    """
    :param number_id: takes the user id
    :return: a random different id
    """
    numbers = list(number_id)
    new_lst = [repl(i) for i in numbers]
    return "".join(new_lst)


def repl(c):
    if c.islower():
        c = random.choice(string.ascii_lowercase)
    elif c.isupper():
        c = random.choice(string.ascii_uppercase)
    elif c.isdigit():
        c = random.choice(string.digits)
    return c


if __name__ == "__main__":
    replace(sys.argv[1])
