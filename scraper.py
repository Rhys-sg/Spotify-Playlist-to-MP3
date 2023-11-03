import time
import requests
from bs4 import BeautifulSoup

# gets the title and author from a spotify page, either a playlist name/author or a song name/author
def get_title(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    # Title is in the form "{NAME} - song and lyrics by {ARTIST} | Spotify"
    song = soup.find("title").text
    seperator = " - song and lyrics by "
    title = song[:song.find(seperator)]
    artist = song[song.find(seperator) + len(seperator) : song.rfind(" |")]
    return (title, artist)
    
# gets the list of links to songs from a spotify playlist
def get_songs_authors(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    song_links = soup.find_all("meta", {"name":"music:song"})
    titles = []
    for i in range(len(song_links)):
        # time.sleep(1) # To avoid sending too many requests and getting blocked by Spotify
        name_author = get_title(song_links[i]["content"])
        
        # if song not found, print message, skip it
        if name_author[1] == "Page not available": 
            print("Song " + str(i+1) + " not found")
            continue
        titles.append(name_author[0] + " by " + name_author[1])
    return titles