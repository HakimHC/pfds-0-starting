from types import NoneType
from typing import Any
import math


EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def NULL_not_found(object: Any) -> int:
    ret = EXIT_FAILURE
    res = type(object)

    if res == float and math.isnan(object):
        print(f"nan { res }")
        return EXIT_SUCCESS

    tab = {
            float: "NaN",
            int: 0,
            str: "",
            bool: False,
            NoneType: "None"
    }

    to_print = "Type not found"
    if not object:
        to_print = f"{ tab[res] } { res }"
        ret = EXIT_SUCCESS

    print(to_print)
    return ret
