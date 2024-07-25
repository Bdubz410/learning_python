# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from guest_list and changing_guest_list. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use insert() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.
guest_list = ['charlie chaplin', 'kaeden', 'madre']
guest_list[-1] = 'brian'
#print(f'Hey everyone, {guest_list} I found a bigger table for dinner!')

guest_list.insert(0, 'oscar wilde')
guest_list.insert(2,'jane austin')
guest_list.insert(-1, 'einstein')

print(f'Hey {guest_list[0].title()}, would you like to join my big dinner party?')
print(f'Hey {guest_list[1].title()}, perhaps a dinner party?')
print(f'Hi {guest_list[2].title()}, how would you like to partake in a dinner party?')
print(f'Hola {guest_list[3].title()}, you must join dinner!')
print(f'Hey there {guest_list[4].title()}, would you like to join a dinner party?')
print(f'Hello {guest_list[-1].title()}, please join my dinner party with several other amazing guests.')