#!/usr/bin/env python3
"""
Setup script for ML Backend
This script installs all required dependencies and downloads the spaCy model
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🚀 Setting up ML Backend for Document Processing...")
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
    else:
        print("⚠️  Warning: Not in a virtual environment. Consider using 'python -m venv venv' first")
    
    # Upgrade pip first
    print("🔧 Upgrading pip...")
    run_command("python -m pip install --upgrade pip", "Upgrading pip")
    
    # Install requirements with fallback
    print("🔧 Installing Python dependencies...")
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        print("⚠️ Trying to install dependencies individually...")
        
        # Try installing core dependencies individually
        core_deps = [
            "flask>=2.0.0",
            "flask-cors>=3.0.0", 
            "requests>=2.25.0",
            "pillow>=9.0.0",
            "pandas>=1.5.0",
            "python-dateutil>=2.8.0"
        ]
        
        for dep in core_deps:
            run_command(f"pip install '{dep}'", f"Installing {dep}")
        
        # Try optional dependencies
        optional_deps = [
            "pytesseract>=0.3.0",
            "pdf2image>=1.16.0", 
            "spacy>=3.4.0",
            "pycountry>=22.1.0",
            "python-docx>=0.8.0",
            "openpyxl>=3.0.0"
        ]
        
        for dep in optional_deps:
            if not run_command(f"pip install '{dep}'", f"Installing {dep}"):
                print(f"⚠️ Optional dependency {dep} failed to install")
    
    # Download spaCy model
    print("🔧 Downloading spaCy English model...")
    if not run_command("python -m spacy download en_core_web_sm", "Downloading spaCy English model"):
        print("⚠️ SpaCy model download failed. Trying alternative installation...")
        if not run_command("pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl", "Installing spaCy model from wheel"):
            print("❌ Failed to download spaCy model. The server will work but NLP features may be limited.")
    
    # Install system dependencies (if needed)
    print("\n📋 System Dependencies Check:")
    print("Make sure you have the following system dependencies installed:")
    print("- Tesseract OCR: https://github.com/tesseract-ocr/tesseract")
    print("- Poppler (for PDF processing): https://poppler.freedesktop.org/")
    
    if sys.platform.startswith('win'):
        print("\nFor Windows:")
        print("- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki")
        print("- Install Poppler: https://blog.alivate.com.au/poppler-windows/")
    elif sys.platform.startswith('darwin'):
        print("\nFor macOS:")
        print("- brew install tesseract")
        print("- brew install poppler")
    else:
        print("\nFor Linux (Ubuntu/Debian):")
        print("- sudo apt-get install tesseract-ocr")
        print("- sudo apt-get install poppler-utils")
    
    print("\n🎉 ML Backend setup completed!")
    print("To start the server, run: python server.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)