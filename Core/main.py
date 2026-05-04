import cv2 as cv
import numpy as np

img = cv.imread('../Resources/messi5.jpg') # Read the image
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[100,100] # Get pixel value at (100, 100)
print(px) # Print the BGR values of the pixel

color = img[100, 100, 0] # Third parameter is the color channel (0: Blue, 1: Green, 2: Red)

# Image pixels can be modified by assigning new values to them
# img[100,100] = [255,255,255]

# Accessing a Region of Interest (ROI)
ball = img[372:442, 410:480] # Define the ROI (y1:y2, x1:x2) (Ball size = 70x70)
img[273:343, 100:170] = ball # Copy the ROI to another location in the image (Ball size = 70x70)

(b, g, r) = cv.split(img) # Split colors from image
# ^ Costly Operation, use with caution
img = cv.merge((b, g, r)) # Merge the channels back to an image

print(b, g, r)

img[:, :, 2] = 255 # Set the red channel to zero (remove red color from the image)

cv.imshow("Messi", img)           # Display the image in a window called 'Messi'
if cv.waitKey(0) & 0xFF == ord('q'):    # Wait for a key press
    cv.destroyAllWindows()