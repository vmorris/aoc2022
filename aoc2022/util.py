def get_input(f, type="str"):
    input = [line.rstrip() for line in open(f)]
    if type == "str":
        return input
    if type == "int":
        return [int(i) for i in input]
    if type == "split":
        return [i.split() for i in input]
    if type == "int-matrix":
        result = list()
        for line in input:
            result.append([int(i) for i in line])
        return result


def get_input_nlnl_records(f):
    """Return list of lists, split on newlines"""
    data = open(f).read()
    groups = data.rstrip().split("\n\n")
    return [line.rstrip().split("\n") for line in groups]


def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError(f"{x} is not in the list.")
