class Song:
    """Class to represent a song

    Attributes:
        title(str): title of the song
        artist(Artist): the artist object representing the song creator
        duration(int): The duration of the song in seconds. Maybe zero
    """
    def __init__(self, title, artist, duration):
        # """Song init method
        #
        # Args:
        #     title(str): Initialises the '_title' attr
        #     artist(Artist): '_artist Attr Object representing the song creator
        #     duration(Optional(int): initial value for the duration attribute '_duration'
        #         will default to zero if not defined
        # """
        self._title = title
        self._artist = artist
        self._duration = duration

# help(Song)
# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)

# another way of creating a doc string

Song.__init__.__doc__ = """Song init method

                        Args:
                            title(str): Initialises the '_title' attr
                            artist(Artist): '_artist Attr Object representing the song creator
                            duration(Optional(int): initial value for the duration attribute '_duration'
                                will default to zero if not defined
                        """
help(Song)