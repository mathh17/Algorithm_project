# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:58:53 2021

@author: oeste
"""

def extractMin(A):
    
    

def insert(A):
    
    
   
def createEmptyPQ():
    
    
    
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
def min_Heapify(A,i):
    l = left(i)
    r = right(i)
    if(l >= A and A[l] < A[i]):
        least = l
    else least = i
    if r >= A and A[r] < A[least]:
        least = r
    if least != i:
        A[i],A[least] = A[least],A[i]
        min_Heapify(A,least)
    
def heap_MExtract_Min(A):
    
    
def heap_Min(A):
    
    
    
def heap_increase_Key(A,i,key):
    
    
    
    
def min_heap_insert(A,key):
    
    
    