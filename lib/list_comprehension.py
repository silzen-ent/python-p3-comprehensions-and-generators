#!/usr/bin/env python3

# Using a list comprehension, write a function return_evens() that returns a list of all of the even elements of a sequence of integers.
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

print(return_evens([0, 1, 3, 5, 7, 8, 9]))



def make_exclamation(sentence_list):    
    return [sentence + '!' for sentence in sentence_list]
