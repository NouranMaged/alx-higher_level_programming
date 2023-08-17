#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return {max(k): value for k, value in a_dictionary.items()}
