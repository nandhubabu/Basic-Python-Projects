import cv2
import pytesseract
from PIL import Image

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the input image
image_path = "input/image copy.png"

# Load the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to binarize the image
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Extract text from the preprocessed image using Tesseract
text = pytesseract.image_to_string(thresh, lang="eng")

# List of unwanted symbols to remove
unwanted_symbols = ["!", "#", "@", "$", "%", "^", "&", "*", "]", "�", "-"]

# Remove unwanted symbols from the extracted text
for symbol in unwanted_symbols:
    text = text.replace(symbol, "")

# Save the cleaned text to a file
output_path = "output/ocr_output.txt"
with open(output_path, 'w') as file:
    file.write(text)

# Print confirmation message
print(f"Text saved to {output_path}")