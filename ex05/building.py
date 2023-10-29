import sys
import string


help_symbols = ["--help", "-h", "-?"]


def is_punctuation(c):
    """Determines if a character is a punctuation mark"""
    return c in string.punctuation


def cnt(s, f) -> int:
    """
    Sums the count of times when a character in 's'
    passed to the function 'f' returns true
    """
    return sum(1 for c in s if f(c))


def main():
    """
    Displays the sums of the first arguments upper-case characters, lower-case
    characters, punctuation characters, digits and spaces.
    """
    argv = sys.argv
    argc = len(argv)

    try:
        assert argc == 2, "Invalid Arguments"
    except AssertionError as e:
        print(f"{ type(e).__name__ }: { str(e) }")
        return

    if argv[1] in help_symbols:
        help()
        return

    upper = cnt(argv[1], str.isupper)
    lower = cnt(argv[1], str.islower)
    punctuation = cnt(argv[1], is_punctuation)
    spaces = cnt(argv[1], str.isspace)
    digits = cnt(argv[1], str.isdigit)

    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def help():
    """ Help function """
    print(f"{ main.__name__ }: { main.__doc__ }")
    print(f"{ cnt.__name__ }: { cnt.__doc__ }")
    print(f"{ is_punctuation.__name__ }: { is_punctuation.__doc__ }")


if __name__ == "__main__":
    main()
