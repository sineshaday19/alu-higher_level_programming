#!/usr/bin/python3


def raise_exception_msg(message="write anything"):
    if not message:
        raise NameError("Empty message is not allowed.")
    else:
        raise NameError(message)
