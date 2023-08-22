#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#

#import pdb
def f(n):
    result = []
    breakpoint()
    for i in range(n):
        result.append(i)
    return result

if __name__ == '__main__':
    print(f(10))