# DocumentForgery
# Aadhaar Forgery Detector

A lightweight Python-based application that detects possible forgery in Aadhaar card images or PDFs. Built in under 24 hours during a hackathon, this project blends **image processing**, **OCR**, and **visual forensic analysis** into a minimal yet powerful tool.

---

## 🔍 What Does It Do?

The Aadhaar Forgery Detector runs a series of checks to identify inconsistencies or manipulations in Aadhaar documents. These include:

* **Basic structural checks**: image dimensions, DPI, document layout.
* **Text validation**: OCR-based extraction of Aadhaar numbers and layout-based verification.
* **Security element detection**: ghost images, micro-text, hologram positioning.
* **Forgery prediction**: analyzing color balance, noise artifacts, and signs of tampering.

If any suspicious elements are detected, the tool reports a **likelihood of forgery** along with detailed insights.

---

## 📂 Dataset Used

This project was developed using **open-source sample Aadhaar images and dummy PDFs** available for research purposes. No private or confidential data was used.

If you're looking to test the system:

* Use official-looking test PDFs/images (blurred or watermarked).
* You can generate fake test documents using tools like Photoshop (for tampering) to simulate forged Aadhaar cards.

---

## ⚙️ Installation

### 🔧 Prerequisites

Make sure the following are installed:

* Python 3.7+
* Tesseract OCR (must be installed system-wide)
* Poppler (for PDF to image conversion)

### 📦 Install Python Dependencies

```bash
pip install opencv-python numpy pytesseract pillow pdf2image
```

### 📥 Install Poppler

#### Windows:

1. Download Poppler: [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
2. Extract and set the path in your script:

```python
import os
poppler_path = r"C:\path\to\poppler\bin"
os.environ["PATH"] += os.pathsep + poppler_path
```

#### Linux:

```bash
sudo apt update
sudo apt install poppler-utils
```

#### Mac:

```bash
brew install poppler
```

---

## 🚀 How to Run

```python
from aadhar_forgery_detector import AadharForgeryDetector

detector = AadharForgeryDetector()
result = detector.analyze_aadhaar("path_to_aadhaar_card.pdf")
print(result)
```

---

## 🧪 Sample Output

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

---

## 🤝 Contributing

Want to add ML-based forgery classification? Or UI integration? PRs are welcome. Fork this repo, experiment, and raise a pull request with improvements.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).



