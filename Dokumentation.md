Dokumentation der Musik-App
Einführung
Die Musik-App ist ein einfaches Python-Programm zur Verwaltung von Songs und Playlists. Die App ermöglicht Benutzern das Hinzufügen, Suchen, Sortieren und Speichern von Songs sowie das Erstellen und Verwalten von Playlists. Die Anwendung nutzt eine CSV-Datei zur dauerhaften Speicherung von Daten. Diese Dokumentation beschreibt die Struktur und die Funktionalitäten der App im Detail, einschließlich der Hauptklassen und -methoden.

Hauptklassen und -methoden
1. Klasse: Song
Die Klasse Song repräsentiert einen Musiksong und enthält folgende Attribute:

name: Der Titel des Songs.
artist: Der Künstler, der den Song performt.
album: Das Album, aus dem der Song stammt.
genre: Das Genre des Songs.
likes: Die Anzahl der Likes, die der Song erhalten hat.
Konstruktor
python
Code kopieren
def __init__(self, name, artist, album, genre, likes):
Initialisiert ein neues Song-Objekt mit den angegebenen Attributen.
Methoden
__str__(): Gibt eine stringbasierte Darstellung des Songs zurück.
to_dict(): Konvertiert das Song-Objekt in ein Dictionary, um die Speicherung zu erleichtern.
from_dict(data): Statische Methode, die ein Song-Objekt aus einem Dictionary erstellt.
2. Klasse: Playlist
Die Klasse Playlist repräsentiert eine Sammlung von Songs und enthält folgende Attribute:

name: Der Name der Playlist.
songs: Eine Liste von Song-Objekten, die zur Playlist gehören.
Konstruktor
python
Code kopieren
def __init__(self, name):
Initialisiert eine neue Playlist mit dem angegebenen Namen.
Methoden
add_song(song): Fügt einen Song zur Playlist hinzu.
__str__(): Gibt eine stringbasierte Darstellung der Playlist zurück.
to_dict(): Konvertiert die Playlist in ein Dictionary.
from_dict(data): Statische Methode, die eine Playlist aus einem Dictionary erstellt.
3. Klasse: MusicApp
Die MusicApp ist die Hauptklasse, die die Funktionen der App organisiert. Sie verwaltet sowohl Songs als auch Playlists und enthält Methoden für Interaktionen mit dem Benutzer.

Konstruktor
python
Code kopieren
def __init__(self, data_file='C:/Users/svo64/StudioCodes/Algorithmus/music.csv'):
Initialisiert die App und lädt Daten aus einer angegebenen CSV-Datei.
Methoden
load_data(): Lädt Songs und Playlists aus der CSV-Datei und erstellt die entsprechenden Objekte.
save_data(): Speichert die aktuellen Songs und Playlists in der CSV-Datei.
add_song(): Ermöglicht dem Benutzer, einen neuen Song hinzuzufügen.
create_playlist(): Ermöglicht dem Benutzer, eine neue Playlist zu erstellen.
add_song_to_playlist(): Ermöglicht dem Benutzer, einen vorhandenen Song zu einer bestehenden Playlist hinzuzufügen.
bubble_sort(songs, key): Implementiert den Bubble-Sort-Algorithmus, um Songs nach einem bestimmten Schlüssel (z.B. Titel oder Likes) zu sortieren.
search_songs(): Bietet dem Benutzer die Möglichkeit, nach Songs zu suchen, entweder durch lineare oder binäre Suche.
sort_songs(): Ermöglicht dem Benutzer, Songs zu sortieren, indem er einen Algorithmus auswählt (Bubble Sort oder Shell Sort).
Suchmethoden
Die Suchmethoden sind besonders wichtig, um eine schnelle und effiziente Suche in der Songliste zu ermöglichen.

linear_search(songs, key, lookup): Durchsucht die Liste der Songs linear nach einem bestimmten Schlüssel und gibt die gefundenen Songs zurück.
binary_search(songs, key, lookup): Führt eine binäre Suche in der Liste der Songs durch, um einen bestimmten Song zu finden.
Sortiermethoden
Die Sortiermethoden ermöglichen es, die Songs nach verschiedenen Kriterien zu ordnen.

bubble_sort(songs, key): Sortiert die Songs mithilfe des Bubble-Sort-Algorithmus. Es ist einfach zu implementieren, jedoch möglicherweise weniger effizient bei größeren Datensätzen.
shell_sort(songs, key): Führt eine Sortierung mithilfe des Shell-Sort-Algorithmus durch, der eine verbesserte Effizienz im Vergleich zum einfachen Bubble-Sort bietet.
Nutzung der Musik-App
Um die Musik-App zu nutzen, folgt der Benutzer den untenstehenden Schritten:

Start der Anwendung: Die App kann durch Ausführen des Python-Skripts gestartet werden. Die Anwendung lädt die Daten aus der angegebenen CSV-Datei.

Interaktion mit dem Benutzer: Die Benutzeroberfläche fordert den Benutzer auf, verschiedene Aktionen auszuwählen, wie das Hinzufügen eines Songs, das Erstellen einer Playlist oder das Suchen von Songs.

Datenverwaltung:

Songs hinzufügen: Der Benutzer kann neue Songs mit allen erforderlichen Informationen hinzufügen.
Playlists erstellen: Benutzer können eigene Playlists erstellen und Songs hinzufügen.
Songs suchen: Die App ermöglicht die Suche nach Songs mithilfe von linearen oder binären Suchalgorithmen.
Sortieren von Songs: Benutzer können ihre Songs nach verschiedenen Kriterien sortieren.
Speichern von Daten: Nach Änderungen werden die aktuellen Songs und Playlists automatisch in der CSV-Datei gespeichert, um die Persistenz der Daten sicherzustellen.

Beenden der Anwendung: Der Benutzer kann die Anwendung schließen, wobei alle Änderungen automatisch gespeichert werden.

Fazit
Die Musik-App ist ein benutzerfreundliches Tool zur Verwaltung von Musik-Songs und Playlists. Durch die Implementierung grundlegender Funktionen wie Hinzufügen, Suchen und Sortieren von Songs bietet die App eine solide Grundlage für eine Musikverwaltungslösung. Zukünftige Erweiterungen könnten zusätzliche Funktionen wie die Unterstützung von Benutzeranmeldungen oder eine grafische Benutzeroberfläche umfassen.
