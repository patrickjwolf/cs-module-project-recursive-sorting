# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start >= target: 
  
        mid = target + (start - target) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == end: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > end: 
            return binary_search(arr, target, mid-1, end) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binary_search(arr, mid + 1, start, end) 
  
    # else: 
    #     # Element is not present in the array 
    #     return -1
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
end = 10
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, end) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")    


# # STRETCH: implement an order-agnostic binary search
# # This version of binary search should correctly find 
# # the target regardless of whether the input array is
# # sorted in ascending order or in descending order
# # You can implement this function either recursively 
# # or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here