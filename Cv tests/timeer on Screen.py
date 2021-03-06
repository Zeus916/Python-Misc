import cv2
import sys
from datetime import datetime

# Initialize variables
camSource = 0
running = True
saveCount = 0
nSecond = 0
totalSec = 4
strSec = '3210'
# keyPressTime = 0.0
startTime = 0.0
timeElapsed = 0.0
startCounter = False
# endCounter = False

# Start the camera
camObj = cv2.VideoCapture(camSource)
if not camObj.isOpened():
    sys.exit('Camera did not provide frame.')

# Start video stream
while running:
    readOK, frame = camObj.read()

    # Display counter on screen before saving a frame
    if startCounter:
        if nSecond < totalSec: 
            # draw the Nth second on each frame 
            # till one second passes  
            cv2.putText(img = frame, 
                        text = strSec[nSecond],
                        org = (100,100), 
                        fontFace = cv2.FONT_HERSHEY_DUPLEX, 
                        fontScale = 2, 
                        color = (255,0,255),
                        thickness = 2)

            timeElapsed = (datetime.now() - startTime).total_seconds()
#            print 'timeElapsed: {}'.format(timeElapsed)

            if timeElapsed >= 1:
                nSecond += 1
#                print 'nthSec:{}'.format(nSecond)
                timeElapsed = 0
                startTime = datetime.now()

        else:
            cv2.imwrite('img' + str(saveCount) + '.jpg', frame)  
#            print 'saveTime: {}'.format(datetime.now() - keyPressTime)

            saveCount += 1
            startCounter = False
            nSecond = 1

    # Get user input
    keyPressed = cv2.waitKey(3)
    if keyPressed == ord('s'):
        startCounter = True
        startTime = datetime.now()
#        print 'startTime: {}'.format(startTime)
#        print 'keyPressTime: {}'.format(keyPressTime)

    elif keyPressed == ord('q'):
        # Quit the while loop
        running = False
        cv2.destroyAllWindows()

    # Show video stream in a window    
    cv2.imshow('video', frame)

camObj.release()