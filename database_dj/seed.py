from app import app
from models import db, Playlist, Song, PlaylistSong

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create playlists
    p1 = Playlist(name="Workout Mix", description="High energy songs")
    p2 = Playlist(name="Chill Vibes", description="Relaxing tunes")

    # Create songs
    s1 = Song(title="Eye of the Tiger", artist="Survivor")
    s2 = Song(title="Blinding Lights", artist="The Weeknd")
    s3 = Song(title="Ocean Eyes", artist="Billie Eilish")
    s4 = Song(title="Shape of You", artist="Ed Sheeran")

    # Add all to session and commit
    db.session.add_all([p1, p2, s1, s2, s3, s4])
    db.session.commit()

    # Associate songs to playlists
    ps1 = PlaylistSong(playlist_id=p1.id, song_id=s1.id)
    ps2 = PlaylistSong(playlist_id=p1.id, song_id=s2.id)
    ps3 = PlaylistSong(playlist_id=p2.id, song_id=s3.id)
    ps4 = PlaylistSong(playlist_id=p2.id, song_id=s4.id)

    db.session.add_all([ps1, ps2, ps3, ps4])
    db.session.commit()

    print("Seeded database successfully.")
