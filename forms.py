# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[InputRequired(), Length(max=50)])
    description = StringField("Description")


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", validators=[InputRequired(), Length(max=100)])
    artist = StringField("Artist", validators=[InputRequired(), Length(max=100)])

    playlist = SelectField('Playlist', coerce=int)


class AddSongToPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField("Song To Add", coerce=int)
