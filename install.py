#!/usr/bin/env python3
"""
Simple installation script for ML Backend
"""

import subprocess
import sys

def install_package(package):
    """Install a single package"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Installed {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        return False

def main():
    print("🚀 Installing ML Backend Dependencies...")
    
    # Upgrade pip first
    print("📦 Upgrading pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    
    # Core dependencies (must have)
    core_packages = [
        "flask",
        "flask-cors", 
        "requests",
        "pillow",
        "pandas",
        "python-dateutil",
        "werkzeug"
    ]
    
    print("\n📦 Installing core dependencies...")
    for package in core_packages:
        install_package(package)
    
    # ML/OCR dependencies (optional but recommended)
    ml_packages = [
        "pytesseract",
        "pdf2image",
        "spacy",
        "pycountry",
        "python-docx",
        "openpyxl",
        "PyPDF2"
    ]
    
    print("\n🤖 Installing ML dependencies...")
    for package in ml_packages:
        if not install_package(package):
            print(f"⚠️ {package} failed to install, continuing...")
    
    # Try to install spaCy model
    print("\n🧠 Installing spaCy English model...")
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        print("✅ SpaCy model installed successfully")
    except:
        print("⚠️ SpaCy model installation failed. NLP features may be limited.")
    
    print("\n🎉 Installation completed!")
    print("To start the server: python server.py")

if __name__ == "__main__":
    main()