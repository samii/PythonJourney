if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    maxi=0
    for i in range(len(arr)) :
            for j in range(i+1,len(arr)):
            	tmp=0
            	if (arr[i]<arr[j]):
                	tmp=arr[i]
                	arr[i]=arr[j]

                	arr[j]=tmp
    print (arr)
