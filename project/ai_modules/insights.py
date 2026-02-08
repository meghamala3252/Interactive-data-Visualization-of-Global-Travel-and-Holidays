import pytesseract
import cv2
import numpy as np
import os
from project.config import Config

# Point to tesseract exe if needed (Windows)
pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_CMD

def extract_text_from_image(image_path):
    try:
        if not os.path.exists(Config.TESSERACT_CMD):
            return "Tesseract OCR not found. Please install it to enable text extraction."
            
        img = cv2.imread(image_path)
        if img is None:
            return "Error loading image."
            
        # Preprocessing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Thresholding
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        text = pytesseract.image_to_string(thresh)
        return text
    except Exception as e:
        print(f"OCR Error: {e}")
        return f"Error processing image: {str(e)}"


def generate_insights_from_data(text_data, metadata):
    # This is where you would call OpenAI or a local LLM
    # For now, we use a simple rule-based stub or mock response
    
    insights = []
    
    if "increase" in text_data.lower():
        insights.append("The data indicates a positive trend.")
    
    if "decrease" in text_data.lower():
        insights.append("The data indicates a downward trend.")
        
    insights.append(f"Analysis based on dashboard: {metadata.get('title', 'Unknown')}")
    
    # Mock sophisticated output
    return [
        "Tourist arrivals peaked in the summer months.",
        "France remains the top destination based on visual data.",
        "There is a 15% increase in spending compared to last year."
    ]
