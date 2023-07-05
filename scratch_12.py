# s1 = 'My Name is Jessa'
# x=s1.split(" ")
# for i in x:
#     y=i[::-1]
#     print(y ,end=" ")

# l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# l2=[]
# for i in l1:
#     if i<=50:
#         l2.append(i)
# print(l2)

# dict1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# x={value:key for key,value in dict1.items()}
# print(x)

# l1 = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# set={}
# l2=[]
# for i in l1:
#     if i not in set:
#         set[i]=1
#     else:
#         l2.append(i)
# print(l2)

# d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# l1 = ['A', 'C', 'F']
# x = {key: d1[key] for key in l1}
# print(x)

# rows = 5
# x = 0
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     x += 1
#     for j in range(1, i + 1):
#         print(x, end=' ')
#     print('\r')

# l1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# l1[1][2][2][1]=3500
# print(l1)

emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}
print(emp_dict["company"]["employee"]["payable"]["increment"])

