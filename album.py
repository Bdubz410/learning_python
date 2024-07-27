# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information perfectly.
def make_album(artist_name, album_title):
    """Describe a music album."""
    album = {'artist': artist_name, 'album': album_title}
    return album

albums = make_album('prince', 'purple rain')
print(albums)

albums = make_album('shakira', 'shake it')
print(albums)

albums = make_album('shaggy', 'it was not me')
print(albums)

# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs, add that value to the album's dictionary.
# Make at least one new function call that includes the number of songs on an album.
def make_album(artist_name, album_title, songs=None):
    """Describe a music album."""
    album = {'artist': artist_name, 'album': album_title}
    if songs:
        album['songs'] = songs
    return album

albums = make_album('ludacris', 'red light district', songs=28)
print(albums)