
#import vlc
import urllib.request
import re
import urllib

def Finder(Search):
    
    # Properly encode search query
    signSearch = urllib.parse.quote(Search + " asl dictionary")
    URL = f'https://youtube.com/results?search_query={signSearch}'

    html = urllib.request.urlopen(URL)
    videoIds = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    videoURL = "https://youtube.com/watch?v=" + videoIds[0]

    with open("URLLinks.txt", "a") as linkFile:
        linkFile.write(videoURL + "\n")
    linkFile.close()





#player = vlc.MediaPlayer(videoURL)
#player.play()

#print(htmlContent)
#above print leads to literal hundreds of lines of class \n
#i think its the full HTML of the search page
