"""Comprehension examples."""


def main() -> None:
    nums = [1, 2, 3, 4, 5, 6]

    squares = [n * n for n in nums]
    even_squares = [n * n for n in nums if n % 2 == 0]
    unique_lengths = {len(word) for word in ["cat", "apple", "dog", "banana"]}
    cube_map = {n: n**3 for n in nums}
    lazy_doubles = (n * 2 for n in nums)

    print("Squares:", squares)
    print("Even squares:", even_squares)
    print("Unique word lengths:", unique_lengths)
    print("Cube map:", cube_map)
    print("First three doubles from generator:", [next(lazy_doubles) for _ in range(3)])


if __name__ == "__main__":
    main()
