import os
import cv2

def Player():
    folderPath = r"C:\Users\iamsa\Desktop\Code\AVERIS\VideoFiles"
    fileList = os.listdir(folderPath)
    videoFiles = [file for file in fileList if file.endswith(".mp4")]
    
    for videoFile in videoFiles:
        mp4File = os.path.join(folderPath, videoFile)

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
 
