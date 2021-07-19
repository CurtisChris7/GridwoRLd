def argmax(dic: dict, values: list):
    """
    Description
    ----------
    Finds the value amongst a list of candidate values which maps to the highest value
    in a given dictionary

    Parameters
    ----------
    dic : dict
        A dictionary that maps keys of the same type as the value in values to numbers

    values : list
        The candiate list of values

    Returns
    -------
    dict
        The candidate value which maps to the highest value in the dictinary
    """
    max_ = dic[values[0]]
    val = values[0]
    for v in values:
        new_val = dic[v]
        if new_val > max_:
            max_ = new_val
            val = v
    return val


def testPolicy():
    return
