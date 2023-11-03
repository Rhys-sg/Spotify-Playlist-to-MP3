import Youtube_to_mp3
import scraper
import os 

def main():
    # prompts user for link to playlist
    userInput = str(input("Enter the URL of the Spotify Playlist you want to download: \n>> "))
    print("Downloading...")

    # playlist title and author, if private or not found, returns "Page not available"
    playlistName, ext = scraper.get_title(userInput)
    if playlistName == "Page not available":
        print("Playlist not found")
        return
    
    # gets list of songs from playlist
    songs = scraper.get_songs_authors(userInput)

    # creates folder for playlist
    newpath = createFolder(playlistName.split(" |", 1)[0])

    # downloads songs into folder, in order
    for order, song in enumerate(songs):
        Youtube_to_mp3.Download(song, str(order+1) + ". ", newpath)

    print("Download complete")

# creates folder for playlist
def createFolder(playlistName):
    path = os.path.dirname(__file__) + "\\" + playlistName
    if not os.path.exists(path):
        os.makedirs(path)
    return path

main()