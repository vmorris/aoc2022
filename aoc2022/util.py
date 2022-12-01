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
    """ Return list of lists, split on newlines """
    data = open(f).read()
    groups = data.rstrip().split("\n\n")
    return [line.rstrip().split("\n") for line in groups]


def get_input_day04(f):
    inputs = get_input_nlnl_records(f)
    numbers = list(map(int, inputs[0][0].split(",")))
    cards = inputs[1:]
    card_results = list()
    for card in cards:
        new_card = list()
        for row in card:
            new_card.append(list(map(int, row.split())))
        card_results.append(new_card)
    return [numbers, card_results]

def binary_search(data, instructions, control):
    """ day05 has a few binary search problems where the
    search direction is a specific control character.
    - `data` is a list to search
    - `instructions` is a string with control characters
    - `control` is two characters,
        indicating which direction to subdivide to continue the search
    """
    if len(control) != 2:
        raise ValueError("Invalid control set")
    if len(instructions) > 0 and not any(item in instructions for item in control):
        raise ValueError("Instruction not in control set")
    half = int(len(data) / 2)
    if len(data) == 1:
        return data[0]
    if instructions[0] == control[0]:
        # first half
        return binary_search(data[:half], instructions[1:], control)
    elif instructions[0] == control[1]:
        # last half
        return binary_search(data[half:], instructions[1:], control)


def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError(f"{x} is not in the list.")
