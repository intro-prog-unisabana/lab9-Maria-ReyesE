# rite your code here!
class Song:
    def __init__(self, name , artist, length):
        self.title = name
        self.artist = artist
        self.length = length

    def get_length_in_seconds(self):
        return self.length * 60

my_song = Song("tv off", "Kendrick Lamar", 3.7)
print(my_song.get_length_in_seconds())
