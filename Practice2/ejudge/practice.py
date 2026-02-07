# a = int(input())
# if a %4 ==0 and a%100!=0 or a%400==0:
#     print("YES")
# else:
#     print("NO")




# a = int(input())
# sum =0
# for i in range(1,a+1):
#     sum +=i
# print(sum)




# n = int(input())
# numbers = list(map(int, input().split()))
# print(sum(numbers))




# a = int(input())
# numbers = list(map(int, input().split()))
# sum = 0 
# for b in numbers:
#     if b > 0:
#         sum+=1
# print(sum)




# a = int(input())
# while a >1:
#     if a%2==0:
#         a/=2
#         continue
#     else:
#         print("NO")
#         break
# else:
#     print("YES")




# a = int(input())
# num = list(map(int, input().split()))
# print(max(num))




# a = int(input())
# num = list(map(int, input().split()))
# print(max(num))




# a = int(input())
# i = 1
# while i <= a:
#     print(i, end = ' ')
#     i*=2




# a = int(input())
# num = list(map(int, input().split()))
# max_num = max(num)
# min_num = min(num)
# for x in num:
#     if x == max_num:
#         print(min_num, end = ' ')
#         continue
#     print(x, end = ' ')



# a = int(input())
# num = list(map(int, input().split()))
# num.sort(reverse = True)
# for x in num:
#     print(x, end = ' ')



# a = list(map(int, input().split()))
# nums = list(map(int, input().split()))
# nums[a[1]-1:a[2]] = nums[a[1]-1:a[2]][::-1]
# print(*nums)




# a = int(input())
# b = list(map(int, input().split()))
# for x in b:
#     print(x**2, end =' ')




# a = int(input())
# if a<=1:
#     print("No")
# else:
#     for i in range(2 , int(a**0.5)+1):
#         if a % i == 0:
#             print("No")
#             break
#     else: 
#         print("Yes")





# a = int(input())
# arr = list(map(int, input().split()))

# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num] = 1

# max_freq = max(freq.values())

# c = list()
# for num, count in freq.items():
#     if count == max_freq:
#         c.append(num)
# print(min(c))



# a = int(input())
# surnames = list()
# counter =0
# for i in range(a):
#     b = input()
#     surnames.append(b)
# uniq = set(surnames)
# print(len(uniq))




# a = int(input())
# numbers = set() 
# arr = list(map(int, input().split())) 

# for b in arr:
#     if b not in numbers:
#         print("YES")
#         numbers.add(b)
#     else:
#         print("NO")




# a = int(input())
# all_numbers = list()
# counter = 0
# for i in range(a):
#     b = input()
#     all_numbers.append(b)
# tel = set(all_numbers)
# for x in tel:
#     if all_numbers.count(x) == 3:
#         counter +=1
# print(counter)




# a = int(input())
# arr = list()
# for i in range(a):
#     b = input()
#     arr.append(b)
# uniq_arr = sorted(set(arr))
# for x in uniq_arr:
#     print(x, arr.index(x)+1)




n = int(input())
ep = {}

for i in range(n):
    s, k = input().split()
    k = int(k)
    if s in ep:
        ep[s] += k
    else:
        ep[s] = k

for d in sorted(ep):
    print(d, ep[d])
