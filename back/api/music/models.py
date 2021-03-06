from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=128)
  nationality = models.CharField(max_length=128, null=True)
  image = models.TextField(null=True)

  def __str__(self):
    return f'{self.name}'

class Album(models.Model):
  image = models.TextField(null=True)
  name = models.CharField(max_length=128, null=True)
  genre = models.CharField(max_length=128, null=True)
  release_date = models.DateField(null=True)
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
  # authors = models.ManyToManyField(Artist, through='AlbumsArtists',null=True)
  author = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return f'{self.name}'

class Song(models.Model):
  name = models.CharField(max_length=128)
  song_length = models.CharField(max_length=128, null=True)
  song_file = models.TextField(null=True)
  song_preview = models.TextField(null=True)
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
  play = models.IntegerField(null=True, default=0)
  album = models.ForeignKey(Album, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name}'

# class AlbumsArtists(models.Model):
# 	album = models.ForeignKey(Album, related_name='AlbumWithArtists', on_delete=models.DO_NOTHING)
# 	artist = models.ForeignKey(Artist, related_name='ArtistWithAlbums', on_delete=models.DO_NOTHING)

# 	def __str__(self):
# 		return f'{self.id}'

class Ticket(models.Model):
  purchase_date = models.DateField(null=True)
  user = models.CharField(max_length=128, null=True)
  albums = models.ManyToManyField(Album, through='TicketsAlbums',null=True)
  songs = models.ManyToManyField(Song, through='TicketsSongs',null=True)
  total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

  def __str__(self):
    return f'{self.name}'

class TicketsAlbums(models.Model):
	album = models.ForeignKey(Album, related_name='AlbumWithTickets', on_delete=models.DO_NOTHING)
	ticket = models.ForeignKey(Ticket, related_name='TicketWithAlbums', on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.id}'

class TicketsSongs(models.Model):
	song = models.ForeignKey(Song, related_name='SongWithTickets', on_delete=models.DO_NOTHING)
	ticket = models.ForeignKey(Ticket, related_name='TicketWithSongs', on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.id}'
