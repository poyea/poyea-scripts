#!/usr/bin/env python3

from random import choice
from string import ascii_letters, digits, printable
import sys


letters = ascii_letters + "_"
all_letters = ascii_letters + digits


def generate_appropriate_string(N: int = 32) -> str:
    """Generate a string that is appropriate for user ID.

    >>> s = generate_appropriate_string()
    >>> len(s)
    32
    """
    generated = choice(letters)
    for _ in range(0, N - 1):
        generated += choice(all_letters)
    return generated


def generate_random_string(N: int = 50000) -> str:
    """Generate a pure random string.

    >>> s = generate_random_string()
    >>> len(s)
    50000
    """
    generated = choice(all_letters)
    for _ in range(0, N - 1):
        generated += choice(printable)
    return generated


if __name__ == "__main__":
    print(generate_appropriate_string()) if len(sys.argv) == 1 else print(
        generate_random_string()
    )
