def all_thing_is_obj(object: any) -> int:
    types = [list, tuple, set, dict, str]
    res = type(object)

    if res not in types:
        res = "Type not found"
    print(res)
    return 42
