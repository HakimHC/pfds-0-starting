import sys


def valid_args(argc: int) -> bool:
    ret = True

    try:
        assert argc == 2, "Invalid Argumets"
    except AssertionError as e:
        print(f"{ type(e).__name__ }: { str(e) }")
        ret = False
    return ret

def main():
    argc = len(sys.argv)

    if not valid_args(argc):
        return
    
    arg = sys.argv[1]
    success = True
    int_arg = 0
    try:
        int_arg = int(arg)
    except ValueError:
        success = False

    try:
        assert success, "Invalid Input"
    except AssertionError as e:
        print(f"{ type(e).__name__ }: { str(e) }")
        return

    res = "Im Odd"
    if int_arg % 2 == 0:
        res = "Im Even"
    print(res)



if __name__ == "__main__":
    main()
