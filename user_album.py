# Start with your program from Album exercise.
# Write a while loop that allows users to enter an album's artist and title.
# Once you have that information, call make_album() with the user's input and print the dictionary that's created.
# Be sure to include a quit value in the while loop
def make_album(artist_name, album_title):
    """Describe a music album."""
    album = f"{artist_name} {album_title}"
    return album.title()

while True:
    print("\nTell me an artist and your favorite album from them:")
    print("(Enter 'q' at any point to quit)")

    a_name = input("Enter the artist's name: ")
    if a_name == 'q':
        break
    al_name = input("Enter their album: ")
    if al_name == 'q':
        break
    favorite_album = make_album(a_name, al_name)
    print(f"\n{favorite_album}")