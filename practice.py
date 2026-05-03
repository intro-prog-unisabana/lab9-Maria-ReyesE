from song import Song

def print_songs(song_list):
    for song in song_list:
        print(song)

songs = []

n = int(input("How many songs do you want to enter? "))

for _ in range(n):
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    duration = float(input("Enter duration: "))
    
    song = Song(title, artist, duration)
    songs.append(song)

print_songs(songs)