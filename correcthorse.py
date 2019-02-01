#!/usr/bin/env python3

import random

filename = "20k.txt"


def main(filename):
    with open(filename) as words_file:
        words = list(set(word.strip() for word in words_file))
    while True:
        length = input("Words:")
        try:
            length = int(length)
            print(" ".join(random.choice(words) for _ in range(length)))
        except ValueError as e:
            print('Exiting...')
            return


if __name__ == "__main__":
    main(filename)
