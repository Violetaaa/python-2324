#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_lengths(a):
    sum = np.sum(a**2, axis=1)
    return np.sqrt(sum)

def main():
    a=np.random.randn(2, 5)
    v=vector_lengths(a)
    correct=scipy.linalg.norm(a, 2, axis=1)
    print(v)
    print(correct)

if __name__ == "__main__":
    main()
