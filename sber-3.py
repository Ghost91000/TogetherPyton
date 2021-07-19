# Задание 1

list1 = [-5, 5, 10]
max1 = max(list1)
min1 = min(list1)
max2 = list1.index(max1)
min2 = list1.index(min1)

list2 = list1[:]
list2[max2], list2[min2] = list2[min2], list2[max2]
print(list2)
