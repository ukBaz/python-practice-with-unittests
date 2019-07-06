
def boxes_required(qty, box_capacity=6):
    """
    Calculate how many egg boxes will be required for a given quatity of eggs.
    :param qty: Number of eggs
    :param box_capacity: How many eggs will fit in a box
    :return: The number of boxes that are required
    """
    return int(qty / box_capacity) + 1
