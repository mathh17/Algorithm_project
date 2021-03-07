# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:58:53 2021

@author: oeste
"""
# Joachim 
# Fjerner elementet i A med laveste prioritet og returnerer det
def extract_min(A):
    return A.pop()
    
# Joachim
# Tilføjer e til A i prioritetskøen med laveste prioritet
def insert(A, e):
    A.append(e)
    
# Joachim - er det seriøst det de mener? 
# returnerer en tom prioritetskø 
def create_emptyPQ():
    return []
    
    
    
# Mathias  
def parent(i):
    int(i/2)
    
# Mathias
def left(i):
    return 2*i
    
# Mathias    
def right(i):
    return 2*i+1
    
    
# Mathias
def min_heapify(A,i):
    l = left(i)
    r = right(i)
    if(l >= len(A) and A[l] < A[i]):
        least = l
    else: least = i
    if r >= len(A) and A[r] < A[least]:
        least = r
    if least != i:
        A[i],A[least] = A[least],A[i]
        min_heapify(A,least)
    
def heap_extract_min(A):
    if len(A) < 1: 
        print("Error heap underflow")
        return -1
    min_e = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    min_heapify(A,0)
    return min_e
    
def heap_min(A):
    return A[0]
    
    
def heap_increase_Key(A,i,key):
    pass
    
    
    
    
def min_heap_insert(A,key):
    pass
    
    




