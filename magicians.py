# Looping through an entire list; be sure to remember the ':' and proper indentation.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Doing more work within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cannot wait to see your next trick, {magician.title()}.\n")
print('Thank you everyone that was a great show!')