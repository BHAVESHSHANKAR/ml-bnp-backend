# ML Backend Installation Guide

## Quick Start (Minimal Setup)

### 1. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac  
source venv/bin/activate
```

### 2. Install Core Dependencies
```bash
# Option 1: Use the simple installer
python install.py

# Option 2: Install minimal requirements
pip install -r requirements-minimal.txt

# Option 3: Install manually
pip install flask flask-cors requests pillow pandas python-dateutil werkzeug
```

### 3. Start Server
```bash
python server.py
```

The server will start on http://localhost:5001 with basic functionality.

## Full Setup (All Features)

### 1. Install System Dependencies

#### Windows
- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Install Poppler: https://blog.alivate.com.au/poppler-windows/

#### macOS
```bash
brew install tesseract
brew install poppler
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils
```

### 2. Install Python Dependencies
```bash
# Install all dependencies
pip install -r requirements.txt

# Install spaCy model
python -m spacy download en_core_web_sm
```

## Features by Dependency

### Core Features (Always Available)
- ✅ Text file processing
- ✅ Basic text extraction
- ✅ REST API endpoints
- ✅ File upload handling

### Optional Features

#### With pytesseract + pdf2image
- ✅ PDF OCR processing
- ✅ Image text extraction

#### With python-docx
- ✅ DOCX file processing
- ✅ Word document text extraction

#### With spacy
- ✅ Named Entity Recognition (NER)
- ✅ Advanced name extraction
- ✅ Better text processing

#### With pycountry
- ✅ Comprehensive country detection
- ✅ ISO country codes
- ✅ Country name normalization

#### With python-dateutil
- ✅ Advanced date parsing
- ✅ Multiple date formats
- ✅ DOB and expiry detection

## Troubleshooting

### Common Issues

#### 1. Package Installation Fails
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install packages individually
pip install flask
pip install flask-cors
pip install requests
```

#### 2. SpaCy Model Not Found
```bash
# Try different installation methods
python -m spacy download en_core_web_sm

# Or install from wheel
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl
```

#### 3. Tesseract Not Found
- Make sure Tesseract is installed and in PATH
- On Windows, add Tesseract to system PATH
- Test with: `tesseract --version`

#### 4. PDF Processing Fails
- Install poppler-utils (Linux) or poppler (macOS/Windows)
- Ensure PDF files are not corrupted
- Check file permissions

## Testing Installation

### 1. Test Server
```bash
curl http://localhost:5001/
```

### 2. Test File Processing
```bash
curl -X POST -F "file=@test.txt" http://localhost:5001/process-single
```

## Minimal Working Example

If you just want to test the integration:

```bash
# Install only core dependencies
pip install flask flask-cors requests

# Start server
python server.py
```

The server will work with limited functionality but will handle the integration with the Express backend.