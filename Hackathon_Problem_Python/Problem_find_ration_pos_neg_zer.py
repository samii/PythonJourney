#!/bin/python3

import math, os , random , re , sys
def plus_minus(arr):
	print('again')
	print(arr)
	total=len(arr)
	n_pos=0
	n_neg=0
	n_zero=0
	for i in arr:
		if (i>0):
			n_pos+=1
		elif (i<0):
			n_neg+=1
		else: 
			n_zero+=1
	
	ratio_pos = round(n_pos / total,6)
	ratio_neg = round(n_neg / total,6)
	ratio_zero = round(n_zero / total,6)
	print(ratio_pos)
	print(ratio_neg)
	print(ratio_zero)

	
if __name__ == '__main__':
    n = int(input().strip())
    arr = map(int, input().rstrip().split())
    arr=list(arr)
    print (arr)
    total=len(arr)
    print(total)
    plus_minus(arr)

