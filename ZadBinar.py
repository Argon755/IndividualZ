from random import randint
 
# Создание списка,
# его сортировка по возрастанию
# и вывод на экран
a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)
 
# искомое число
value = int(input())
 
