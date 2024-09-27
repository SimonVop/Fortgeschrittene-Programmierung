import csv  
import os   
import time 

songs = []

# Klasse zur Darstellung eines Songs
class Song:
    # Initialisiert ein Song-Objekt
    def __init__(self, name, artist, album, genre, likes):
        self.name = name       
        self.artist = artist   
        self.album = album     
        self.genre = genre     
        self.likes = likes

    # Gibt den Song als String zurück
    def __str__(self):
        return f"{self.name} by {self.artist} - Album: {self.album}, Genre: {self.genre}, Likes: {self.likes}"

    # Konvertiert das Song-Objekt in ein Dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'artist': self.artist,
            'album': self.album,
            'genre': self.genre,
            'likes': self.likes
        }

    # Erstellt ein Song-Objekt aus einem Dictionary
    @staticmethod
    def from_dict(data):
        return Song(data['name'], data['artist'], data['album'], data['genre'], data['likes'])


# Klasse zur Darstellung einer Playlist
class Playlist:
    # Initialisiert eine Playlist
    def __init__(self, name):
        self.name = name          
        self.songs = []           

    # Fügt einen Song zur Playlist hinzu
    def add_song(self, song):
        self.songs.append(song)

    # Gibt die Playlist als String zurück
    def __str__(self):
        return f"Playlist: {self.name}, Songs: {len(self.songs)}"

    # Konvertiert die Playlist in ein Dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'songs': [song.to_dict() for song in self.songs]
        }

    # Erstellt eine Playlist aus einem Dictionary
    @staticmethod
    def from_dict(data):
        playlist = Playlist(data['name'])
        playlist.songs = [Song.from_dict(song_data) for song_data in data['songs']]
        return playlist


# Hauptklasse für die Musik-App
class MusicApp:
    # Initialisiert die Musik-App und lädt Daten
    def __init__(self, data_file='C:/Users/svo64/StudioCodes/Algorithmus/music.csv'): 
        self.data_file = data_file  
        self.playlists = []         
        self.songs = []              
        self.load_data()            

    # Lädt die Songs und Playlists aus einer CSV-Datei
    def load_data(self):
        with open(self.data_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            loading_playlists = False 
            
            for row in csv_reader:
                if row == []:
                    loading_playlists = True
                    continue

                elif not loading_playlists:
                    song_objekt = Song(row[0], row[1], row[2], row[3], row[4])
                    songs.append(song_objekt)
                else:
                    playlist_name = row[0]   
                    song_title = row[1]      

                    playlist = next((p for p in self.playlists if p.name == playlist_name), None)

                    if not playlist:
                        playlist = Playlist(playlist_name)
                        self.playlists.append(playlist)

                    for playlist in self.playlists:
                        for s in songs:
                            if s.name == song_title and s not in playlist.songs:
                                playlist.add_song(s)

        print('Data successfully loaded')

    # Speichert die Songs und Playlists in einer CSV-Datei
    def save_data(self):
        with open(self.data_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for song in songs:
                writer.writerow([song.name, song.artist, song.album, song.genre, song.likes])
            
            writer.writerow([])

            for playlist in self.playlists:
                for song in playlist.songs:
                    writer.writerow([playlist.name, song.name])

        print('Data saved successfully.')

    # Fügt einen neuen Song zur Liste hinzu
    def add_song(self):
        name = input("Enter song name: ")
        artist = input("Enter artist name: ")
        album = input("Enter album name: ")
        genre = input("Enter genre: ")
        likes = input('Enter your likes: ')
        song = Song(name, artist, album, genre, likes)
        songs.append(song)
        print(f"Added song: {song}")

    # Erstellt eine neue Playlist
    def create_playlist(self):
        name = input("Enter playlist name: ")
        playlist = Playlist(name)
        self.playlists.append(playlist)
        print(f"Created playlist: {playlist}")

    # Fügt einen Song zu einer bestehenden Playlist hinzu
    def add_song_to_playlist(self):
        playlist_name = input('Enter the name of the playlist: ')
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                song_name = input('Enter the song to be added: ')
                for s in songs:
                    if s.name == song_name:                         
                        playlist.add_song(s)
                        print(f"Added {s.name} to playlist {playlist.name}")
                    else:
                        print('Song not found')
            else:
                print('Playlist not found')

    # Bubble-Sort-Algorithmus zum Sortieren von Songs
    def bubble_sort(self, songs, key):
        n = len(songs)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if key == 'likes': 
                    if int(getattr(songs[j], key)) < int(getattr(songs[j+1], key)):
                        songs[j], songs[j+1] = songs[j+1], songs[j]
                        swapped = True
                else:
                    if getattr(songs[j], key) > getattr(songs[j+1], key):  
                        songs[j], songs[j+1] = songs[j+1], songs[j]
                        swapped = True
            if not swapped:
                break

    # Sucht nach Songs
    def search_songs(self):
        print('1. Linear Search')
        print('2. Binary Search')
        searching_algorithm = input('Enter the searching algorithm: ')

        if searching_algorithm == '1':
            print("Sort by:")
            print("1. Title")
            print("2. Artist")

            sort_input = input("(T)itle or (A)rtist ")
            if sort_input == 'T':
                key = 'name'
            elif sort_input == 'A':
                key = 'artist'
            else:
                print("Invalid choice. No sorting applied.")
                return
            
            lookup = input(f"Enter the {key} you are looking for: ")

            def linear_search(songs, key, lookup):
                start_time = time.time()
                songs_found = []
                for song in songs:
                    if getattr(song, key).lower() == lookup.lower():
                        songs_found.append(song)
                end_time = time.time()
                print(f"Linear Search completed in {end_time - start_time:.6f} seconds")
                return songs_found
            
            songs_found = linear_search(songs, key, lookup)

            if songs_found:
                print(f"Found {len(songs_found)} song(s)")
                for song in songs_found:
                    print(song)
            else:
                print("No songs found")

        if searching_algorithm == '2':
            def binary_search(songs, key, lookup):
                start_time = time.time()
                left = 0
                right = len(songs) - 1

                if left <= right:
                    mid = (left + right) // 2
                    if songs[mid] == lookup:
                        end_time = time.time()
                        return lookup
                    elif songs[mid] > lookup:
                        end_time = time.time()
                        return binary_search(songs, left, mid - 1, lookup)
                    else:
                        return binary_search(songs, mid + 1, right, lookup)
                else:
                    return -1    
            index = binary_search(songs, key, lookup)

            if index != -1:
                print(f"Song found: {songs[index]}")
            else:
                print("No songs found")

    # Sortiert die Songs
    def sort_songs(self):
        print('1. Bubble Sort')
        print('2. Shell Sort')
        sorting_algorithm = input('(S)ort or (B)ubble ')

        if sorting_algorithm == '1':
            print("Sort by:")
            print("1. Title")
            print("2. Artist")

            sort_input = input("What are you looking for?: ")
            if sort_input == '1':
                key = 'name'
            elif sort_input == '2':
                key = 'artist'
            else:
                print("Invalid choice. No sorting applied.")
                return
            start_time = time.time()
            self.bubble_sort(songs, key)
            end_time = time.time()
            print(f"Bubble Sort completed in {end_time - start_time:.6f} seconds")

        elif sorting_algorithm == '2':
            sort_input = input("(T)itle or (A)rtist ")
            if sort_input == 'T':
                key = 'name'
            elif sort_input == 'A':
                key = 'artist'
            else:
                print("Invalid choice. No sorting applied.")
                return

        # Shell-Sort-Algorithmus
        def shell_sort(self, key):
            gap = len(self.songs) // 2
            while gap > 0:
                for i in range(gap, len(self.songs)):
                    temp = self.songs[i]
                    j = i
                    while j >= gap and getattr(self.songs[j - gap], key) > getattr(temp, key):
                        self.songs[j] = self.songs[j - gap]
                        j -= gap
                    self.songs[j] = temp
                gap //= 2

        print("Songs sorted successfully.")

    def run(self):
        # Main loop for interacting with the Music App
        while True:
            print("\nMenu:")
            print("1. Add a song")
            print("2. Create a playlist")
            print("3. Add a song to a playlist")
            print("4. Search for a song")
            print("5. Sort songs")
            print("6. Save and exit")

            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_song()
            elif choice == '2':
                self.create_playlist()
            elif choice == '3':
                self.add_song_to_playlist()
            elif choice == '4':
                self.search_songs()
            elif choice == '5':
                self.sort_songs()
            elif choice == '6':
                self.save_data()
                break
            else:
                print("Invalid choice, please try again.")



if __name__ == "__main__":
    app = MusicApp() # Erstellt eine Instanz der Musik-App
    app.run() # Öffnet das Hauptmenü

