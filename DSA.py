# reverse array problem
# def reverseArray(A,start,end):
#     while start < end:
#         A[start],A[end] = A[end], A[start]
#         start += 1
#         end -= 1

# arr = [1,2,3,4,5,6]
# print(arr)
# reverseArray(arr,0,5)
# print("Reversed array list is", arr)


#find min or max number in array
# def getMin(arr, n):
#     res = arr[0]
#     for i in range(1, n):
#         res = min(res, arr[i])
#     return res
    
# def getMax(arr, n):
#     res = arr[0]
#     for i in range (1, n):
#         res = max(res, arr[i])
#     return res

# arr = [1,5,8,10]
# n = len(arr)
# print("min number is: ", getMin(arr, n))
# print("max number is: ", getMax(arr, n))


#Rearrange array such that -ve num first and +ve num at last
# def rearrangeArray(arr, n):
#     j = 0
#     for i in range(0, n):
#         if(arr[i] < 0):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             j = j+1

# arr = [-1,2,-3,4,-5,-6,-7,8,9,10]
# n = len(arr)
# rearrangeArray(arr, n)
# print(arr)


#find peak element in array
# def findPeak(arr, n):
#     if(n == 1):
#         return 0
#     if(arr[0] >= arr[1]):
#         return 0
#     if(arr[n-1] >= arr[n-2]):
#         return n-1
#     for i in range(1, n-1):
#         if(arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
#             return i
# arr = [1,2,20,4,1,0]
# n = len(arr)
# print("Index of peak element is: ", findPeak(arr,n))


#sort array 0,1,2 
# def sort012(arr, n):
#     low = 0
#     high = n-1
#     mid = 0
#     while mid <= high:
#         if arr[mid] == 0:
#             arr[low], arr[mid] = arr[mid], arr[low]
#             low += 1
#             mid += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:
#             arr[mid],arr[high] = arr[high], arr[mid]
#             high -= 1
#     return arr


# def printArray(arr):
#     for num in arr:
#         print(num)

# arr = [1,2,0,2,0,1,0,1,0,2,2,1,0,0]
# n = len(arr)
# result = sort012(arr, n)
# print(result)    


#count occurence of num in an array
# def countOccurence(arr, n, x):
#     res = 0
#     for i in range(n):
#         if x == arr[i]:
#             res += 1
#     return res
# arr = [1,2,2,2,3,4,5,2,2,2]
# n = len(arr)
# x = 2
# print(countOccurence(arr, n, x))


#find union and intersection in an array
# def UnionIntersection(arr1, arr2):
#     # Convert arrays to sets to get unique elements
#     set1 = set(arr1)
#     set2 = set(arr2)
    
#     # Union: Merge both sets and convert back to list
#     union_list = list(set1.union(set2))
    
#     # Intersection: Get common elements from both sets
#     intersection_list = list(set1.intersection(set2))
    
#     return union_list, intersection_list
  
# if __name__ == "__main__":
#     arr1 = [1, 2, 2, 2, 3]
#     arr2 = [2, 3, 3, 4, 5, 5]
#     # Function call
#     union, intersection = UnionIntersection(arr1, arr2) 
#     print("Union:", union)
#     print("Intersection:", intersection)


#program to print subarray with sum as given sum

# def subArraySum(arr, n, sum):

#     for i in range(0,n):
#         currentSum = arr[i]
#         if(currentSum == sum):
#             print("Sum found at indexes",i)
#             return
#         else:
#             # Try all subarrays starting with 'i'
#             for j in range(i+1,n):
#                 currentSum += arr[j]
#                 if(currentSum == sum):
#                     print("Sum found between indexes",i,"and",j)
#                     return
#     print("No Subarray Found")

# if __name__ == "__main__":
#     arr = [15,2,4,8,9,5,10,23]
#     n = len(arr)
#     sum = 23
#     subArraySum(arr, n, sum)


#find kth smallest number in an array
# def kthSmallest(arr, N, K):

#     arr.sort()
#     # Return k'th element
#     return arr[K-1]

# if __name__ == '__main__':
#     arr = [12, 3, 5, 7, 19]
#     N = len(arr)
#     K = 2
#     print("K'th smallest element is", kthSmallest(arr, N, K))


#find factorial of large number using biginteger
# def factorial(n):
#     res = 1
#     for i in range(2, n+1):
#         res *= i
#     return res
# n = 20
# print(factorial(n))

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# def main():
#     n = 10
#     res = fibonacci(n)
#     print(res)

# if __name__ == "__main__":
#     main()





