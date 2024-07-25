# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
# append(), insert(), pop(), sort(), reverse(), sorted(), remove()
my_list = []

my_list.append('santa fe')
my_list.insert(1, 'anywhere, alaska')
my_list.insert(2, 'cali')
my_list.append('home')
print(my_list)

back_list = my_list.pop(0)
my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list)
print(back_list)

print(sorted(my_list))

my_list.remove('cali')
my_list.remove('home')
print(my_list)