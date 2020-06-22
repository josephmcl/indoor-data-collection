from random import choice

toks = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-0123456789'

def make_token(length=13): 
    return ''.join(choice(toks) for _ in range(length))
