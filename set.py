def findPair(arr, Sum):
    for x  in range(len(arr) - 1):
        for y in range(x + 1, len(arr)):
            if arr[x] + arr[y] == Sum:
                print(arr[x],arr[y])
                return
    print("Pair not found")
if _name_ == '_main_':
    arr = [1,2,3,4,6]
    Sum = 8
    findPair(arr,Sum)