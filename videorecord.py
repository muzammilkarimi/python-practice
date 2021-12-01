import cv2
def main():
    windowname="live video Feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    if(cap.isOpened()):
        ret,frame=cap.read()
    else:
        rat=False
    while(ret):
        ret,frame=cap.read()
        cv2.imshow(windowname,frame)
        if cv2.waitkey(1)==27:
            break
        cv2.destroyAllWindows()
        cap.release()

main()

