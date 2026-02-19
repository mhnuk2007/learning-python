"""Quick tour of random, itertools, and functools."""

import functools
import itertools
import random


def main() -> None:
    random.seed(7)

    names = ["Asha", "Ben", "Chloe", "Dina"]
    print("Random choice:", random.choice(names))

    print("Pair combinations:", list(itertools.combinations(names, 2)))

    numbers = [1, 2, 3, 4]
    total = functools.reduce(lambda acc, n: acc + n, numbers, 0)
    print("Reduced sum:", total)


if __name__ == "__main__":
    main()
