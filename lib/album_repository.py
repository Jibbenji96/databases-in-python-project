from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], 
                        row["title"], 
                        row["release_year"], 
                        row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [id])
        row = rows[0]  
        if row is None:
            return None
        
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

        # for d in row:
        #     item = Album(d["id"], 
        #                 d["title"], 
        #                 d["release_year"], 
        #                 d["artist_id"])
        #     specified_album.append(item)
        
        # return specified_album

    def create(self, title, release_year, artist_id):
        artist_exists = self._connection.execute(
            "SELECT EXISTS(SELECT 1 FROM artists WHERE id = %s)", 
            [artist_id]
        )[0]['exists']
        
        if not artist_exists:
            raise Exception(f"Artist with id {artist_id} not in music library.")
        
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)",
            [title, release_year, artist_id])
        
    def delete(self, id):
        self._connection.execute("DELETE FROM albums WHERE id = %s", [id])