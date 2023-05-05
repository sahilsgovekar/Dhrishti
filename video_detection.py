import cv2

# cap= cv2.VideoCapture(0)

def video_capture(cap, speech):
    width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer= cv2.VideoWriter('emergencyvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))


    while True:
        ret,frame= cap.read()

        writer.write(frame)

        cv2.imshow('frame', frame)

        speech.Text2Speech("video capturing")
        cond = speech.Speech2Text()
        if cond == "stop" or cond == 's':
            break

        if cv2.waitKey(1) & 0xFF == 27:
            break


    cap.release()
    writer.release()
    cv2.destroyAllWindows()
