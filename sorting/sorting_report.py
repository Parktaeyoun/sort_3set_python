#-*- coding: utf-8 -*-

'''
Created on 2016. 8. 8.

@author: enrjfenrjf
'''

import sys
import time

#default 재귀 호출이 1000번이나 정렬을 위해 10000으로 강제 변경
sys.setrecursionlimit(10000)

def bubble(ar):
    "Bubble sort"
    for i in range(len(ar)):
        sorted=True
        for j in range(len(ar)-i-1):
            if(ar[j]>ar[j+1]):
                ar[j],ar[j+1]=ar[j+1],ar[j]
                sorted=False
        if sorted:
            break
       
    #print ar

def quickSort(ar):          #This function returns the sorted list but does not change the original array like others . Uses extra array and not in place .
    "Quicksort implementation"
    if len(ar)<=1:              
        return ar
    lf,rt=[],[]
    p=ar[0]
    for j in ar:
        if j>=p:
            rt.append(j)
        else:
            lf.append(j)
    l=quickSort(lf)
    r=quickSort(rt[1:])
    c=l+[rt[0]]+r
    #for u in c:
    #    print u,
    #print
    return c

def mergesort(ar):
    "Merge sort implementation"
    if len(ar)<=1:
        return ar
    middle=len(ar)/2
    left =ar[:middle]
    right=ar[middle:]
    left=mergesort(left)
    right=mergesort(right)
    res=merge(left,right)
    #print res
    return res

def merge(left,right):
    "Merging left and right array in order"
    res=[]
    while len(left)+len(right):
        if len(left)*len(right):
            if left[0]<=right[0]:
                res.append(left[0])
                left=left[1:]
            else:
                res.append(right[0])
                right=right[1:]
        elif len(left):
            res.append(left[0])
            left=left[1:]
        elif len(right):
            res.append(right[0])
            right=right[1:]
    return res

if __name__ == '__main__':
    "Main Function"
    
    start_time = None
    end_time = None
    
    "file open"
    f = open("randomNum.txt", "r")
    
    "file read"
    lines = f.readlines()
    
    "file data to list"
    unsorted=[int(x) for x in lines]

    "bubble sort"
    start_time = time.time()
    bubble(unsorted)
    end_time = time.time()
    time_bubble = end_time - start_time
    
    "quick sort"
    start_time = time.time()
    quickSort(unsorted[:])
    end_time = time.time()
    time_quick = end_time - start_time
    
    "merge sort"
    start_time = time.time()
    res = mergesort(unsorted)
    end_time = time.time()
    time_merge = end_time - start_time
    #print res
    
    "result set"
    resultInfo = "sort\tbubble\tquick\tmerge\ntime\t%.2f(s)\t%.2f(s)\t%.2f(s)\n"%(time_bubble,time_quick,time_merge)
    
    print resultInfo
    
    "result print to file"
    f = open("resultNum.txt", "w")
    f.write(resultInfo);
    f.write("\n")
    for x in res:
        f.write(str(x)+"\n")
    f.close