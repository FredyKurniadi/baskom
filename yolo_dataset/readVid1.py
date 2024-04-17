import cv2
import numpy as np

def f1():
    # Load the video
    video_path = 'vid1.mp4'
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        exit()

    # Get the dimensions of the image
    height, width = 478, 848

    t = 0

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if ret:
            # Convert the frame to HSV
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Get current trackbar positions
            h_min = 162
            s_min = 77
            v_min = 109
            h_max = 186
            s_max = 236
            v_max = 255

            # Define lower and upper HSV thresholds
            lower_bound = np.array([h_min, s_min, v_min])
            upper_bound = np.array([h_max, s_max, v_max])

            # Create a mask using the thresholds
            mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

            # Find indices of non-black pixels
            non_black_pixels = np.where(mask != 0)

            # Calculate the bounding box
            if non_black_pixels[0].size > 0:
                y_min, y_max = np.min(non_black_pixels[0]), np.max(non_black_pixels[0])
                x_min, x_max = np.min(non_black_pixels[1]), np.max(non_black_pixels[1])
                
                cv2.imwrite(f'images/img{t}.jpg', frame)
                # Draw rectangle around the white area
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                
                # print(f"x_min: {x_min}, y_min: {y_min}, x_max: {x_max}, y_max: {y_max}")

                # Open a text file in write mode
                with open(f'labels/img{t}.txt', 'w') as file:
                    # Write some text to the file
                    file.write(f"0 {(x_max+x_min)/(2*width)} {(y_max+y_min)/(2*height)} {(x_max-x_min)/width} {(y_max-y_min)/height}")

                print(f"images/img{t}.jpg")
            else:
                x_min, y_min, x_max, y_max = 0, 0, 0, 0

            # Display the result
            cv2.imshow('image', frame)

            # Press 'q' to exit the video
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
        
        t+=1

    # Release the VideoCapture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
