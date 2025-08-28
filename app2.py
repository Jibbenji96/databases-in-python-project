from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")


    def run(self):
        try: 
            welcome_message = int(input(
            "\nWelcome to the music library manager! \n\n\n" \
            "What would you like to do?\n\n" \
            "1 - List all albums\n" \
            "2 - List all artists\n\n" \
            "Enter your choice:  ")
            )
        except ValueError:
            print("Invalid input, please enter a number (1 or 2).")
            return

        valid_inputs = ("1","2")

        if welcome_message not in valid_inputs:
            print("Invalid input, 1 or 2 required. Please run application again.")

        if welcome_message == 1:
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()

            for index, album in enumerate(albums, start=1):  
                print(f"* {index} - {album.title}")  

        elif welcome_message == 2:
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()

            for index, artist in enumerate(artists, start=1):  
                print(f"* {index} - {artist.name}") 


if __name__ == '__main__':
    app = Application()
    app.run()
