#!/usr/bin/python3


def raise_exception_msg(message=""):
    if not message:
        raise NameError("")
    else:
        raise NameError(message)
