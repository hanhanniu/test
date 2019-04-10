#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import student

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("error type")
    if x>=0:
        return x
    else:
        return -x

def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

def fib(x):
    if x<=2:
        return 1
    else:
        return fib(x-1)+fib(x-2)


def normalize(name):
    return str(name[:1]).upper()+str(name[1:]).lower()

L1=['admin','LISA']
L2=list(map(normalize,L1))

from functools import reduce
def c(x,y):
    return x*y

n=reduce(c,[1,2,3,4,5])

def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-3-25')

bart=student.Student('jack',66)
bart.print_score()
