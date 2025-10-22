#!/usr/bin/env python3
"""
Test script to verify the ATS application setup
"""

import os
from dotenv import load_dotenv

def test_setup():
    print("🔍 Testing ATS Application Setup...")
    print("=" * 50)
    
    # Test 1: Environment variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key and api_key != "your_google_api_key_here":
        print("✅ Google API Key: Configured")
    else:
        print("❌ Google API Key: Not configured")
        return False
    
    # Test 2: Required modules
    try:
        import streamlit as st
        print("✅ Streamlit: Available")
    except ImportError:
        print("❌ Streamlit: Not available")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI: Available")
    except ImportError:
        print("❌ Google Generative AI: Not available")
        return False
    
    try:
        import pdf2image
        print("✅ PDF2Image: Available")
    except ImportError:
        print("❌ PDF2Image: Not available")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow (PIL): Available")
    except ImportError:
        print("❌ Pillow (PIL): Not available")
        return False
    
    # Test 3: Google AI Configuration
    try:
        genai.configure(api_key=api_key)
        print("✅ Google AI: Configured successfully")
    except Exception as e:
        print(f"❌ Google AI Configuration: Failed - {e}")
        return False
    
    print("=" * 50)
    print("🎉 All tests passed! Your ATS application is ready to run.")
    print("=" * 50)
    print("\nTo run the application:")
    print("1. Open a new terminal/command prompt")
    print("2. Navigate to your project directory")
    print("3. Run: streamlit run app.py")
    print("4. Open your browser to the URL shown (usually http://localhost:8501)")
    
    return True

if __name__ == "__main__":
    test_setup()
