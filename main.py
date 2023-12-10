#23)Generate a dictionary from a list ,Where value of key would be it's just next element::
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#
# res={j for i,j in enumerate(l)}
# print(res)




# d={}
# for i in range(len(l)-1):
#     d[l[i]]=l[i+1]
# print(d)






# res={}
# dict1={}
# while l:
#     if len(l)==1:
#         dict1[l[0]]=0
#         l=[]
#
#     else:
#         dict1[l[0]]=l[1]
#         l=l[2:]
# print(dict1)


# l=[1,4,5,2]
# k=6
# count=0
# for i in range(len(l)):
#     for j in l:
#         if i+j==k:
#             print((i,j))
#             count+=1
#
# print(count)
# res1=[(i,j)  for i in range(len(l)) for j in l if i+j==k]
# print(res1)
#
# l = [1, 4, 5, 2]
# k = 6
# count = 0
# value_to_index = {}
#
# for i, num in enumerate(l):
#     complement = k - num
#     if complement in value_to_index:
#         print((complement, num))
#         count += 1
#     value_to_index[num] = i
#
# print("Total pairs found:", count)



































