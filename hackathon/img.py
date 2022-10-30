import cv2


def vid():
    cap = cv2.VideoCapture(0)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

    while True:
        ret, frame = cap.read()

        writer.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()


def imagep():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")

    cv2.imshow("test", frame)
    cv2.waitKey(3000)
    # SPACE pressed
    img_name = "opencv_frame_{}.png".format(0)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))

    cam.release()

    cv2.destroyAllWindows()