import random


def code_generation():
    # TODO: specify length of digits dynamically
    """
    generate random code with five digit
    """
    code = '{0:05}'.format(random.randint(1, 100000))
    return code
