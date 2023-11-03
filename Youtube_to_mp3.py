# importing packages 
from pytube import YouTube 
from pytube import Search
import os 

# Takes in a the name of a video downloads the audio from it
def Download(userInput, preface = "", destination = os.path.dirname(__file__)):
    # create YouTube video object with url either from input or search
    yt = YouTube(Search(userInput).results[0].watch_url) 
    
    try:
        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 
        
        # download the file 
        out_file = video.download(output_path=destination) 

        # save the file 
        base, ext = os.path.splitext(out_file)
        name = os.path.basename(base) 
        new_file = destination + "\\" + preface + name + '.mp3'
        os.rename(out_file, new_file) 

        # result of success 
        # print(yt.title + " has been successfully downloaded.")

    except FileExistsError:
        print("File already exists")

    except:
        print("An error has occurred")