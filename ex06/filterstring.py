import sys
from ft_filter import ft_filter


def validate(n):
    try:
        int(n)
    except ValueError:
        raise AssertionError("Cannot convert to integer")


def main():
    """ Main function """
    argv = sys.argv
    argc = len(argv)

    try:
        assert argc == 3, "Invalid Arguments"
    except AssertionError as e:
        print(f"{ type(e).__name__ }: { str(e) }")
        return

    try:
        validate(argv[2])
    except AssertionError as e:
        print(f"{ type(e).__name__ }: { str(e) }")
        return

    min_len = int(argv[2])

    iter = argv[1].split(" ")
    res = ft_filter(lambda x: len(x) >= min_len, iter)
    print([i for i in res])


if __name__ == "__main__":
    # print(ft_filter.__doc__)
    # print(filter.__doc__)
    main()
