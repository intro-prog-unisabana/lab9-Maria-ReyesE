# rite your code here!
class Song:
    def __init__(self, name , artist, length):
        self.title = name
        self.artist = artist
        self.length = length

    def get_length_in_seconds(self):
        return self.length * 60
    def __str__(self):
        return f"{self.title} by {self.artist} ({self.length})"
    
