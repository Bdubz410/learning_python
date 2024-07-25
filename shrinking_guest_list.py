# You just found out that your new dinner table won't arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from exercise more_guests. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they're still invited.
# Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program. Should just be []
guest_list = ['charlie chaplin', 'kaeden', 'madre']
guest_list[-1] = 'brian'
guest_list.insert(0, 'oscar wilde')
guest_list.insert(3, 'jane austin')
guest_list.insert(-1, 'einstein')
print(f'Hey there, {guest_list}, my new table will not arrive in time so I can only invite two guests to dinner.')

first_guest = guest_list.pop(0).title()
print(f'I regret to inform you, {first_guest}, that I will reschedule our dinner party for a later date.')

second_guest = guest_list.pop(0).title()
print(f'I am sorry, {second_guest}, but I must cancel the dinner invitation I sent earlier.')

third_guest = guest_list.pop(1).title()
print(f'I am sorry to inform you, {third_guest}, that I will be cancelling the large dinner party.')

fourth_guest = guest_list.pop(-1).title()
print(f'Hey {fourth_guest}, I am sorry but I will reschedule dinner for a later date.')

print(f'Obviously my babe, {guest_list[0].title()}, is not uninvited!!')
print(f'Hey, {guest_list[-1].title()}, you are still invited to dinner!')

del guest_list[0]
del guest_list[-1]
print(guest_list)