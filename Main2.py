import cv2
import numpy as np
import matplotlib.pyplot as plt

def check_forgery(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(" Error: Unable to read the image. Check the file path.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 50, 50)

    # Analyze noise patterns
    noise = cv2.fastNlMeansDenoising(gray, None, 7, 7, 7)

    # Calculate the difference between original and denoised image
    difference = cv2.absdiff(gray, noise)
    mean_diff = np.mean(difference)

     # Display images using Matplotlib (which properly handles large images)
    fig, axs = plt.subplots(1, 1, figsize=(0, 0))

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detection", edges)
    cv2.imshow("Noise Analysis", noise)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Simple threshold for forgery detection
    if mean_diff > 0.5:  
        print("\n Forgery Detected: The image appears to be manipulated!")
    else:
        print("\n No Forgery Detected: The image appears authentic.")

# Example usage
image_path = r"C:\Users\Ved Thombre\Downloads\Rudra (1).png"  # Your image path
check_forgery(image_path)

