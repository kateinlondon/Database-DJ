# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# models.py
class Playlist(db.Model):
    # playlist_songs = db.relationship('PlaylistSong', backref='playlist', cascade="all, delete")

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    songs = db.relationship("Song", secondary="playlist_songs", backref="playlists")


class Song(db.Model):
    """Song model."""

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_songs"

    song = db.relationship('Song', backref='playlist_song')

    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key=True)


def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)
