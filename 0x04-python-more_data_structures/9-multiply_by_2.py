#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        return {key: value * 2}
