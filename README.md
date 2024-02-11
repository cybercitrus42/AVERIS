# AVERIS
Automatic Video Encoder Rendering Interpretation in Sign

The goal of this project is a search tool that generates a one-to-one direct American Sign Language (ASL) translation in the form in a video in a singular program.

HOW IT WORKS:
- Initial design utilizes the YouTube URL system to generate a YouTube search page of translation videos

-The second design accesses the HTML data of the YouTube search page and looking for the first video with "/watch?v=" in the URL. This, later defined and formatted as the Finder function, will be the base function of the program. 

- The GUI It uses two created functions:
    Finder()
    Clear()
    The end of the Finder() function opens the “URLLinks” text file and prints the found URLs. The Clear() Function erases all text in the “URLLinks” text file, and later all downloaded videos.

- This splitSentence(sentence) function identifies spaces in the search term and separates the words. 

- Downloader() function:
   1.retrieves the URLs placed in the URLLinks text file
   2.finds the mp4 file on YouTube
   3.Downloads the mp4 
   4.places the mp4 into the “Video Files” folder. 

-Player() Function
 When activated this function searches the “Video Files” folder for mp4 files. If found, the function plays each mp4 file found in a pop-up window.

-When the helloButton is clicked it:
    1.Feeds the user input into the Finder()
    2.Runs the Downloader() on the text in the “URLLinks” file
    3.Opens a new window with the playButton.

-When the playButton is clicked:
  1.It checks for mp4 files in the folder
  2.If found, The Player() function is run




Copyright Samantha "cybercitrus" Orange
-
