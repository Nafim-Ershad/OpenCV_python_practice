import cv2 as cv
import numpy as np

if __name__ == "__main__":
    
    print("OpenCV:", cv.__version__)
    
    img = np.zeros((120, 400, 3), dtype=np.uint8) # Generate a black image

    cv.putText(img, "Hello World!!", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3) # Write "Hello World!!" on the image
    # image_instance, text, position, font, font_scale, color, thickness
    
    cv.imwrite("hello.png", img)   # Save the image to the specified path
    cv.imshow("Hello World", img)           # Display the image in a window
    if cv.waitKey(0) & 0xFF == ord('q'):    # Wait for a key press
        cv.destroyAllWindows()             # Close all windows