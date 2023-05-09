
#import vlc
import urllib.request
import re
import urllib
import os

def splitSentence(sentence):
    return re.findall(r"\b\w+\b", sentence)


def Finder(Search):
    words = splitSentence(Search)
    for word in words:
    # Properly encode search query
        signSearch = urllib.parse.quote(word + " asl dictionary")
        URL = f'https://youtube.com/results?search_query={signSearch}'

        html = urllib.request.urlopen(URL)
        videoIds = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        videoURL = "https://youtube.com/watch?v=" + videoIds[0]

        with open("URLLinks.txt", "a") as linkFile:
            linkFile.write(videoURL + "\n")
        linkFile.close()

    
    


def Clear():
    linkFile2 = open('URLLinks.txt', 'r+')
    linkFile2.truncate(0)
    linkFile2.close()  # Close the file after truncating
    
    directory = r"C:\Users\iamsa\Desktop\Code\AVERIS\VideoFiles"  # Raw string to handle backslashes
    for f in os.listdir(directory):
        if f.endswith(".mp4"):
            file_path = os.path.join(directory, f)
            os.remove(file_path)





#player = vlc.MediaPlayer(videoURL)
#player.play()

#print(htmlContent)
#above print leads to literal hundreds of lines of class \n
#i think its the full HTML of the search page
