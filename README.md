# DocumentForgery
# Aadhaar Forgery Detector

## Overview
The Aadhaar Forgery Detector is a Python-based application designed to analyze Aadhaar card images and PDFs for signs of forgery. It checks for various authenticity parameters, including text accuracy, document layout, security features, and image manipulations.

## Features
- **Basic Checks**: Verifies dimensions, image quality, and standard layout.
- **Content Analysis**: Extracts Aadhaar number and validates text positions.
- **Security Features**: Checks for holograms, ghost images, and micro text.
- **Visual Analysis**: Detects digital manipulations, color inconsistencies, and print patterns.

## Installation
### Prerequisites
Ensure you have the following dependencies installed:
- Python 3.7+
- OpenCV (`cv2`)
- NumPy
- Tesseract OCR
- Pillow
- pdf2image
- Poppler (for PDF conversion)

### Install Dependencies
Run the following command:
```bash
pip install opencv-python numpy pytesseract pillow pdf2image
```

### Install Poppler
#### Windows:
1. Download Poppler from [here](https://github.com/oschwartz10612/poppler-windows/releases).
2. Extract the downloaded file and note the path to `poppler/bin`.
3. Add the following to your script:
   ```python
   import os
   poppler_path = r"C:\path\to\poppler\bin"  # Update with your actual path
   os.environ["PATH"] += os.pathsep + poppler_path
   ```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install poppler-utils
```

#### Mac (Homebrew):
```bash
brew install poppler
```

## Usage
### Running the Detector
```python
from aadhar_forgery_detector import AadharForgeryDetector

detector = AadharForgeryDetector()
result = detector.analyze_aadhaar("path_to_aadhaar_card.pdf")
print(result)
```

### Sample Output
```json
{
  "is_forgery": false,
  "forgery_likelihood": 0.2,
  "analysis_details": {
    "basic_checks": {"dimensions_valid": true, "quality_sufficient": true, "layout_valid": true},
    "content_analysis": {"aadhaar_number_valid": true, "text_positions_valid": true},
    "security_features": {"hologram_detected": true, "ghost_image_valid": true},
    "visual_analysis": {"manipulation_detected": false, "color_consistent": true}
  },
  "recommendations": ["No significant signs of forgery detected"]
}
```

## Contributing
Feel free to fork this repository and submit pull requests with enhancements and bug fixes.

## License
This project is licensed under the MIT License.

