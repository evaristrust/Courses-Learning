class Song:
    """Class to represent a song

    Attributes:
        title(str): title of the song
        artist(Artist): the artist object representing the song creator
        duration(int): The duration of the song in seconds. Maybe zero
    """
    def __init__(self, title, artist):
        """Song init method

        Args:
            title(str): Initialises the '_title' attr
            artist(Artist): '_artist Attr Object representing the song creator
            duration(Optional(int): initial value for the duration attribute '_duration'
                will default to zero if not defined
        """
        self._title = title
        self._artist = artist
        self._duration = duration

class Album:
    """Class to represent an album
    Attributes:
        name (str): The name of an album
        year (int): The year of release
        artist (Artist): The artist name. If not specified,
        the artist will default to an artist with the name "Various Artists

    Methods:
        add_song: Used to add a new song to the album's track list
    """
    def __init__(self, album, year, artist):
        self._album_name = album
        self._year = year
        if artist is None:
            self._artist = Artist('Various Artists')
        else:
            self._artist = artist
        self._tracks = []

    def add_song(self, song, position=None):
        """adds a song to the album on a certain position
        Args:
            song (str): the name of the song
            position(Option(int)): the position where the song is located. If specified, the song will be added
            to the position __ inserting in between other songs. else, it will be added to the end
        """
        if position is None:
            self._tracks.append(song)
        else:
            self._tracks.insert(position, song)

class Artist:
    """Basic class to store artist details.
    Attributes:
        name (str): The name of the artist
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's puplished albums
    Methods:
        add_album: Use the add a new album to the artist
    """
    def __init__(self, name):
        self._name = name
        self._albums_list = []

    def add_album(self, album):
        """Add a new album here.
        Args:
            album (Album): Album object to add to the list.
            If the album already exists, it will not be added again. (although this is yet to implement)
        """
        self._albums_list.append(album)

# if there was a file.txt that contained the album of the artist
# we should do like that. we will need to load and open the file

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consists artist, album, year, and song
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print('{}:{}:{}:{}'.format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist._name != artist_field:
                # We've just read details for a new artist
                # Store the current album in the current artists collection then create a new artist object
                new_artist.add_album(new_artist)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album._album_name != album_field:
                # We've just read a new album for the current artist
                # Store the current album in the artist's collection then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)
        # after reading the last line of the text file, we will
        # have an artist and album that haven't been in the store
        # and process them

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
    return artist_list

# def create_checkfile(artist_list):
#     """Create a check file from the object data for the comparison between the original file"""
#     with open('checkfile.txt', 'w') as checkfile:
#         for new_artist in artist_list:
#             for new_album in new_artist._albums_list:
#                 for new_song in new_album_tracks:
#                     print('{0._name}\t{1._name}{1._year}\t{2._title}'.format(new_artist, new_album, new_song),
#                           file='checkfile')


if __name__ == '__main__':
    artists = load_data()
    print('There are {} artists'.format(len(artists)))

    # create_checkfile(artists)
    # will imediately begin on the vid 12




