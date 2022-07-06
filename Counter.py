from collections import Counter

a = 'ostentandonoscodigos'
my_counter = Counter(a)

print(my_counter)
print(my_counter.items())
print(my_counter.values())
print(my_counter.most_common())
print(my_counter.elements())
print(list(my_counter.elements()))
