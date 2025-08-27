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
        rows = self._connection.execute(f"SELECT * FROM albums WHERE id = {id}")
        # specified_album = []
        # specified_album = [Album(d['id'], d['title'], d['release_year'], d['artist_id']) for d in specified_row]
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
        