# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:39:35 2021

@author: Andreas
"""

def parent(i):
    return int(i/2)





def heap_increase_key(A,i,key):
    if key < A[i]:
        print('error - new key is smaææer then current key')
    else:
        A[i] = key
        
        while (i > 1 and A[parent(i)] < A[i]):
            A[i], A[parent(i)] = A[parent(i)], A[i]
            i = parent(i)
    return A
            
    


A = [16,14,10,8,7,9,3,2,4,1]

i = 8

key = 15

print(heap_increase_key(A, i, key))
        