# print(help(list.sort))

def key_sort(x):
    return x[1][1]


my_list = [(2, 'cv'), (1, 'ax'), (2, 'cc')]
my_list.sort(key=key_sort, reverse=True)
# ['cv', 'd', 'cc']

print(my_list)  # [(1, 'd'), (2, 'cv'), (2, 'cc')]


lst = ['aac', 'aab', 'aaa']
lst.sort()
print(lst)  # ['aaa', 'aab', 'aac']
