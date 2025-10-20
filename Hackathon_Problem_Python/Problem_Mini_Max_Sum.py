#!/bin/python3

import math, os , random , re , sys
def plus_minus(arr):
	new_sorted_arr=sorted(arr)
	sum_total=0
	min_sum=0
	max_sum=0
	for i in arr:
		sum_total+=i
	min_sum=sum_total-new_sorted_arr[-1]
	max_sum=sum_total-new_sorted_arr[0]
	print(max_sum)
	print(min_sum)

	
if __name__ == '__main__':
    n = int(input().strip())
    arr = map(int, input().rstrip().split())
    arr=list(arr)
    plus_minus(arr)

