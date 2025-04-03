from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import PlaylistForm, SongForm, AddSongToPlaylistForm
from models import db, connect_db, Playlist, Song, PlaylistSong
from config import Config  # if not already imported

app = Flask(__name__)
app.config.from_object(Config)
connect_db(app)


with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    form = PlaylistForm()
    return render_template('home.html', form=form)

@app.route('/playlists')
def show_playlists():
    playlists = Playlist.query.all()
    return render_template('playlist.html', playlists=playlists)

@app.route('/playlists/add', methods=['GET', 'POST'])
def add_playlist():
    form = PlaylistForm()
    if form.validate_on_submit():
        new_playlist = Playlist(name=form.name.data, description=form.description.data)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect('/playlists')
    return render_template('add_playlist.html', form=form)

@app.route('/songs')
def show_songs():
    songs = Song.query.all()
    return render_template('song.html', songs=songs)

@app.route('/songs/add', methods=['GET', 'POST'])
def add_song():
    form = SongForm()
    form.playlist.choices = [(p.id, p.name) for p in Playlist.query.all()]

    if form.validate_on_submit():
        new_song = Song(title=form.title.data, artist=form.artist.data)
        db.session.add(new_song)
        db.session.commit()

        playlist_song = PlaylistSong(playlist_id=form.playlist.data, song_id=new_song.id)
        db.session.add(playlist_song)
        db.session.commit()

        return redirect('/songs')

    return render_template('song.html', form=form)


@app.route('/playlists/<int:playlist_id>/add-song', methods=['GET', 'POST'])
def add_song_to_playlist(playlist_id):
    playlist = Playlist.query.get_or_404(playlist_id)
    form = AddSongToPlaylistForm()
    form.song.choices = [(s.id, s.title) for s in Song.query.all()]
    if form.validate_on_submit():
        playlist_song = PlaylistSong(playlist_id=playlist_id, song_id=form.song.data)
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(f'/playlists/{playlist_id}')
    return render_template('add_song_to_playlist.html', playlist=playlist, form=form)



