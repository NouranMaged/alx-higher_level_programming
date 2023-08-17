#!/usr/bin/python3
def best_score(a_dictionary):
    return {max(k): value for k, value in a_dictionary.items()}
