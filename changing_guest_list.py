# You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
# You'll have to think of someone else to invite.
# Start your program from the guest_list exercise.
# Add a print() call at the end of your program, stating the name of the guest who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
guest_list = ['charlie chaplin', 'kaeden', 'madre']

print(f'{guest_list[-1].title()}')

guest_list[-1] = 'brian'

print(f'Hola {guest_list[0]}, I would like to invite you to dinner.')
print(f'My mother cannot make it to my dinner, {guest_list[-1]} since you are in town will you join?')
print(f'Hey {guest_list[1]}, I would like you to join my dinner.')