from pytube import YouTube

#your file path here
savePath = r"C:\" 
def Downloader():
    with open("URLLinks.txt", "r") as link:
        for i in link:
         try:
            # Create a YouTube object
            yt = YouTube(i)

            # Filter the streams to get mp4 files
            mp4files = yt.streams.filter(file_extension='mp4')

            # Get the highest resolution video
            d_video = mp4files.get_highest_resolution()

            # Download the video
            d_video.download(savePath)
            print("Download completed for:", i)
         except Exception as e:
              print("Error occurred:", str(e))

Downloader()
print('Task Completed!')
