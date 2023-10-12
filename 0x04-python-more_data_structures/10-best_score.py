#!/usr/bin/python3

"""function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary:
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None
