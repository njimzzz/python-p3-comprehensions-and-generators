#!/usr/bin/env python3

def return_evens(num_list):
    return_list = [num for num in num_list if num % 2 == 0 ]
    return return_list

def make_exclamation(sentence_list):
    list_return = [sentence + "!" for sentence in sentence_list]
    return list_return