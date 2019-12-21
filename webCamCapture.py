import cv2,time

video = cv2.VideoCapture(0)
    
print("Press q to Quit \n")

frame_counter = 0
start_time = time.time()
while True:
    frame_counter = frame_counter+1
    check,frame = video.read()

    frame=cv2.resize(frame,(int(frame.shape[1]),int(frame.shape[0])))
        
    cv2.imshow("Video Playback",frame)
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break

print("Number of frames :: %d" %frame_counter)
print("FPS: ", frame_counter / (time.time() - start_time))
video.release()
cv2.destroyAllWindows()
