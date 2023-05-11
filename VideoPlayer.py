
import os
import cv2
def Player():
    folderPath= (r"C:\Users\iamsa\Desktop\Code\AVERIS\VideoFiles")
    mp4File = None
    while mp4File is None:
        fileList = os.listdir(folderPath)
        videoFiles = [file for file in fileList if file.endswith(".mp4")]
    if videoFiles:
        mp4File = os.path.join(folderPath, videoFiles[0])
        
    cap = cv2.VideoCapture(mp4File)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
Player()
 