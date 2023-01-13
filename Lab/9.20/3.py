a = [2,2,2,2,2,2,1,2,2,2,2,2,2,2,2]
def Sum(arr,start,end):
    i = start
    s = 0
    while(i <= end):
        s += arr[i]
        i += 1 
    return s / (end-start+1)  
def Bijiao(arr,start,end):
    mid = (start + end) // 2
    if start < end:
        if Sum(arr,start,mid) < Sum(arr,mid+1,end):
            Bijiao(arr,start,mid)
        else:
            Bijiao(arr,mid+1,end)
    elif start == end:
        print(start)

Bijiao(a,0,14)