# multiplication table
# n = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(n*i)

#sum of n natural number
# n = 5
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

#sum of number
# n = 7
# sum = 0
# i = 0
# while i <= n:
#     sum += i
#     i += 1
# print(sum) 
   
#factorial of n number
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i +=1
# print("factorial of n is,", fact) 
   
#factorial of num in for loop
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)    

# list = [1,2,3,4,5]
# sum = 0
# for i in list:
#     sum += i
# print(sum)
# print(sum/len(list))

# n = int(input("Enter a number"))
# for i in range(1,11):
#     mul = n*i
#     print(n, "*",i, "=", mul)    

# #function name
# def cal_sum(a,b):#function parameter
#     return a + b
# sum = cal_sum(5,5)#function call or arguments
# print(sum)


# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum / 3
#     print(avg)
#     return avg
# cal_avg(98,50,80)


# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(5) 


# def converter(usd_val):
#     inr_val = usd_val * 75
#     print(usd_val, "USD =", inr_val, "INR")
# converter(5)

#function to find odd even number
# def find_num(n):
#     if(n %2 == 0):
#         print("The number is EVEN")
#     else:
#         print("The number is ODD")
# find_num(1)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def fact(n):
#     if(n==0):
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(5))


#sum of n natural number
# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1) + n
# sum = cal_sum(10)
# print(sum)

#print list of item in recursion:
# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "orange", "banana", "apple"]
# print_list(fruits)