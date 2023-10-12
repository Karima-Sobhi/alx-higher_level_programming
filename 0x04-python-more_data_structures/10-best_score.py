#!/usr/bin/python3

"""function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary:
        sorted_kyes = sorted(list(a_dictionary.keys()), reverse=True)
        return (sorted_kyes[0])
